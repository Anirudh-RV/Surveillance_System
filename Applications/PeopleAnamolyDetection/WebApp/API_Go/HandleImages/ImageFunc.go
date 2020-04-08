package HandleImages

import (
  "context"
  "log"
  "reflect"
  "unsafe"

  // MongoDB drivers
  "go.mongodb.org/mongo-driver/mongo"
  "go.mongodb.org/mongo-driver/mongo/options"
)

type Image_Names struct {
    Name  string
    Img_Name string
}

/*

Write function description here :

*/
func GetClientOptions() *options.ClientOptions {
  clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
  return clientOptions
}

/*

Write function description here :

*/
func GetClient (clientOptions *options.ClientOptions) *mongo.Client{
  client, err := mongo.Connect(context.TODO(), clientOptions)
  if err != nil {
    log.Fatal(err)
  }
  return client
}

/*

Write function description here :

*/
func GetCollection (client *mongo.Client,collectionname string) *mongo.Collection{
  collection := client.Database("GoDB").Collection(collectionname)
  return collection
}

/*

Write function description here :

*/
func BytesToString(b []byte) string {
    bh := (*reflect.SliceHeader)(unsafe.Pointer(&b))
    sh := reflect.StringHeader{bh.Data, bh.Len}
    return *(*string)(unsafe.Pointer(&sh))
}
