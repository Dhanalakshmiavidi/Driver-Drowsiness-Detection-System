const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const alertRoutes = require("./routes/alertRoutes");

const app = express();

app.use(cors());
app.use(express.json());
app.use("/uploads", express.static("uploads"));

mongoose.connect("mongodb://127.0.0.1:27017/drowsiness");

app.use("/api/alerts", alertRoutes);

app.listen(5000, () => console.log("Server running on 5000"));