import * as React from 'react';
import "./marketHours.css"
import axios from 'axios';
import { Component } from 'react';

class MarketHours extends Component {
  constructor() {
    super();
  }
  state = {
    marketHoursData: []
  }

  componentDidMount() {
    axios.get('/get-market-hours').then(response => {
      console.log(response.data);
      this.setState({marketHoursData: response.data})
    })
  }
  render() {
    console.log(this.state.marketHoursData);
    let items = [...this.state.marketHoursData];
    if (this.state.marketHoursData.length > 0) {
      return (
        <div className="marketHoursBlock">
          {items.map((item) => {
            if(item.isMarketOpen == 'true') {
              return <p>The New York Stock Exchange is currently <span style={{color: 'green'}}>Open</span>! 
                It closes at {item.marketCloseHours}.</p>
            } else {
              return <p>The New York Stock Exchange is currently <span style={{color: 'red'}}>Closed</span>! 
                It opens at {item.marketOpenHours}.</p>
            }
          })}
        </div>
      );
    } else {
      return <div>No Market Hours Data!</div>;
    }
  }
}

export default MarketHours;