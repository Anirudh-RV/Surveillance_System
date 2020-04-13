import React, { Component } from 'react';
import { Player } from 'video-react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import NavigationBar from './NavigationBar'
import "../../node_modules/video-react/dist/video-react.css";
import logo from './logo.svg';
import './App.css';
import { FormControl} from "react-bootstrap";
import StreamingFile from './StreamingFile'

class CameraFeed extends Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      playerSource: '',
      inputVideoUrl: ''
    };

    this.handleValueChange = this.handleValueChange.bind(this);
    this.updatePlayerInfo = this.updatePlayerInfo.bind(this);
    this.count = 0;
    this.nodeserverurl = ""
    this.goapiurl = ""
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state.playerSource !== prevState.playerSource) {
      this.player.load();
    }
  }

  handleValueChange(e) {
    const { value } = e.target;
    this.setState({
      inputVideoUrl: value
    });
  }

  updatePlayerInfo() {
    const { inputVideoUrl } = this.state;
    this.setState({
      playerSource:this.nodeserverurl+'/CameraFeed/'+inputVideoUrl
    });
  }

  CheckLiveFootage = () =>{
    if(this.count>50){
      // do nothing
    }
    else{
    console.log("count: "+this.count);
    this.count = this.count + 1;
    this.liveFeedPlayer.src = this.usercredentials.value;
  }
  }

  render() {
    return (
      <div className="App">
      <NavigationBar/>
      <h1>Check Camera feeds here :</h1>
      <section>
      <div className="columnLeftCamera">
        <Player
        playsInline
        poster="/assets/poster.png"
        fluid={false}
        width={480}
        height={540}
        autoPlay = {true}
        ref={player => {
            this.player = player;
          }}
          videoId="video-1"
        >
          <source src={this.state.playerSource} />
        </Player>
        </div>
        <div className="columnRightCamera">
        <div className="SignIn">
          <form>
          <p class = "SignInHead">Select Camera</p>
          <p class = "SignUpHead">Enter any camera name to view </p>
          <Form>
            <FormGroup controlId="VideoName" bsSize="large">
              <Input
                name="inputVideoUrl"
                id="inputVideoUrl"
                placeholder="Enter name"
                value={this.state.inputVideoUrl}
                onChange={this.handleValueChange}
              />
            </FormGroup>
            <FormGroup>
              <Button type="button" onClick={this.updatePlayerInfo}>
                Check Video
              </Button>
              <br/>
              <pre>

              </pre>
              <FormGroup controlId="email" bsSize="large">
                <FormControl
                  autoFocus
                  placeholder="URL"
                  ref = {c => this.usercredentials = c}
                />
              </FormGroup>

            <Button type="button" onClick={this.CheckLiveFootage}>
              Check Footage
            </Button>
          </FormGroup>
        </Form>
            <br/>
          </form>
        </div>
        </div>
        </section>

        <section>
        <div className="LiveFeedDiv">
        <iframe className = "LiveFeed" ref = {c => this.liveFeedPlayer = c} src=""></iframe>
        </div>
        </section>
      </div>
    );
  }
}
export default CameraFeed;
