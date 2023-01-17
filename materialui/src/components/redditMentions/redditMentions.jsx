import * as React from 'react';
import "./redditMentions.css";
import axios from 'axios';
import { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { styled } from "@mui/material/styles";

class RedditMentions extends Component {
  constructor() {
    super();
  }
  state = {
    redditMentionsData: []
  }

  componentDidMount() {
    axios.get('/get-reddit-mentions').then(response => {
      console.log(response.data);
      this.setState({redditMentionsData: response.data})
    })
  }
  render() {
    console.log(this.state.redditMentionsData);
    let items = [...this.state.redditMentionsData];
    if (this.state.redditMentionsData.length > 0) {
      return (
        <div style={{ height: 350, width: '33%', padding: 20 }}>
          <span className="featuredTitle">Stock Mentions on Reddit</span>
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
      return <div>No Reddit Mentions Data!</div>;
    }
  }
}

export default RedditMentions;