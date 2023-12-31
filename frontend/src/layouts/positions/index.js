// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Soft UI Dashboard React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import MiniStatisticsCard from "examples/Cards/StatisticsCards/MiniStatisticsCard";
import ReportsBarChart from "examples/Charts/BarCharts/ReportsBarChart";
import GradientLineChart from "examples/Charts/LineCharts/GradientLineChart";

// Soft UI Dashboard React base styles
import typography from "assets/theme/base/typography";

// Dashboard layout components
import BuildByDevelopers from "layouts/dashboard/components/BuildByDevelopers";
import WorkWithTheRockets from "layouts/dashboard/components/WorkWithTheRockets";
import Projects from "layouts/dashboard/components/Projects";
import OrderOverview from "layouts/dashboard/components/OrderOverview";

// Data
import reportsBarChartData from "layouts/dashboard/data/reportsBarChartData";
import gradientLineChartData from "layouts/dashboard/data/gradientLineChartData";

import Table from "../instruments/components/Table"

const data = [
  { fundId: 1, fundName: "Applebead" },
  { fundId: 2, fundName: "Belaware" },
  { fundId: 3, fundName: "Fund Whitestone" },
  { fundId: 4, fundName: "Leeder" },
  { fundId: 5, fundName: "Magnum" },
  { fundId: 6, fundName: "Wallington" },
  { fundId: 7, fundName: "Gohen" },
  { fundId: 8, fundName: "Catalysm" },
  { fundId: 9, fundName: "Trustmind" },
  { fundId: 10, fundName: "Virtous" }
]

function Positions() {
  const { size } = typography;
  const { chart, items } = reportsBarChartData;

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <Table data={data} />
    </DashboardLayout>
  );
}

export default Positions;
