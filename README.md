# Smart Attendance Marking System(Anti-spoof)

## 📌 Overview
The Smart Attendance Marking System is an AI-powered attendance solution designed to automate and secure classroom attendance using facial recognition and anti-spoofing mechanisms.

This project was initially developed to address real-world attendance inefficiencies and has evolved into a scalable product-oriented solution.

---

## 👥 Team Project

> ⚠️ **Note:** This is a collaborative team project developed by undergraduate engineering students as part of research, innovation, and product development efforts.

---

## 🚀 Problem Statement
Traditional attendance systems:
- Are time-consuming
- Allow proxy attendance
- Lack spoof detection
- Depend heavily on manual verification

Our system eliminates these issues through AI-based identification and hardware-level validation.

---

## 🧠 Key Features

- Face Recognition-based Identification
- Dual Camera Spoof Detection (IR + NoIR)
- Real-time Processing
- Server-based Face Matching
- Offline LAN Communication (Raw TCP Protocol)
- Attendance Logging and Database Storage
- Scalable Architecture (PoC → MVP → Pilot → Product)

---

## 🏗️ System Architecture

### Hardware:
- Raspberry Pi (initial prototype)
- Compute Module 4 (current development)
- IR Cut Camera
- NoIR Camera with IR LED
- Ethernet Communication

### Software:
- Python
- OpenCV
- Face Recognition Models
- TCP Socket Programming
- Backend Server for Processing

---

## 🔐 Anti-Spoofing Approach
To prevent photo-based or screen-based spoofing attacks, the system uses:
- IR reflectance comparison
- Dual-camera validation
- Texture-based detection logic

Backup approach:
- Pseudo stereo vision using dual RGB cameras

---

## 📈 Project Journey
- Initial Raspberry Pi 4 standalone model failed during competition due to performance bottlenecks.
- Pivoted to server-side processing with Pi as capture node.
- Faced spoofing vulnerabilities and iterated multiple hardware configurations.
- Successfully pitched at university innovation platform.
- Patent filed and approved (2025).
- Currently transitioning into product-level development.

---
## 1. Clone the repository:

git clone https://github.com/your-repo-name.git

---

## 2. Install dependencies:

pip install -r requirements.txt

---

## 3. Configure camera and server IP in config file.

---

## 4. Run capture module:

python capture.py

---
## 5. Run server module:

python server.py

---

## 📊 Future Scope
- Cloud integration
- Web dashboard for attendance analytics
- Institutional ERP integration
- Edge AI optimization
- Large-scale deployment testing

---

## 📜 License
This project is currently under development. Usage, distribution, or replication without permission is restricted.

---

## 🤝 Contributions
This is an internal team project. External contributions are currently not open.

---

### ⭐ Acknowledgment
Developed with the vision of creating reliable, secure, and intelligent automation systems for real-world institutional challenges.
