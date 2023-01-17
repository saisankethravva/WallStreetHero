import React, { Component } from "react";
import axios from "axios";
import "../styles/profile.css";
import Table from "react-bootstrap/Table";
import "moment-timezone";
import moment from "moment";
import ReactLoading from "react-loading";
import { saveAs } from "file-saver";

class Profile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null,
      timeZone: "UTC",
      selectedFile: null,
      uploaded: false,
      deleted: false,
    };
  }

  componentDidMount() {
    this.getFiles();
    this.setState({
      timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    });
  }

  getFiles() {
    console.log("files callled");
    let userName = this.props.uname;
    axios
      .get("http://13.57.23.139:5000/getContent/" + userName)
      .then((res) => {
        console.log(res.data);
        this.setState({
          data: res.data,
        });
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  }

  async onFileDownload(fileName) {
      console.log("files download called");
      let userName = this.props.uname;
      let file;
      if(userName == "allusers"){
      file =  fileName}
      else
      {
        file = userName + "/" + fileName
      }
      await axios
        .get("http://13.57.23.139:5000/downloadFile/"+ file)
        .then((res) => {
          console.log(res.data);
          saveAs("https://" + res.data, fileName);
        })
        .catch((error) => {
          console.error("There was an error in download!", error);
        });
    }

     async onFileDelete(fileName) {
      console.log("Delete File");
      let userName = this.props.uname;
      let file;
      if(userName == "allusers"){
      file =  fileName}
      else
      {
        file = userName + "/" + fileName
      }
         await axios
         // console.log("filename =",fileName)
        .get("http://13.57.23.139:5000/deleteFile/" + file)
        .then((res) => {
          console.log(res);
            this.getFiles();
          }
        )
        .catch((error) => {
          console.error("There was an error!, In the deletefile opp", error);
        });
      };


  onFileChange = (event) => {
    // Update the state
    this.setState({ selectedFile: event.target.files[0] });
  };

  onFileUpload = () => {
    // Create an object of formData
    const formData = new FormData();

    // Update the formData object
    formData.append(
      "myFile",
      this.state.selectedFile,
      this.state.selectedFile.name
    );

    // Details of the uploaded file
    console.log(this.state.selectedFile);

    // Request made to the backend api
    // Send formData object
    let userName = this.props.uname;
    axios
      .post("http://13.57.23.139:5000/uploadFile/" + userName, formData)
      .then((res) => {
        console.log(res);
        if (res.data.success) {
          this.setState({
            uploaded: true,
          });
          this.getFiles();
        }
      })
      .catch((error) => {
        console.error("There was an error!", error);
      });
  };

  render() {
    function formatBytes(bytes, decimals = 2) {
      if (bytes === 0) return "0 Bytes";

      const k = 1024;
      const dm = decimals < 0 ? 0 : decimals;
      const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];

      const i = Math.floor(Math.log(bytes) / Math.log(k));

      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
    }

    return (
      <>
        <h2 className="header1">{this.props.uname}'s files</h2>
        {!this.state.data ? (
          <ReactLoading type={"spin"} color="black" />
        ) : (
          <Table striped bordered hover className="tableDesign">
            <thead>
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
                <th>Download</th>
                <th>Delete</th>
              </tr>
            </thead>
            <tbody>
              {this.state.data.map((k, i) => (
                <tr key={k.ETag}>
                  <td>{i + 1}</td>
                  <td>{k.Key}</td>
                  <td>
                    {moment(k.LastModified).tz(this.state.timeZone).calendar()}
                  </td>
                  <td>{formatBytes(k.Size)}</td><td>
                    <button className="selectButton" onClick={() => this.onFileDownload(k.Key)}>
                      Download
                    </button>
                  </td>
                  <td><button className="selectButton" onClick={() => this.onFileDelete(k.Key)}>Delete</button></td>
                  {this.state.deleted ? <p> Deleted successfully !</p> : null}
                </tr>
              ))}
            </tbody>
          </Table>
        )}
        <br />
        <div>
          <input className="selectButton1" type="file" onChange={this.onFileChange} />
          <button className="selectButton" onClick={this.onFileUpload}>Upload!</button>
          {this.state.uploaded ? <p> Uploaded successfully !</p> : null}
        </div>
      </>
    );
  }
}

export default Profile;
