/**
=========================================================
* Soft UI Dashboard React - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/soft-ui-dashboard-material-ui
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// @mui material components
import Card from "@mui/material/Card";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";

// Soft UI Dashboard React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

// Custom styles for the Tables
import styles from "layouts/tables/styles";

import SuiButton from "components/SuiButton";
import { useState } from 'react';
import ImportPopup from "./components/ImportPopup";
import FilterSortTable from "../../components/FilterSortTable"
import Table from "./components/Table";

function Instruments() {
  const classes = styles();
  const [open, setOpen] = useState(false);
  const [insertedRows, setInsertedRows] = useState([]);

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  function getColumns() {
    if (insertedRows.length === 0) return [];
    else return Object.keys(insertedRows[0])
      .filter(columnName => columnName != "_id")
      .map((columnName) => {
        return { id: columnName, label: columnName }
      })
  }

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <Table></Table>
    </DashboardLayout>
  );
}

export default Instruments;
