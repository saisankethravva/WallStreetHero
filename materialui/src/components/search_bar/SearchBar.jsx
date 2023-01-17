// import React, { Component } from "react";
import * as React from "react";
import { Component } from "react";
// import "./styles.css";
import SearchBar from "material-ui-search-bar";
import styled from "styled-components";
import SearchIcon from "@mui/icons-material/Search";
import ReactSearchBox from "react-search-box";
import Button from '@mui/material/Button';


export const StyledSearchBar = styled(SearchBar)`
  margin: 0 auto;
  width: 70%;
  max-width: 800px;
  borderbottomcolor: "transparent";
  bordertopcolor: "transparent";
`;

class Searchbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
      apidata: null,
    };
    // this.handleSearch = this.handleSearch.bind(this);
    // this.handleRequestSearch = this.handleRequestSearch.bind(this);
  }

  // handleSearch(e) {
  //   this.setState(
  //     {
  //       search: e.target.value,
  //     },
  //     () => console.log(this.state.search)
  //   );
  // }

  async handleRequestSearch() {
    let param = {
      search: this.state.value,
    };
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(param),
    };
    fetch("/get-stock-rating", requestOptions).then((response) => {
      console.log(param);
      console.log(response.data);
      //this.setState({...this.state, trendingTickersData: response.data})
      this.setState({ apidata: response.data });
    });
  }

  render() {
    // return (
    //   <div className="App">
    //          <SearchBar
    //        onChange={this.handleSearch}
    //        onRequestSearch={() => this.handleRequestSearch}
    //       />
    //   </div>
    // );

    return (
      <>
      
      <SearchBar
        value={this.state.value}
        onChange={(newValue) => this.setState({ value: newValue })}
        // onRequestSearch={() => this.handleRequestSearch(this.state.value)}
       />
       <Button variant="outlined"
      onClick={() => this.handleRequestSearch(this.state.value)}>
      Search
      </Button>

      </>
      // <>
      //   <ReactSearchBox
      //     placeholder="Placeholder"
      //     value="Doe"
      //     data={this.data}
      //     callback={(record) => console.log(record)}
      //   />
      //   <SearchIcon
      //     className="Addto"
      //     onClick={() => this.handleRequestSearch(this.state.value)}
      //   />
      // </>
    );
  }
}

export default Searchbar;

{
  /* console.log("onChange")} */
}
{
  /* onRequestSearch={() => console.log("onRequestSearch")} */
}
