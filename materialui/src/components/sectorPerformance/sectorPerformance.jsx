import * as React from 'react';
import "./sectorPerformance.css";
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
import { ArrowDownward } from "@material-ui/icons";

class SectorPerformance extends Component {
  constructor() {
    super();
  }
  state = {
    sectorPerformanceData: []
  }

  componentDidMount() {
    axios.get('/get-sector-performance').then(response => {
      console.log(response.data);
      this.setState({sectorPerformanceData: response.data})
    })
  }
  render() {
    console.log(this.state.sectorPerformanceData);
    let items = [...this.state.sectorPerformanceData];
    if (this.state.sectorPerformanceData.length > 0) {
      return (
        <div style={{ height: 350, width: '33%', padding: 20 }}>
          <span className="featuredTitle">Sector Performance</span>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 130 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell style={{fontWeight: 'bold', fontSize: '18px'}}>Sector</TableCell>
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
                      {item.sector}
                    </TableCell>
                    <TableCell style={{color: item.change[0] > '-' ? "green" : "red", fontSize: '12px'}}>
                      {item.change}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      );


    } else {
      return <div>No Sector Performance Data!</div>;
    }
  }
}

export default SectorPerformance;