import './App.css';
import Topbar from './components/topbar/topbar';
import Home from "./pages/home/Home";
// import React from 'react';
import News from './components/news/news';
import React, { Component } from "react";
import Login from "./components/Login";
// import SignUp from "./components/Signup";
import "bootstrap/dist/css/bootstrap.min.css";
import Bot from './components/bot/Bot';


import axios from "axios";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      newUser: true,
    };
  }

  render() {
  return (
    <div>
        <Bot />
    <Router>
      <Routes>
        {/* <Route path="/login"> */}.
      
        <Route path="/" caseSensitive={false} element={<Login />} />
        <Route path="/login" caseSensitive={false} element={<Login />} />
        <Route path="/home" caseSensitive={false} element={<Home />} />
        {/* <ProtectedRoute path="/home">
          <Home />
        </ProtectedRoute> */}
        {/* <Route exact path="/">
          <Navigate exact from="/" to="home" />
        </Route>
        <Route path="*">
          <Navigate from="/" to="home" />
        </Route> */}
      </Routes>
    </Router>
    </div>
  );
}
}

export default App;

  {/* // return (
  // return <>{this.state.newUser ? <Login /> : <SignUp />}</>;
  // return <>{<Login />}</>;
  // <>
  // <Homepage/>
  // </>
//   // )
//   }
// function App() { */}
{/* //   return (
//     <div>
//         <Topbar />
//         <div className="container">

//           <Home />
//         </div>
//     </div>
//   );
// }

// export default App; */}
