import * as React from 'react';
import "./gainers.css"
import axios from 'axios';
import { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { ArrowUpward } from "@material-ui/icons";

class Gainers extends Component {
  constructor() {
    super();
  }
  state = {
    gainersData: []
  }

  componentDidMount() {
    axios.get('/get-gainers').then(response => {
      console.log(response.data);
      this.setState({gainersData: response.data})
    })
  }
  render() {
    console.log(this.state.gainersData);
    let items = [...this.state.gainersData];
    if (this.state.gainersData.length > 0) {
      return (
        <div style={{ height: 350, width: '33%', padding: 20 }}>
          <span className="featuredTitle">Top Gainers</span>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 130 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Stock</TableCell>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Price</TableCell>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Change</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {items.map((item) => (
                  <TableRow
                    key={item._id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row" style={{fontSize: '12px'}}>
                      {item.stock}
                    </TableCell>
                    <TableCell style={{fontSize: '12px'}}>
                      $ {item.price}
                    </TableCell>
                    <TableCell style={{color: "green", fontSize: '12px'}}>
                      +{item.changes} ({item.changePercent}%)
                      <span><ArrowUpward className="featuredIcon positive"/></span>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      );
    } else {
      return <div>No Top Gainers Data!</div>;
    }
  }
}

export default Gainers;