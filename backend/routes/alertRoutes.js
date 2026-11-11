const express = require("express");
const router = express.Router();
const multer = require("multer");
const { createAlert } = require("../controllers/alertController");

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(null, Date.now() + ".avi");
  }
});

const upload = multer({ storage });

router.post("/upload", upload.single("video"), createAlert);

module.exports = router;