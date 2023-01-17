import * as React from "react";
import { DataGrid } from "@mui/x-data-grid";
import "./gainers.css";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import RemoveRedEyeIcon from "@mui/icons-material/RemoveRedEye";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { render } from "react-dom";
import { styled } from "@mui/material/styles";
import PropTypes from "prop-types";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import Typography from "@mui/material/Typography";
import FeaturedInfo from "../featuredInfo/FeaturedInfo";

function Gainers() {
  const [open, setOpen] = React.useState(false);
  const handleClickOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  const BootstrapDialog = styled(Dialog)(({ theme }) => ({
    "& .MuiDialogContent-root": {
      padding: theme.spacing(2),
    },
    "& .MuiDialogActions-root": {
      padding: theme.spacing(1),
    },
  }));

  const BootstrapDialogTitle = (props) => {
    const { children, onClose, ...other } = props;

    return (
      <DialogTitle sx={{ m: 0, p: 2 }} {...other}>
        {children}
        {onClose ? (
          <IconButton
            aria-label="close"
            onClick={onClose}
            sx={{
              position: "absolute",
              right: 8,
              top: 8,
              color: (theme) => theme.palette.grey[500],
            }}
          >
            <CloseIcon />
          </IconButton>
        ) : null}
      </DialogTitle>
    );
  };

  const handleAdd = (id) => {
    //Add logic goes here;
  };

  const columns = [
    { field: "id", headerName: "ID", width: 90 },
    { field: "Name", headerName: "Name", width: 130 },
    { field: "Price", headerName: "Price", type: "number", width: 130 },
    {
      field: "view",
      headerName: "View",
      width: 130,
      renderCell: ({ children }) => {
        // console.log(children)
        return (
          <div>
            <RemoveRedEyeIcon
              className="Viewicon"
              onClick={handleClickOpen}
            />
            <BootstrapDialog
              onClose={handleClose}
              aria-labelledby="customized-dialog-title"
              open={open}
            >
              <BootstrapDialogTitle
                id="customized-dialog-title"
                onClose={handleClose}>
                Modal title
              </BootstrapDialogTitle>
              <DialogContent dividers><FeaturedInfo/></DialogContent>
            </BootstrapDialog>
          </div>
        );
      },
    },
    {
      field: "add",
      headerName: "Add",
      width: 130,
      renderCell: (params) => {
        return (
          <>
            {/*<Link to={"/user/" + params.row.id}> */}
            {/* <button className="Add">Add</button> */}
            {/* </Link> */}
            <AddCircleIcon
              className="Addto"
              onClick={() => handleAdd(params.row.id)}
            />
          </>
        );
      },
    },
  ];

  const rows = [
    { id: 1, Name: "AMZ", Price: 35 },
    { id: 2, Name: "APPL", Price: 34 },
    { id: 3, Name: "GOOG", Price: 35 },
    { id: 4, Name: "FORD", Price: 35 },
    { id: 5, Name: "TLA", Price: 35 },
    { id: 6, Name: "MCD", Price: 35 },
    { id: 7, Name: "BGK", Price: 35 },
    { id: 8, Name: "GYH", Price: 35 },
    { id: 9, Name: "INFY", Price: 35 },
    { id: 10, Name: "TCS", Price: 35 },
  ];
  return (
    <div className="Tables">
      <div style={{ height: 400, width: "33%", padding: 20 }}>
        <span className="featuredTitle">Top Gainers</span>
        <DataGrid
          // title={<MyNewTitle variant="h6" text="Average Expense Ratio" />}
          rows={rows}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
        />
      </div>
      <div style={{ height: 400, width: "33%", padding: 20 }}>
        <span className="featuredTitle">Top Loser</span>
        <DataGrid
          // title={<MyNewTitle variant="h6" text="Average Expense Ratio" />}
          rows={rows}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
        />
      </div>
      <div style={{ height: 400, width: "33%", padding: 20 }}>
        <span className="featuredTitle">Trending</span>
        <DataGrid
          // title={<MyNewTitle variant="h6" text="Average Expense Ratio" />}
          rows={rows}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
        />
      </div>
    </div>
  );
}

export default Gainers;
