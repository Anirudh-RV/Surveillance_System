import React, { Component } from 'react';
import axios from 'axios';
import {Progress} from 'reactstrap';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import Cookies from 'universal-cookie';
import './App.css';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Bootstrap from "react-bootstrap";
import {FormGroup, FormControl} from "react-bootstrap";
import { Link } from 'react-router-dom';

class WelcomePage extends Component {

componentDidMount(){
// OnLoad function
// if counter exceeds 5, then stop process
this.heading.innerHTML = this.props.location.state.userName+"</br>Surveillance System";
}

dividetheframes = () =>{
  var username = this.props.location.state.userName
  var videoname =  this.videoname.value
  var imagetype = 'jpeg'
  var videourl = 'http://localhost:4000/videos/'+username+'/downloads/'+videoname+'.mp4'
  var low = '1'
  var high = '5'
  var data = {'username':username,'videoname':videoname,'videourl':videourl,'imagetype':imagetype,'low':low,'high':high}
  console.log("inside the testdjangoapi function : ")
  axios.post("http://127.0.0.1:8000/dividetheframes/",data)
    .then(res => { // then print response status
      //toast.success('upload success')
      console.log("API message : ")
      console.log(res)
      console.log(res.data["message"])
      if(this.DataRetrieved) {
       this.DataRetrieved.innerHTML = res.data["message"];
    }
    this.gotoeditpage();
    })
    .catch(err => { // then print response status
    //  toast.error('upload fail')
    console.log("fail")
    console.log(err)
    })
}

wait = (ms) =>{
var d = new Date();
var d2 = null;
do { d2 = new Date(); }
while(d2-d < ms);
}

SeeCameraFeed = () =>{
  var userName = this.props.location.state.userName;
  this.props.history.push({
    pathname: '/CameraFeed',
    state: {userName: this.props.location.state.userName}
})
}

StartAnnotation = () =>{
  var userName = this.props.location.state.userName;
  this.props.history.push({
    pathname: '/upload',
    state: {userName: this.props.location.state.userName}
})
}

Logout = () =>{
    const cookies = new Cookies()
    cookies.remove('username');
    window.location.reload(false);
}

handleSubmit = () =>{
  this.Message.innerHTML = "The process may take a few minutes..."
  axios.post("http://localhost:4000/download/",{
    username : this.props.location.state.userName,
    videoname : this.videoname.value,
    videourl : this.videourl.value,
  })
    .then(res => { // then print response status
      //toast.success('upload success')
      console.log(res)
      this.Message.innerHTML = "Download complete..."

    })
    .catch(err => {
    // then print response status
    //  toast.error('upload fail')
    console.log("fail")
    console.log(err)
    })
}

render() {
    return (
      <div className = "BackgroundSign">
      <h1 className = "AppName" ref = {c => this.heading = c}></h1>
      <div className="SignIn">
        <form>
        <p class = "SignInHead">Surveillance System</p>
        <p class = "SignUpHead">Some information about the system.</p>
        &nbsp;
          <FormGroup controlId="url" bsSize="large">
          <Button className="StartButton" block bsSize="large" onClick={this.SeeCameraFeed} type="button">
            See CameraFeed
          </Button>
          </FormGroup>

          <FormGroup controlId="url" bsSize="large">
          <Button className="StartButton" block bsSize="large" onClick={this.StartAnnotation} type="button">
            Start Annotation
          </Button>
          </FormGroup>

          <br/>
          <p className = "ErrorMessage" ref = {c => this.Message = c}></p>
        </form>
      </div>
      <div className="SecondBoxSignIn" ref = {c => this.Info = c}>
        <p className = "LinkToAccount"> Some LOGOUT option ?Click here&nbsp;
          <Link className="LinkToSignUp" onClick={this.Logout}>LOGOUT</Link>
        </p>
      </div>
      </div>
    );
  }
}

export default WelcomePage;