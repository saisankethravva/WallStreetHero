import React from "react";
import "./topbar.css";
import {Settings} from "@material-ui/icons";
import Avatar from '@material-ui/core/Avatar';
import Searchbar from '../search_bar/SearchBar.jsx'
import { Link } from 'react-router-dom'

export default function topbar() {
  function logout() {
    localStorage.clear();
    window.location.href = '/';
}
  return (
    <div className="topbar">
      <div className="topbarWrapper">
        <div className="topLeft">
          <div className="logo">Wall Street Hero</div>
        </div>
        <div className="topRight">
          <div className="searchbar">
            <Searchbar />
          </div>
            <div className="topbarIconContainer">
              <button className="logoutButton" href="#" onClick={logout}>Logout</button>
            </div>
            <Avatar>WH</Avatar>
          </div>
        </div>
      </div>
  );
}


