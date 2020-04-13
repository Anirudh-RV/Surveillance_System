import React, { Component } from 'react';
import axios from 'axios';
import {Progress} from 'reactstrap';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import Cookies from 'universal-cookie';
import Home from './Home';
import NavigationBar from './NavigationBar';

class CompareFaceComponent extends Component {
  constructor(props) {
    super(props);
      this.state = {
        selectedFile: null,
        loaded:0,
        index:0,
      }
      this.nodeserverurl = "http://35.170.249.159"
      this.goapiurl = "http://54.197.42.159"
      this.pythonbackendurl = "http://itchy-puma-26.serverless.social"
  }

Logout = () =>{
    const cookies = new Cookies()
    cookies.remove('username');
    window.location.reload(false);
}
  checkMimeType=(event)=>{
    //getting file object
    let files = event.target.files
    //define message container
    let err = []
    // list allow mime type
    const types = ['image/png', 'image/jpeg', 'image/gif']
    // loop access array
    for(var x = 0; x<files.length; x++) {
     // compare file type find doesn't matach
         if (types.every(type => files[x].type !== type)) {
         // create error message and assign to container
         err[x] = files[x].type+' is not a supported format\n';
       }
     };
     for(var z = 0; z<err.length; z++) {// if message not same old that mean has error
         // discard selected file
        event.target.value = null
    }
   return true;
  }
  maxSelectFile=(event)=>{
    let files = event.target.files
        if (files.length > 1) {
           const msg = 'Only 1 images can be uploaded at a time'
           event.target.value = null
           return false;
      }
    return true;
 }
 checkFileSize=(event)=>{
  let files = event.target.files
  let size = 2000000
  let err = [];
  for(var x = 0; x<files.length; x++) {
  if (files[x].size > size) {
   err[x] = files[x].type+'is too large, please pick a smaller file\n';
 }
};
for(var z = 0; z<err.length; z++) {// if message not same old that mean has error
  // discard selected file
 event.target.value = null
}
return true;
}

getfacesfrommlbackend = (imageName) =>{
  console.log('in getfacesfrommlbackend')

  var username = this.props.location.state.userName;
  var imagename = imageName
  var url = this.nodeserverurl+"/comparefaces/"+imagename
  console.log('username : '+username)
  console.log('imagename : '+imagename)
  console.log('url : '+url)

  var data = {'username':username,'imagename':imagename,'imageurl':url}
  axios.post(this.pythonbackendurl+"/index/",data)
    .then(res => { // then print response status
      console.log(res)
      console.log(res['data'])

      var data = res['data']
      console.log(typeof data)
      var splitdata = data.split(',')
      var datalength = splitdata.length

      console.log('splitdata: ')
      // [&#x27;hardy2.jpg&#x27;, &#x27;hardy3.jpg&#x27;, &#x27;hardy1.jpg&#x27;] for str response
      // preprocess
      splitdata[0]  = splitdata[0].replace('[&#x27;', '')
      splitdata[0] = splitdata[0].replace('&#x27;','')
      splitdata[datalength-1]  = splitdata[datalength-1].replace('&#x27;', '')
      splitdata[datalength-1] = splitdata[datalength-1].replace('&#x27;]','')
      splitdata[datalength-1] = splitdata[datalength-1].replace(' ','')

      for(var i=1;i<datalength-1;i++){
        splitdata[i]  = splitdata[i].replace('&#x27;', '')
        splitdata[i] = splitdata[i].replace('&#x27;','')
        splitdata[i] = splitdata[i].replace(' ','')

      }
      this.showLength.innerHTML = "Number of matches : "+datalength;
      console.log(splitdata)
      this.MatchedImages = splitdata
      this.ImageTag.src = this.nodeserverurl+"/comparefaces/"+this.MatchedImages[this.state.index];
    })
    .catch(err => { // then print response status
    console.log(err)
    })
}


// using Api, add names of the images being uploaded to a database
addToBackendUsingApi = (files) =>{
      var sendToDjangoBackend = "";
      var fileNames = "CompareFaceDatabase,";
      for(var x =0; x<files.length-1;x++)
      {
        fileNames = fileNames +files[x].name+ ",";
        sendToDjangoBackend = sendToDjangoBackend + files[x].name+ ",";
      }
      fileNames = fileNames + files[files.length-1].name;
      sendToDjangoBackend = sendToDjangoBackend + files[files.length-1].name;
      console.log("filename : "+fileNames)
      // api call
      axios.post(this.goapiurl+"/insertimagedata",fileNames)
        .then(res => { // then print response status
          console.log(res)
          console.log('Sending to getfacesfrommlbackend')
          this.getfacesfrommlbackend(sendToDjangoBackend)
        })
        .catch(err => { // then print response status
        console.log(err)
        })
}

// && this.checkFileSize(event) taken out
onChangeHandler=event=>{
  var files = event.target.files
  if(this.maxSelectFile(event) && this.checkMimeType(event)){
  // if return true allow to setState
     this.setState({
     selectedFile: files,
     loaded:0
  })
}
}

RedirecToEditPage = () =>{
  var userName = this.props.location.state.userName;
  this.props.history.push({
    pathname: '/EditPage',
    state: {userName: this.props.location.state.userName}
})

}
  onClickHandler = () => {
    const data = new FormData()

    // getting username from input
    var userName = this.props.location.state.userName;

    // filling FormData with selectedFiles(Array of objects)
    for(var x = 0; x<this.state.selectedFile.length; x++) {
      data.append('file', this.state.selectedFile[x])
    }

    // header carries information of username to backend with data
    axios.post(this.nodeserverurl+"/upload",data,
    {
    headers: {
      userName: userName,
      type : 'CompareFaces'
    },
      onUploadProgress: ProgressEvent => {
        this.setState({
          loaded: (ProgressEvent.loaded / ProgressEvent.total*100),
        })
      },
    })
      .then(res => { // then print response status
        this.addToBackendUsingApi(this.state.selectedFile)
        // redirect to WorkingArea.js for viewing images
      })
      .catch(err => { // then print response status
      console.log(err)
      })

    }

    NextImage= () => {
      console.log('next image : '+this.MatchedImages)
      // clearing out previously draw boxes and adding back the image tag
      if(this.state.index>this.MatchedImages.length-2) {
        // Do nothing
      }
      else {
        this.state.index = this.state.index + 1
        if(this.ImageTag) {
          console.log(this.nodeserverurl+"/img/"+this.MatchedImages[this.state.index]);
         this.ImageTag.src = this.nodeserverurl+"/comparefaces/"+this.MatchedImages[this.state.index];
          }
        }
    }

    PrevImage= () => {
      // clearing out previously draw boxes and adding back the image tag
      if(this.state.index == 0) {
      }
      else {
      this.state.index = this.state.index - 1
      if(this.ImageTag) {
       this.ImageTag.src = this.nodeserverurl+"/comparefaces/"+this.MatchedImages[this.state.index];
        }
      }
    }

render() {
    return (
    <div>
    <body>
       <NavigationBar/>
    <section id = "1">
	     <div class="row">
          <div class="offset-md-3 col-md-6">
              <div class="form-group files">
                <label>Upload Your File </label>
                <input id="input_upload" type="file" class="form-control" multiple onChange={this.onChangeHandler}/>
              </div>
              <div class="form-group">
                <Progress max="100" color="success" value={this.state.loaded} >{Math.round(this.state.loaded,2) }%</Progress>
              </div>
              <button type="button" class="buttonclass" onClick={this.onClickHandler}>Check</button>
              <button type="button" class="buttonclass" onClick={this.Logout}>Log out</button>
	      </div>
      </div>
    </section>

    <section id="2">
    <p ref = {c => this.showLength = c}></p>
    <div className = "ImageContainer" ref = {c => this.ImgaeContainer = c}>
    <button type="button" class="buttonclass" onClick={this.PrevImage}>Previous</button>
    <button type="button" class="buttonclass" onClick={this.NextImage}>NEXT</button>
    <img className='name' ref = {c => this.ImageTag = c}/>
    </div>
    </section>


    </body>
    </div>
    );
  }
}

export default CompareFaceComponent;
