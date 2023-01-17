import LexChat from "react-lex-plus"
import React, { Component } from "react";
import './bot.css'
class Bot extends Component {
  render() {
    return (<LexChat
      botName="WallStreet"
      IdentityPoolId="us-east-1:a3b5fa16-8d8b-40a8-ae5d-66cad74f136e"
      placeholder="Placeholder text"
      backgroundColor="#FFFFFF"
      height="430px"
      region="us-east-1"
      headerText="WallStreet Chat Bot"
      headerStyle={{ backgroundColor: "#ABD5D9", fontSize: "30px" }}
      greeting={
        "Welcome to WallStreet. How can we help you today?"
      }
    />);
  }
}
export default Bot;