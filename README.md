# 🔌 Microcontroller Systems & IoT Development Portfolio

[![Python](https://img.shields.io/badge/Python-MicroPython-blue.svg)](https://micropython.org/)
[![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Pico-green.svg)](https://www.raspberrypi.org/products/raspberry-pi-pico/)
[![IoT](https://img.shields.io/badge/IoT-MQTT%20%7C%20HTTP%20%7C%20Cloud-orange.svg)](https://mqtt.org/)
[![License](https://img.shields.io/badge/License-Educational-yellow.svg)](https://opensource.org/licenses/MIT)

> **Professional portfolio demonstrating embedded systems and IoT development skills through practical microcontroller projects**

## 📋 Table of Contents

- [About This Project](#about-this-project)
- [Technical Skills Demonstrated](#technical-skills-demonstrated)
- [Project Highlights](#project-highlights)
- [Repository Structure](#repository-structure)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Portfolio Context](#portfolio-context)
- [Contact](#contact)

## 🎯 About This Project

This repository showcases my practical embedded systems and IoT development skills through comprehensive microcontroller projects completed during my **Certificate IV in Programming** at **Kangan Institute**. The coursework spans 15 weeks of hands-on learning, demonstrating progression from basic GPIO control to sophisticated IoT systems with real-time cloud connectivity.

### 📊 Project Statistics
- **📁 34 Python files** - Production-ready MicroPython implementations
- **📓 13 Jupyter notebooks** - Detailed project documentation and theory
- **🔌 6+ Hardware platforms** - Multi-sensor integration and control systems
- **☁️ 4 Communication protocols** - Wi-Fi, HTTP, MQTT, SPI/I2C
- **🏗️ 15 Weeks** - Progressive learning from basics to advanced IoT

### 🎓 Learning Outcomes Demonstrated
- **Embedded Programming**: MicroPython on Raspberry Pi Pico/Pico W
- **Hardware Integration**: Multi-sensor systems and real-time control
- **Network Programming**: Wi-Fi connectivity and cloud database integration  
- **IoT Protocols**: MQTT pub/sub messaging and HTTP REST APIs
- **System Architecture**: End-to-end IoT solutions with proper error handling
- **Professional Development**: Code organization, documentation, and testing

## 💻 Technical Skills Demonstrated

### Programming & Development
- **MicroPython** - Embedded programming for microcontrollers
- **Circuit Design** - Hardware interfacing and component integration  
- **Real-time Systems** - Sensor monitoring and control loops
- **Error Handling** - Robust exception management and debugging
- **Code Organization** - Modular programming and documentation

### Hardware Platforms & Components
- **Microcontrollers**: Raspberry Pi Pico, Raspberry Pi Pico W
- **Sensors**: DHT11 (temperature/humidity), PIR (motion), LDR (light)
- **Displays**: SSD1306 OLED (128x64, I2C communication)
- **Communication**: RFID-RC522 (NFC card reader), IR receivers
- **Control**: RGB LEDs, servo motors, buzzers, relay switches

### Network & IoT Protocols  
- **Wi-Fi Connectivity** - Wireless network configuration and management
- **HTTP/REST APIs** - GET/POST requests with JSON data handling
- **MQTT Protocol** - Pub/sub messaging with TLS security (HiveMQ Cloud)
- **Database Integration** - Supabase PostgreSQL via REST API
- **Real-time Communication** - Live sensor data streaming and remote control

### Development Tools & Environment
- **Thonny IDE** - MicroPython development and debugging
- **Serial Communication** - UART debugging and data monitoring  
- **Version Control** - Git repository management
- **Documentation** - Jupyter notebooks with technical explanations
- **Testing** - Hardware validation and system integration

## 🚀 Project Highlights

### 🌡️ Smart Greenhouse Environmental Monitor
**Week 11** | *Advanced sensor integration with OLED display*
```python
# Real-time temperature/humidity monitoring with visual feedback
DHT.measure()
temperature = DHT.temperature()
humidity = DHT.humidity()
oled.text(f'Temp: {temperature}C', 0, 0)
oled.text(f'Humidity: {humidity}%', 0, 10)
```
- **Skills**: DHT11 sensor integration, I2C communication, real-time display updates
- **Hardware**: Raspberry Pi Pico, DHT11, SSD1306 OLED display
- **Application**: Agricultural monitoring system with environmental controls

### 🔒 RFID Access Control System  
**Week 13** | *Database-integrated authentication system*
```python
# RFID card authentication with cloud database verification
card = int.from_bytes(bytes(uid), "little", False)
response = urequests.get(f"{supabase_url}?card_id=eq.{card}", headers=headers)
if response.json():
    led_green.on()  # Access granted
```
- **Skills**: RFID/NFC communication, HTTP API integration, authentication logic
- **Hardware**: Raspberry Pi Pico W, MFRC522 RFID reader, RGB LEDs
- **Application**: Secure access control with cloud-based user management

### 📡 IoT Weather Station with MQTT
**Week 15** | *Real-time data streaming to cloud services*
```python
# MQTT publish/subscribe with TLS encryption
client.publish(b"greenhouse/sensor1/data", 
               json.dumps({"temp": temperature, "humidity": humidity}))
```
- **Skills**: MQTT protocol, TLS security, JSON data formatting, pub/sub messaging
- **Hardware**: Raspberry Pi Pico W, DHT11 sensor, Wi-Fi connectivity  
- **Application**: Industrial IoT monitoring with real-time alerts

### 🏠 Smart Home Automation Hub
**Week 10-12** | *Multi-sensor control system*
- **Motion-activated security alarm** with PIR sensors and remote notifications
- **Ambient lighting control** with LDR sensors and PWM dimming
- **IR remote control system** for wireless device management
- **Energy-saving hallway lighting** with automatic on/off scheduling

### 🎮 Interactive Memory Game
**Week 7** | *Assessment project demonstrating programming fundamentals*
- LED sequence memory challenge with increasing difficulty
- User input validation and score tracking
- Real-time feedback and game state management

## 📈 Learning Progression

| Week Range | Focus Area | Key Technologies | Complexity |
|------------|------------|------------------|------------|
| **1-7** | Fundamentals | GPIO, PWM, Basic sensors | 🟢 Beginner |
| **8-10** | Advanced Control | Multi-sensor, Timing, Interrupts | 🟡 Intermediate |  
| **11-12** | Communication | I2C, SPI, UART protocols | 🟠 Advanced |
| **13-14** | IoT Integration | Wi-Fi, HTTP APIs, Cloud databases | 🔴 Professional |
| **15** | Real-time Systems | MQTT, TLS security, Pub/Sub | 🟣 Expert |

## 📁 Repository Structure

```
📦 kangan-microcontrollers-repo/
├── 📁 week_01-week_15/           # Weekly project modules
│   ├── 📓 Week_XX_Tasks.ipynb   # Project documentation & theory
│   ├── 🐍 Task_01-project.py    # Implementation files
│   └── 🐍 setup_files.py        # Hardware configuration
├── 📁 tests/                    # Hardware validation scripts
│   ├── blink.py                 # Basic LED functionality test  
│   ├── test.py                  # Component testing utilities
│   └── os_test.py               # System verification
├── 📋 CLAUDE.md                 # Development environment guide
└── 📖 README.md                 # This portfolio documentation
```

### 🗂️ Navigation Guide

- **Early Learning (Weeks 1-7)**: Foundational concepts and basic projects
- **Skill Building (Weeks 8-12)**: Advanced sensor integration and communication protocols  
- **Professional Projects (Weeks 13-15)**: Cloud-integrated IoT systems and real-time communication
- **Tests Folder**: Hardware validation and debugging utilities

### 📝 File Naming Conventions

- `Week_XX_Tasks.ipynb` - Comprehensive project documentation with theory and examples
- `Task_XX-descriptive_name.py` - Production implementations of specific assignments
- `setup_files.py` - Hardware initialization and configuration helpers

## 🛠️ Technologies Used

### Core Technologies
- ![Python](https://img.shields.io/badge/MicroPython-3.4-blue?logo=python) **MicroPython 3.4+** - Embedded programming language
- ![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_Pico-green?logo=raspberrypi) **Raspberry Pi Pico/Pico W** - ARM Cortex-M0+ microcontroller
- ![Thonny](https://img.shields.io/badge/IDE-Thonny-orange) **Thonny IDE** - MicroPython development environment

### Communication Protocols
- **I2C** - Inter-Integrated Circuit for sensor communication
- **SPI** - Serial Peripheral Interface for high-speed data transfer  
- **UART** - Universal Asynchronous Receiver/Transmitter for serial communication
- **Wi-Fi 802.11** - Wireless networking (Pico W)

### IoT & Cloud Services
- **HTTP/HTTPS** - RESTful API communication
- **MQTT 3.1.1** - Lightweight messaging protocol with TLS 1.2
- **JSON** - Data interchange format
- **Supabase** - PostgreSQL cloud database with REST API

### Hardware Libraries
```python
# Key MicroPython libraries used
import machine          # GPIO, PWM, I2C, SPI control
import network          # Wi-Fi connectivity  
import urequests        # HTTP client for REST APIs
import umqtt.simple     # MQTT client implementation
import dht              # DHT11/DHT22 sensor interface
import ssd1306          # OLED display driver
```

## 🚀 Getting Started

### Prerequisites
- **Hardware**: Raspberry Pi Pico or Pico W microcontroller
- **Software**: [Thonny IDE](https://thonny.org/) (recommended) or any MicroPython-compatible editor
- **Optional**: Breadboard, sensors, and components for specific projects

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/kangan-microcontrollers-repo.git
   cd kangan-microcontrollers-repo
   ```

2. **Set up your development environment**
   - Install [Thonny IDE](https://thonny.org/)
   - Connect your Raspberry Pi Pico via USB
   - Configure serial connection:
     - **Windows**: `%serialconnect to --port=COM3 --baud=115200`
     - **macOS**: `%serialconnect to --port=/dev/tty.SLAB_USBtoUART --baud=115200`

3. **Install required MicroPython libraries**
   ```python
   import mip
   mip.install("umqtt.simple")    # For MQTT projects
   mip.install("urequests")       # For HTTP API projects
   ```

4. **Start with basic tests**
   ```bash
   # Test basic functionality
   python tests/blink.py
   
   # Explore weekly projects
   jupyter notebook week_11/Week_11_Tasks.ipynb
   ```

### 🔧 Hardware Setup Examples

**Basic LED Control**
```python
from machine import Pin
import time

led = Pin(25, Pin.OUT)  # Built-in LED on Pico
led.toggle()            # Toggle LED state
```

**Sensor Reading (DHT11)**
```python
import dht
from machine import Pin

sensor = dht.DHT11(Pin(16))
sensor.measure()
temp = sensor.temperature()    # °C
humidity = sensor.humidity()   # %
```

### 📚 Recommended Learning Path
1. **Start with basics** - Week 1-7 projects (GPIO, LED control, basic sensors)
2. **Build complexity** - Week 8-12 (multi-sensor systems, communication protocols)  
3. **Add connectivity** - Week 13-15 (Wi-Fi, cloud integration, MQTT)
4. **Explore documentation** - Read Jupyter notebooks for theory and implementation details

## 🎯 Portfolio Context

### Professional Relevance
This repository demonstrates **practical embedded systems engineering skills** highly valued in today's IoT-driven technology landscape. The projects showcase:

- **Problem-solving abilities** through progressive complexity from basic sensors to cloud-integrated systems
- **Industry-relevant technologies** including MQTT, REST APIs, and real-time data processing  
- **Professional development practices** with proper code organization, documentation, and version control
- **Hardware-software integration** skills essential for IoT and embedded systems roles

### Career Applications
The skills demonstrated here directly apply to roles in:
- **IoT Development** - Connected device programming and cloud integration
- **Embedded Systems Engineering** - Microcontroller programming and hardware interface design
- **Industrial Automation** - Sensor networks and control system implementation  
- **Smart Building Technology** - Environmental monitoring and automation systems
- **Agricultural Technology** - Precision farming and monitoring solutions

### Continuous Learning
This coursework represents **foundational expertise** in embedded systems, with clear pathways for advancement into:
- Advanced microcontroller platforms (ESP32, STM32)
- Industrial communication protocols (Modbus, CAN bus)
- Edge computing and machine learning on embedded devices
- Professional IoT development frameworks

---

## 📞 Contact

**Fraser Brown** - Programming Student & Embedded Systems Enthusiast

- 🔗 **LinkedIn**: [Connect with me](https://linkedin.com/in/your-profile)
- 📧 **Email**: your.email@example.com  
- 🐱 **GitHub**: [View more projects](https://github.com/YourUsername)
- 🎓 **Institution**: Kangan Institute - Certificate IV in Programming

---

### 📋 Repository Statistics
- **Created**: 2024
- **Language**: MicroPython (100%)
- **License**: Educational Use
- **Status**: Portfolio Project - Completed ✅

*This repository serves as a comprehensive portfolio demonstrating embedded systems and IoT development capabilities through practical, industry-relevant projects.*
