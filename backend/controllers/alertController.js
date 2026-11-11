// const Alert = require("../models/Alert");
// const sendSMS = require("../config/twilio");

// exports.createAlert = async (req, res) => {
//   try {
//     const alert = new Alert({
//       driverId: req.body.driverId,
//       message: req.body.message,
//       video: req.file.filename
//     });

//     await alert.save();

//     await sendSMS("🚨 Driver Drowsiness Detected!");

//     res.json({ msg: "Saved + SMS Sent" });
//   } catch (err) {
//     res.status(500).json(err);
//   }
// };







exports.createAlert = async (req, res) => {
  try {
    console.log("📥 API HIT");

    const alert = new Alert({
      driverId: req.body.driverId,
      message: req.body.message,
      video: req.file.filename
    });

    await alert.save();

    console.log("📦 Saved to DB");

    await sendSMS("🚨 Driver Drowsiness Detected!");

    console.log("📩 SMS Triggered");

    res.json({ msg: "Saved + SMS Sent" });

  } catch (err) {
    console.error(err);
    res.status(500).json(err);
  }
};