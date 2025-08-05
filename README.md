# Bipedal WiFi-Controlled Robot (ESP8266 + Python)

A compact bipedal robot powered by **ESP8266 (Wemos D1 Mini)** and controlled via WiFi using **Python**.

## Features

- 📡 **WiFi Control (UDP)** — Operate the robot from any device running Linux/Python on the same network.
- 🐍 **Python API** — Easy-to-use control functions for motion and behavior.
- 🔌 **Simple Wiring** — Minimalistic setup using 4 servos.

## Project concept

🧠 Project Concept
The core idea behind this project is to offload all servo control to the ESP8266, while keeping the entire decision-making and logic layer in Python.

This architecture brings a few key benefits:

⚡ Fast development – You can modify and test your Python logic instantly, without reflashing the microcontroller.

🧠 Separation of concerns – The ESP8266 acts purely as a low-level actuator controller (“muscles”), while Python handles the higher-level behavior and intelligence (“brain”).

🔄 Flexible updates – All changes to walking patterns, movement sequences, or reactions can be done from the Python side.

Think of it as:
Wemos = Muscles, 
Python = Brain

## Hardware Setup

| Component   | Description                              |
|------------|------------------------------------------|
| Controller | Wemos D1 Mini (ESP8266)                  |
| Servos     | 2x Positional (LL, RL), 2x Continuous (LF, RF) |
| Power      | 5V                                       |

### Wiring Diagram

| Servo | ESP8266 Pin |
|-------|-------------|
| LL    | D1          |
| LF    | D2          |
| RL    | D5          |
| RF    | D6          |

## Installation

### 1. Flash ESP8266 Firmware

- Install [Arduino IDE](https://www.arduino.cc/en/software)
- Add **ESP8266 support** via the Boards Manager (search for "ESP8266")
- Open the sketch from this repo:  
  [OttoNinjaServoDriverESP](https://github.com/boryspimpek/OttoNinjaServoDriverESP)

#### Configure your WiFi credentials

Inside the firmware, set your WiFi name and password:

```cpp
const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";
```

- Upload the code to your Wemos D1 Mini

---

### 2. Python Control Script

Clone the Python control repository:

```bash
git clone https://github.com/boryspimpek/OttoNinjaServoDriver.git
cd OttoNinjaServoDriver
```

#### ✅ Recommended: Use a virtual environment

To avoid conflicts with other Python packages, it's recommended to use a virtual environment:

```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the environment:
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the web control interface:

```bash
python3 app.py
```

Open your browser and navigate to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## License

This project is open source.
