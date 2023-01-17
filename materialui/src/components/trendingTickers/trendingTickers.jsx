import * as React from 'react';
import "./trendingTickers.css";
import AddCircleIcon from '@mui/icons-material/AddCircle';
import axios from 'axios';
import { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

class TrendingTickers extends Component {
  constructor() {
    super();
  }
  state = {
    trendingTickersData: []
  }

  componentDidMount() {
    axios.get('/trending/tickers').then(response => {
      console.log(response.data);
      //this.setState({...this.state, trendingTickersData: response.data})
      this.setState({trendingTickersData: response.data})
    })
  }
  render() {
    console.log(this.state.trendingTickersData);
    let items = [...this.state.trendingTickersData];
    if (this.state.trendingTickersData.length > 0) {
      /* return (
        <div>
          <h1>Gainers!</h1>
          {items.map((item) => (
            <Table key={item._id}>
              <div className="container">
                <TableRow>Stock: {item.stock} - Change: {item.change}</TableRow>
              </div>
            </Table>
          ))}
        </div>
      ); */

      return (
        <div style={{ minheight: 350 , width: '33%', padding: 20 }}>
          <span className="featuredTitle" style={{textDecoration: 'underline'}}>Trending Tickers</span>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 130 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Symbol</TableCell>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Company</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {items.map((item) => (
                  <TableRow
                    key={item._id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row" style={{fontSize: '12px'}}>
                      {item.symbol}
                    </TableCell>
                    <TableCell style={{fontSize: '12px'}}>
                      {item.company}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      );


    } else {
      return <div>No Trending Tickers Data!</div>;
    }
  }
}

export default TrendingTickers;