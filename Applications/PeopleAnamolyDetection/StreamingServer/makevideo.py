import os

directory_input = "OutputPhotos/"
frame_name = "output_"
directory_output = "OutputPhotos/"
output_video = "outputvideo"

frames_to_video = "ffmpeg -start_number 1 -i "+directory_input+frame_name+"%d.jpg -c:v libx264 -vf fps=30 -pix_fmt yuv420p "+directory_output+output_video+".mp4"
print(frames_to_video)
os.system(frames_to_video)
