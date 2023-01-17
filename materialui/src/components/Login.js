import React, { Component } from "react";
import "../styles/login.css";
import "../styles/signup.css";
import axios from "axios";
import Home from "../pages/home/Home.jsx";
//import Profile from "./Profile";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      uname: "",
      pass: "",
      isLoggedIn: false,
      signUp: true,
      firstName: "",
      lastName: "",
      store: null,
      pass2: "",
    };
    this.handleSubmitLogin = this.handleSubmitLogin.bind(this);
    this.handleSubmitSignUp = this.handleSubmitSignUp.bind(this);
    this.handleUName = this.handleUName.bind(this);
    this.handlePass = this.handlePass.bind(this);
    this.handleUName2 = this.handleUName2.bind(this);
    this.handlePass2 = this.handlePass2.bind(this);
    this.handleDob = this.handleDob.bind(this);
    this.handlePhonenumber = this.handlePhonenumber.bind(this);
    this.handleSignUp = this.handleSignUp.bind(this);
    this.handleFN = this.handleFN.bind(this);
    this.handleLN = this.handleLN.bind(this);
  }

  handleUName(e) {
    this.setState(
      {
        uname: e.target.value,
      },
      () => console.log(this.state.uname)
    );
  }

  handlePass(e) {
    this.setState({
      pass: e.target.value,
    });
  }

  handleUName2(e) {
    this.setState(
      {
        uname: e.target.value,
      },
      () => console.log(this.state.uname)
    );
  }

  handlePass2(e) {
    this.setState({
      pass: e.target.value,
    },
    // () => console.log(this.state.pass)
  );
}

  handlePhonenumber(e) {
    this.setState({
      phonenumber: e.target.value,
    },
      () => console.log(this.state.phonenumber)
    );
  }

  handleDob(e) {
    this.setState({
      dob: e.target.value,
    });
  }

  handleFN(e) {
    this.setState({
      firstName: e.target.value,
    });
  }

  handleLN(e) {
    this.setState({
      lastName: e.target.value,
    });
  }

  handleSignUp(e) {
    this.setState({
      signUp: !this.state.signUp,
    });
  }

  async handleSubmitLogin() {
    let user = {
      username: this.state.uname,
      password: this.state.pass,
    };
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user),
    };
    fetch("/login", requestOptions)
    .then((response)=>{
      response.json().then((result)=>{
      console.log("result", result);
      localStorage.setItem('isLoggedIn', JSON.stringify({
        isLoggedIn: true,
        token:result.access_token
      }))
      this.setState({
         isLoggedIn: true,
      })
    })
  })
  }

  async handleSubmitSignUp() {
    let user2 = {
      email: this.state.uname,
      password: this.state.pass,
      first_name: this.state.firstName,
      last_name: this.state.lastName,
      phone_number: this.state.phonenumber,
    };
    console.log(user2);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(user2),
    };
    fetch("/user", requestOptions)
    .then((response)=>{
      response.json().then((result)=>{
      console.log("result", result);
      localStorage.setItem('isLoggedIn', JSON.stringify({
        isLoggedIn: true,
        token:result.access_token
      }))
      this.setState({
         isLoggedIn: true,
      })
    })
  })
}

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    const isSignUpClicked = this.state.signUp;

    return (
      <div>
        {isLoggedIn ? (
          <Home />
        ) : (
          <div>
            {isSignUpClicked ? (
              <div className="login">
                  <h2>Wall Street Hero</h2>
                  <div className="user-box">
                  <input
                    type="text"
                    name="uname"
                    id="uname"
                    // placeholder="Please Enter Username"
                    onChange={this.handleUName}
                    required />
                    <label>Username</label>
                  </div>
                  <br/>

                  <div className="user-box">
                  <input
                    type="password"
                    name="pass"
                    id="pass"
                    // placeholder="Please Enter Password"
                    onChange={this.handlePass}
                    required />
                    <label>Password</label>
                    </div>
                    <br />

                    <div className="button">
                    <input
                    type="submit"
                    id="login"
                    name="login"
                    value="Login"
                    onClick={this.handleSubmitLogin} />

                    <br/>
                    <br/>

                    <input
                    type="submit"
                    id="login"
                    name="login"
                    value="Signup"
                    onClick={this.handleSignUp} />
                    {/* <label>Signup</label> */}

                    <br />
                    <br />

                    <input
                    type="submit"
                    id="login"
                    name="login"
                    value="Google"
                    onClick={this.handleSignUp} />
                  </div>
                </div>
            ) : (
              <div className="signup">
                <h2>Sign up</h2>
                {/* <p> First Name </p> */}
                <div className="user-box">
                <input
                  type="text"
                  name="firstname"
                  // placeholder="Please enter your First Name"
                  onChange={this.handleFN}
                  required
                />
                  <label>First Name</label>
                </div>
                {/* <p> Last Name </p> */}
                <div className="user-box">
                <input
                  type="text"
                  name="lastname"
                  // placeholder="Please enter your Last Name"
                  onChange={this.handleLN}
                  required
                />
                    <label>Last Name</label>

                </div>

                {/* <p> Username </p> */}
                <div className="user-box">
                <input
                  type="text"
                  name="uname2"
                  id="uname2"
                  // placeholder="Please enter Username"
                  onChange={this.handleUName2}
                  required
                />
                    <label>Username</label>

                </div>
                {/* <p> Password</p> */}
                <div className="user-box">
                <input
                  type="password"
                  name="pass2"
                  id="pass2"
                  onChange={this.handlePass2}
                  required
                />
                    <label>Password</label>
                </div>

                <div className="user-box">
                    <input
                      type="text"
                      name="phonenumber"
                      id="phonenumber"
                      onChange={this.handlePhonenumber}
                      required
                    />
                      <label>Phone Number</label>
                </div>
                 {/* <p> Date of Birth </p> */}
                 <div className="user-box">
                   <div className="dob">
                    <input
                      type="date"
                      name="dob"
                      id="dob"
                      // placeholder="Please enter DOB"
                      onChange={this.handleDob}
                      required
                    />
                    </div>
                </div>
                <br />
                <div className="button1">
                <input
                  type="submit"
                  id="signup"
                  name="signup"
                  value="Sign Up"
                  onClick={this.handleSubmitSignUp}
                />
                <br />
                <br/>
                <input
                  type="submit"
                  id="signup"
                  name="signup"
                  value="Login"
                  onClick={this.handleSignUp}
                />
                <br />
                {/* <button onClick={this.handleSignUp}>Login</button>  */}
                <br />
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    );
  }
}

export default Login;
