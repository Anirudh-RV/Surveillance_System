import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import IntroBar from './IntroBar'

class StreamingFile extends Component {
//TODO : ADD INTRODUCTION TO PROJECT

componentDidMount(){
// OnLoad function
// if counter exceeds 5, then stop process
this.count = 0;
}

keepupdating = () =>{
  while(this.count<50){
  console.log("Count : "+this.count)
  this.count = this.count + 1;
  this.liveFeedPlayer.src = "http://localhost:4000/CameraFeed/videoimages.jpeg";
  this.wait(1000);
  this.keepupdating();
  }
}

wait = (ms) =>{
var d = new Date();
var d2 = null;
do { d2 = new Date(); }
while(d2-d < ms);
}
  render() {
    return (
      <div className="App">
      <iframe className = "LiveFeed" ref = {c => this.liveFeedPlayer = c} src="http://localhost:4000/CameraFeed/videoimages.jpeg"></iframe>
      </div>
    );
  }
}
export default StreamingFile;
