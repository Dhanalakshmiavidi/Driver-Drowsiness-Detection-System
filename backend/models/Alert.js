const mongoose = require("mongoose");

const alertSchema = new mongoose.Schema({
  driverId: String,
  message: String,
  video: String,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model("Alert", alertSchema);