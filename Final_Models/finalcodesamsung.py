input_size = input_shape[:2]

# model to predict

img = cv2.imread('test.jpg')

print(img.shape)
img_h = img.shape[0]
img_w = img.shape[1]
print(img_h)
print(img_w)

img1 = np.copy(img)
img2 = np.zeros_like(img)

# model to predict
x = np.array([preprocess(img, input_size)])




#x = np.array([preprocess(img, input_size)])
with sl_graph.as_default():
    with sl_session.as_default():
        y = sl_model.predict(x)

result = prior_util.decode(y[0], confidence_threshold)

if len(result) > 0:
    bboxs = result[:,0:4]
    quads = result[:,4:12]
    rboxes = result[:,12:17]

    boxes = np.asarray([rbox3_to_polygon(r) for r in rboxes])

    xy = boxes
    xy = xy * [img_w, img_h]
    xy = np.round(xy)
    xy = xy.astype(np.int32)

    cv2.polylines(img1, tuple(xy), True, (0,0,255))

    rboxes = np.array([polygon_to_rbox(b) for b in np.reshape(boxes, (-1,4,2))])
    bh = rboxes[:,3]
    rboxes[:,2] += bh * 0.1
    rboxes[:,3] += bh * 0.2
    boxes = np.array([rbox_to_polygon(f) for f in rboxes])

    boxes = np.flip(boxes, axis=1) # TODO: fix order of points, why?
    boxes = np.reshape(boxes, (-1, 8))

    boxes_mask_a = np.array([b[2] > b[3] for b in rboxes]) # width > height, in square world
    boxes_mask_b = np.array([not (np.any(b < 0) or np.any(b > 512)) for b in boxes]) # box inside image
    boxes_mask = np.logical_and(boxes_mask_a, boxes_mask_b)

    boxes = boxes[boxes_mask]
    rboxes = rboxes[boxes_mask]
    xy = xy[boxes_mask]

    if len(boxes) == 0:
        boxes = np.empty((0,8))

    words = crop_words(img, boxes, input_height, width=input_width, grayscale=True)
    words = np.asarray([w.transpose(1,0,2) for w in words])

    if len(words) > 0:
        with crnn_graph.as_default():
            with crnn_session.as_default():
                res_crnn = crnn_model.predict(words)

    for i in range(len(words)):
        chars = [alphabet[c] for c in np.argmax(res_crnn[i], axis=1)]
        res_str = decode(chars)
        #cv2.imwrite('croped_word_%03i.png' % (i), words[i])
        cv2.putText(img2, res_str,
            tuple(np.array((xy[i][0] + xy[i][3]) / 2, dtype=int)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255,255,255), 1)

# draw fps
cv2.rectangle(img1, (0,0), (50, 17), (255,255,255), -1)
cv2.putText(img1, fps, (3,10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,0), 1)

cv2.imwrite('Testout2.jpg', img1)
print("DONE!")
cv2.waitKey(10)
