import React, { Component } from "react";
//import React from 'react'
// import data from "./data.json"
import axios from "axios";

class Homepage extends Component {
  constructor() {
    super();
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    // var data={
    //     "1": [
    //         "Resist buying U.S. stocks and Treasurys, Morgan Stanley advises. Here’s what their strategists recommend buying instead.",
    //         "https://www.marketwatch.com/story/resist-buying-u-s-stocks-and-treasurys-morgan-stanley-advises-heres-what-they-recommend-buying-instead-11636971805?siteid=yhoof2&yptr=yahoo"
    //     ],
    //     "2": [
    //         "Billionaire Ray Dalio Picks Up These 3 ‘Strong Buy’ Stocks",
    //         "https://finance.yahoo.com/news/billionaire-ray-dalio-picks-3-155810811.html"
    //     ],
    //     "3": [
    //         "Warren Buffett saw inflation coming early on — 8 tips to help you come out ahead",
    //         "https://finance.yahoo.com/news/warren-buffet-saw-inflation-coming-200000608.html"
    //     ],
    //     "4": [
    //         "2 Big Dividend Stocks Yielding 9%; Analysts Say ‘Buy’",
    //         "https://finance.yahoo.com/news/2-big-dividend-stocks-yielding-010909661.html"
    //     ],
    //     "5": [
    //         "Cathie Wood strongly disputes Jack Dorsey’s ‘hyperinflation’ warning, but they agree on one asset class — in any market environment",
    //         "https://finance.yahoo.com/news/cathie-wood-strongly-disputes-jack-140700556.html"
    //     ]
    // }
    axios
      .get("/news")
      .then((res) => {
        console.log(res.data);
        // data: res.data,
        var arr = [];
        for (let [key, val] of Object.entries(res.data)) {
          console.log("key-->", key, val);
          arr.push({ key: val });
        }
        console.log("Arr", arr);
        this.setState({ data: arr });

      })



  }

  render() {
    console.log(this.state.data);
    if (this.state.data.length > 0) {
      return (
        <div>
          <h2> Welcome </h2>
          <ul>
            {this.state.data.map(function (news, index) {
              return (
                <div key={index}>
                  <h2> Welcome </h2>
                  <p>{news.key}</p>
                </div>
              );
            })}
          </ul>
        </div>
      );
    } else {
      return <div>No data</div>;
    }
  }
}

export default Homepage;
