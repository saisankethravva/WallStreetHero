import React, { Component } from 'react';
import "./news.css";
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

class News extends Component {
  constructor() {
    super();
  }
  state = {
    newsData: []
  }

  componentDidMount() {
    axios.get('/news').then(response => {
      console.log(response.data);
      this.setState({newsData: response.data})
    })
  }
  render() {
    console.log(this.state.newsData);
    let items = [...this.state.newsData];
    if (this.state.newsData.length > 0) {
      return (
        // <div style={{ height: 500, width: '100%', padding: 20 }}>
        <div style={{width: '100%', padding: 20 }}>
          <span className="featuredTitle">News</span>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 130 }} aria-label="simple table">
              <TableHead>
              </TableHead>
              <TableBody>
                {items.map((item) => (
                  <TableRow
                    key={item._id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="a" href={item.url} scope="row" style={{fontSize: '14px'}}>
                      {item.title}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      );
    } else {
      return <div><h3>No News Data!</h3></div>;
    }
  }
} 

export default News;