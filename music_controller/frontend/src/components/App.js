import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from "./CreateRoomPage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <fgfdgdsfgfd/>
        <HomePage/>
        <RoomJoinPage/>
        <CreateRoomPage/>
        return <h1>{this.props.name}</h1>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App  name="DJANGO" />, appDiv);