# Concussion Detection Sensor for Athlete Safety

**Using Technology and Faith to Protect God's Gift of Life**

---

## Table of Contents
1. [Introduction and Objective](#introduction-and-objective)  
2. [Materials](#materials)  
   - [Hardware](#hardware)  
   - [Software](#software)  
3. [Setup and Connections](#setup-and-connections)  
   - [Raspberry Pi <-> MPU-6050 Pinout](#raspberry-pi---mpu-6050-pinout)  
   - [Buzzer Pin Setup](#buzzer-pin-setup)  
   - [Additional Wiring Tips](#additional-wiring-tips)  
   - [Device Pinouts](#device-pinouts)  
4. [Software Installation](#software-installation)  
5. [Python Code for Delayed Logger](#python-code-for-delayed-logger)  
6. [Python Code for Live Logger](#python-code-for-live-logger)  
7. [How It Works](#how-it-works)  
8. [Catholic Values Integration](#catholic-values-integration)  
9. [Display Board and Presentation Script](#display-board-and-presentation-script)  
   - [Display Board Layout](#display-board-layout)  
   - [Presentation Script for JD](#presentation-script-for-jd)  
10. [Additional Resources](#additional-resources)  
11. [License](#license)

---

## Introduction and Objective
Concussions are a serious concern in sports. This project aims to design a **concussion detection sensor** prototype that can monitor impacts in sports and alert coaches to potential concussions. By using **historical data** to analyze trends, we can better understand when and how concussions occur and protect athletes more effectively.

This project integrates **Catholic values** of compassion, stewardship, and human dignity by emphasizing the responsibility to care for athletes’ well-being and by leveraging technology to safeguard the life that God has given.

---

## Materials

### Hardware
- Raspberry Pi 400 (or any compatible Raspberry Pi model)  
- MPU-6050 Accelerometer/Gyroscope Module  
- Buzzer (for audible alerts)  
- Breadboard and jumper wires  
- MicroSD card with Raspberry Pi OS  
- Helmet (for mounting the sensor)  
- Portable battery pack (to power the Raspberry Pi for portability)  
- Velcro or glue (for attaching the sensor to the helmet)  
- USB flash drive or cloud setup (to save historical data)

### Software
- Python libraries:
  - `smbus2`
  - `RPi.GPIO`
  - `matplotlib`
  - `pandas`
  - `datetime`

---

## Setup and Connections

### Raspberry Pi <-> MPU-6050 Pinout

| **Raspberry Pi Pin (Physical #)** | **BCM GPIO** | **MPU-6050 Pin** | **Description**                                                     |
|:---------------------------------:|:-----------:|:---------------:|---------------------------------------------------------------------|
| **Pin 1**                         | 3V3 Power   | **VCC**          | Power to the MPU-6050 (3.3V) <br> *Check if your module can accept 5V*  |
| **Pin 3**                         | GPIO2 (SDA) | **SDA**          | I2C Data Line                                                        |
| **Pin 5**                         | GPIO3 (SCL) | **SCL**          | I2C Clock Line                                                       |
| **Pin 6**                         | GND         | **GND**          | Ground reference                                                     |

> **Note**: Some MPU-6050 boards have onboard voltage regulators, allowing 5V input on VCC.  
> Always confirm the acceptable voltage input for your specific module.

#### Optional Pins
- **INT (Interrupt)** on the MPU-6050 can be connected to any free GPIO pin on the Raspberry Pi if you want to use interrupt-driven events (e.g., GPIO4, GPIO17). This is not required for basic polling or simple I2C reads.

### Buzzer Pin Setup
If you are using a buzzer for impact alerts, wire it as follows:

| **Raspberry Pi Pin (Physical #)** | **BCM GPIO** | **Buzzer Pin** | **Description**              |
|:---------------------------------:|:-----------:|:--------------:|------------------------------|
| **Pin 11**                        | GPIO17       | **+** (Buzzer) | Positive leg of the buzzer   |
| **Any GND** pin (e.g. Pin 6)      | GND          | **-** (Buzzer) | Ground leg of the buzzer     |

> **Note**: If your buzzer requires more current than the GPIO pin can safely supply, use a transistor driver circuit with an appropriate resistor rather than driving the buzzer directly from the GPIO.

### Additional Wiring Tips
1. **I2C Interface**: Make sure I2C is enabled on the Raspberry Pi (via `sudo raspi-config` -> *Interfacing Options* -> *I2C* -> *Enable*).  
2. **Pull-Up Resistors**: Many MPU-6050 breakout boards include pull-up resistors on SDA and SCL. If yours does not, you may need to add external pull-up resistors (typically 4.7kΩ) to 3.3V.  
3. **Voltage Levels**: If the MPU-6050 board lacks level shifting or regulators, use only 3.3V to avoid damaging the sensor.  
4. **Buzzer Requirements**: If you have a passive buzzer or one that draws more current than the GPIO can provide, use a transistor or MOSFET with a diode and appropriate resistor.


## Device Pinouts

| [<img src="rPi400Pinout-3a.png" alt="Pi 400 Pinout" title="Pi 400 Pinout" width="820px">](rPi400Pinout-3a.png) |
|:--------------------------------------------------------------------------------------------------------------:|
| **Pi 400 Pinout**                                                                                             |

#### Pi 400 Full 40-Pin GPIO Header

Below is the complete 40-pin layout for the Pi 400 (which matches the Raspberry Pi 4 pinout).  
Columns include **Physical Pin #**, **BCM GPIO** numbering, **Name/Function**, and a brief **Description**.

| **Physical Pin #** | **BCM GPIO** | **Name / Function** | **Description**                                                                       |
|:------------------:|:-----------:|:-------------------:|:--------------------------------------------------------------------------------------|
| 1                  | 3V3 Power   | 3.3V               | **3.3V Power Supply** for low-voltage components.                                    |
| 2                  | 5V          | 5V                 | **5V Power Supply** (direct from USB-C power in).                                    |
| 3                  | GPIO2       | SDA                | **I2C Data Line** (default).                                                         |
| 4                  | 5V          | 5V                 | **5V Power Supply** (direct from USB-C power in).                                    |
| 5                  | GPIO3       | SCL                | **I2C Clock Line** (default).                                                        |
| 6                  | GND         | Ground             | **Common Ground Reference**.                                                         |
| 7                  | GPIO4       | GPCLK0             | General-purpose clock pin (also used for 1-Wire with config changes).               |
| 8                  | GPIO14      | TXD                | **UART TX** pin (transmit).                                                          |
| 9                  | GND         | Ground             | **Common Ground Reference**.                                                         |
| 10                 | GPIO15      | RXD                | **UART RX** pin (receive).                                                           |
| 11                 | GPIO17      | GPIO17             | General-purpose I/O. Often used for LED or buzzer.                                   |
| 12                 | GPIO18      | PCM_CLK            | PCM/I2S clock or general-purpose I/O.                                                |
| 13                 | GPIO27      | GPIO27             | General-purpose I/O.                                                                 |
| 14                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 15                 | GPIO22      | GPIO22             | General-purpose I/O.                                                                 |
| 16                 | GPIO23      | GPIO23             | General-purpose I/O.                                                                 |
| 17                 | 3V3 Power   | 3.3V               | **3.3V Power Supply** (another 3.3V rail).                                           |
| 18                 | GPIO24      | GPIO24             | General-purpose I/O.                                                                 |
| 19                 | GPIO10      | MOSI               | **SPI MOSI** (Master Out, Slave In).                                                 |
| 20                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 21                 | GPIO9       | MISO               | **SPI MISO** (Master In, Slave Out).                                                 |
| 22                 | GPIO25      | GPIO25             | General-purpose I/O.                                                                 |
| 23                 | GPIO11      | SCLK               | **SPI Serial Clock**.                                                                |
| 24                 | GPIO8       | CE0                | **SPI Chip Enable 0**.                                                               |
| 25                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 26                 | GPIO7       | CE1                | **SPI Chip Enable 1**.                                                               |
| 27                 | GPIO0       | ID_SD              | **ID EEPROM Data** (used internally for HAT identification).                         |
| 28                 | GPIO1       | ID_SC              | **ID EEPROM Clock** (used internally for HAT identification).                        |
| 29                 | GPIO5       | GPIO5              | General-purpose I/O.                                                                 |
| 30                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 31                 | GPIO6       | GPIO6              | General-purpose I/O.                                                                 |
| 32                 | GPIO12      | GPIO12             | General-purpose I/O, also PWM channel 0, etc.                                        |
| 33                 | GPIO13      | GPIO13             | General-purpose I/O, also PWM channel 1, etc.                                        |
| 34                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 35                 | GPIO19      | GPIO19             | General-purpose I/O, I2S word select (PCM_FS), etc.                                  |
| 36                 | GPIO16      | GPIO16             | General-purpose I/O.                                                                 |
| 37                 | GPIO26      | GPIO26             | General-purpose I/O.                                                                 |
| 38                 | GPIO20      | GPIO20             | General-purpose I/O.                                                                 |
| 39                 | GND         | Ground             | **Common Ground Reference**.                                                         |
| 40                 | GPIO21      | GPIO21             | General-purpose I/O.                                                                 |

> **Notes**:  
> - The BCM GPIO numbers (e.g., GPIO2, GPIO3, etc.) are commonly used in Python with libraries like `RPi.GPIO`.  
> - Pins 27 (ID_SD) and 28 (ID_SC) are reserved for HAT identification and should generally be left unused unless you’re designing a custom HAT with its own ID EEPROM.  
> - Always verify power pins (3.3V and 5V) before making connections to ensure proper voltage levels for your devices.  
> - For more detailed information, consult the [official Raspberry Pi documentation](https://www.raspberrypi.com/documentation/).


| [<img src="MPU6050-Module.jpg" alt="MPU6050 Module" title="MPU6050 Module" width="400px">](MPU6050-Module.jpg) | [<img src="MPU6050-Pinout.png" alt="MPU6050 Pinout" title="MPU6050 Pinout" width="400px">](MPU6050-Pinout.png) |
|:--------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| **MPU6050 Module**                                                                                            | **MPU6050 Pinout**                                                                                             |

#### MPU6050 Pinout Configuration
| Pin Number | Pin Name              | Description                                                                  |
|------------|-----------------------|------------------------------------------------------------------------------|
| 1          | Vcc                   | Provides power to the module (3V-5V). Typically +5V is used.                 |
| 2          | Ground                | Connected to system ground                                                   |
| 3          | Serial Clock (SCL)    | Provides clock pulses for I2C communication                                  |
| 4          | Serial Data (SDA)     | Transfers data via I2C                                                       |
| 5          | Aux Serial Data (XDA) | Can interface additional I2C modules (optional)                              |
| 6          | Aux Serial Clock (XCL)| Can interface additional I2C modules (optional)                              |
| 7          | AD0                   | Used to vary the address if multiple MPU6050s share the same I2C bus         |
| 8          | Interrupt (INT)       | Signals when data is ready for the MCU to read                               |

---

## Software Installation

1. **Update and Upgrade the System**  
   ``` bash
   sudo apt-get update
   sudo apt-get upgrade -y
   ```

2. **Install Python and Libraries**  
   ``` bash

   sudo apt-get update
   sudo apt-get install -y python3-smbus python3-rpi.gpio python3-pandas python3-matplotlib python3-numpy

   sudo apt-get install -y python3-pip python3-dev
   sudo apt-get install -y python3-smbus2  # For I2C communication with MPU-6050
   sudo apt-get install -y python3-RPi.GPIO
   sudo apt-get install -y python3-pandas
   sudo apt-get install -y python3-matplotlib
   sudo apt-get install -y python3-numpy    # Optional for advanced data processing
   ```

3. **Install I2C Tools**  
   ``` bash
   sudo apt-get install -y i2c-tools
   ```

4. **Enable the I2C Interface**  
   - Run the configuration tool:  
     ``` bash
     sudo raspi-config
     ```  
   - Go to **Interface Options** -> **I2C** -> **Enable**.  
   - Reboot the Pi:  
     ``` bash
     sudo reboot
     ```  

5. **Verify the Installation**  
   ``` bash
   ls /dev/i2c*
   sudo i2cdetect -y 1
   ```

   The MPU-6050 sensor should appear at address `0x68`.

---

## Python Code for Delayed Logger
``` python
#!/usr/bin/env python3
"""
Script to monitor impacts using an MPU-6050 accelerometer on a Raspberry Pi.
When a dangerous impact is detected, a buzzer is activated and the event is logged.
A graph of the impact history is generated upon exit.

Suggested improvements and explanatory comments are included throughout.
"""

import smbus                   # To communicate with the MPU-6050 sensor via I2C
import time                    # To manage delays/sleep intervals
import RPi.GPIO as GPIO        # To control GPIO pins (e.g., buzzer)
import pandas as pd            # To handle CSV logging and data management
import matplotlib.pyplot as plt
from datetime import datetime  # To timestamp the logged data

# ------------------------------------------------------------------------------
#                           USER-MANIPULATED VARIABLES
# ------------------------------------------------------------------------------
BUZZER_PIN = 17            # GPIO pin number for the buzzer (BCM numbering)
MPU_ADDRESS = 0x68         # I2C address for the MPU-6050 sensor
IMPACT_THRESHOLD = 15000   # Threshold to trigger an impact alert (tune as needed)
LOG_FILE = "impact_data.csv" # File to which impact data will be logged
SAMPLING_INTERVAL = 0.1    # Time (seconds) between each reading of the sensor
# ------------------------------------------------------------------------------

# MPU-6050 register addresses (do not usually need to change)
ACCEL_XOUT_H = 0x3B  # Address to read X-axis acceleration (high byte)
PWR_MGMT_1 = 0x6B    # Address used to wake the MPU-6050

# Initialize GPIO
GPIO.setmode(GPIO.BCM)           # Use Broadcom GPIO numbering
GPIO.setup(BUZZER_PIN, GPIO.OUT) # Set the buzzer pin as output

# Initialize I2C (MPU-6050)
bus = smbus.SMBus(1)                     # Using I2C bus 1 on Raspberry Pi
bus.write_byte_data(MPU_ADDRESS, PWR_MGMT_1, 0)  # Wake up MPU-6050

def read_raw_data(addr):
    """
    Read two bytes of raw data starting from the provided address on the MPU-6050.
    Returns a 16-bit signed value (taking into account the sensor's two's complement data).
    """
    high = bus.read_byte_data(MPU_ADDRESS, addr)       # Read the high byte
    low = bus.read_byte_data(MPU_ADDRESS, addr + 1)    # Read the low byte
    value = (high << 8) | low

    # Convert to signed value in case the number goes above 32767
    if value > 32768:
        value -= 65536
    return value

def log_data(timestamp, accel_x):
    """
    Appends a new row with the timestamp and X-axis acceleration to the CSV file.
    """
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp},{accel_x}\n")

def generate_graph():
    """
    Reads data from the CSV file, converts timestamps, and plots the acceleration data
    against time. An impact threshold line is also drawn.
    """
    data = pd.read_csv(LOG_FILE, names=["Timestamp", "Acceleration_X"])
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    plt.figure(figsize=(10, 5))
    plt.plot(data['Timestamp'], data['Acceleration_X'], label="Acceleration X")
    plt.axhline(y=IMPACT_THRESHOLD, color="r", linestyle="--", label="Impact Threshold")

    plt.title("Impact History")
    plt.xlabel("Timestamp")
    plt.ylabel("Acceleration (X-Axis)")
    plt.legend()
    plt.grid(True)
    plt.savefig("impact_graph.png")
    plt.show()

def check_impact(threshold):
    """
    Reads current acceleration from MPU-6050, logs the data, and triggers buzzer alert
    if the absolute X-axis acceleration exceeds the given threshold.
    """
    # Read the raw X-axis acceleration data
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_total = abs(acc_x)

    # Create a string timestamp for logging
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log the data to the CSV file
    log_data(timestamp, acc_total)

    # Compare to threshold and activate buzzer if above limit
    if acc_total > threshold:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        print(f"[{timestamp}] Impact detected! Value: {acc_total}")
        time.sleep(1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)

def main():
    """
    Main loop that continuously checks for impacts until interrupted.
    On exit, cleans up GPIO resources and generates a graph of the recorded data.
    """
    print("Monitoring impacts... Press Ctrl+C to stop.")
    try:
        while True:
            check_impact(IMPACT_THRESHOLD)
            time.sleep(SAMPLING_INTERVAL)  # Wait between readings
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()  # Always clean up GPIO
        generate_graph()

if __name__ == "__main__":
    main()
```


## Python Code for Live Logger
``` python
#!/usr/bin/env python3
"""
Helmet Impact Detection with MPU6050 Sensor
===========================================
This program detects impacts on a helmet using the MPU6050 sensor to monitor acceleration and rotation. 
It includes threshold-based alerts, live graphing, and detailed logging. The script is designed for 
debugging and calibration, with verbose output when the DEBUG flag is enabled.

Features:
- Acceleration and rotational measurements with improved accuracy.
- Vector-based impact detection for better sensitivity.
- Adjustable thresholds and sampling rates.
- Calibration at startup for offset correction.

Press Ctrl+C to stop the program.
"""

import smbus                     # For communication with the MPU6050 sensor
import time                      # For timekeeping
import RPi.GPIO as GPIO          # For controlling the buzzer
import pandas as pd              # For data logging
import matplotlib.pyplot as plt  # For live graphing
import matplotlib.animation as animation  # For real-time graph updates
from datetime import datetime    # For timestamping

# -------------------------------------------------------------------------
#                1. USER SETTINGS
# -------------------------------------------------------------------------
USE_BUZZER = True                # Set to False if no buzzer is connected
DEBUG = True                     # Set to True for detailed debug output
BUZZER_PIN = 17                  # GPIO pin for buzzer
MPU_ADDRESS = 0x68               # I2C address of the MPU6050 sensor
IMPACT_THRESHOLD_G = 2.0         # Threshold in g-forces for impact detection
SAMPLE_RATE_HZ = 100             # Data sampling rate in Hz

# Log file configuration
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"{current_time}_helmet_impact_data.csv"

# Graph settings
WINDOW_SIZE = 50                 # Number of data points shown on the graph
LINE_COLOR_ACCEL = "blue"        # Color for acceleration line
LINE_COLOR_GYRO = "orange"       # Color for gyroscope line

# -------------------------------------------------------------------------
#                2. INITIALIZATION
# -------------------------------------------------------------------------
# Set up the buzzer
if USE_BUZZER:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Initialize the I2C bus
bus = smbus.SMBus(1)

# Wake up the sensor
bus.write_byte_data(MPU_ADDRESS, 0x6B, 0)

# Calibration offsets
acc_offset_x = 0
acc_offset_y = 0
acc_offset_z = 0

def calibrate_sensor():
    """Calibrates the MPU6050 to determine acceleration offsets."""
    global acc_offset_x, acc_offset_y, acc_offset_z
    samples = 100
    if DEBUG:
        print("Calibrating sensor...")
    acc_x, acc_y, acc_z = 0, 0, 0
    for _ in range(samples):
        acc_x += read_raw_data(0x3B)
        acc_y += read_raw_data(0x3D)
        acc_z += read_raw_data(0x3F)
        time.sleep(1 / SAMPLE_RATE_HZ)
    acc_offset_x = acc_x / samples
    acc_offset_y = acc_y / samples
    acc_offset_z = acc_z / samples
    if DEBUG:
        print(f"Calibration complete: Offsets -> X: {acc_offset_x}, Y: {acc_offset_y}, Z: {acc_offset_z}")

calibrate_sensor()

# -------------------------------------------------------------------------
#                3. DATA COLLECTION AND IMPACT DETECTION
# -------------------------------------------------------------------------
def read_raw_data(register_address):
    """
    Reads raw 16-bit data from the MPU6050 sensor.
    """
    high_byte = bus.read_byte_data(MPU_ADDRESS, register_address)
    low_byte = bus.read_byte_data(MPU_ADDRESS, register_address + 1)
    value = (high_byte << 8) | low_byte
    if value > 32768:
        value -= 65536
    return value

def check_impact():
    """
    Reads acceleration and gyroscope data, applies offsets, and checks for dangerous impacts.
    """
    # Read raw acceleration data
    raw_x = read_raw_data(0x3B) - acc_offset_x
    raw_y = read_raw_data(0x3D) - acc_offset_y
    raw_z = read_raw_data(0x3F) - acc_offset_z

    # Convert to g-forces
    acc_x_g = raw_x / 16384.0
    acc_y_g = raw_y / 16384.0
    acc_z_g = raw_z / 16384.0

    # Compute vector magnitude
    acc_magnitude_g = (acc_x_g**2 + acc_y_g**2 + acc_z_g**2)**0.5

    # Log data and debug output
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if DEBUG:
        print(f"Timestamp: {timestamp}")
        print(f"Acceleration: X={acc_x_g:.2f}g, Y={acc_y_g:.2f}g, Z={acc_z_g:.2f}g, Total={acc_magnitude_g:.2f}g")

    # Save data to file
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp},{acc_x_g},{acc_y_g},{acc_z_g},{acc_magnitude_g}\n")

    # Check impact
    if acc_magnitude_g > IMPACT_THRESHOLD_G:
        print(f"[{timestamp}] Impact detected! Magnitude: {acc_magnitude_g:.2f}g")
        if USE_BUZZER:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

    return acc_x_g, acc_y_g, acc_z_g, acc_magnitude_g

# -------------------------------------------------------------------------
#                4. LIVE GRAPHING
# -------------------------------------------------------------------------
fig, ax = plt.subplots()
x_vals = []
acc_vals = []

(line_acc,) = ax.plot([], [], label="Acceleration (g)", color=LINE_COLOR_ACCEL)
ax.set_title("Helmet Impact Monitoring")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Acceleration (g)")
ax.legend()
ax.grid(True)

start_time = time.time()

def init_graph():
    """Initialize the graph with empty data."""
    line_acc.set_data([], [])
    return (line_acc,)

def update_graph(frame):
    """Update the graph with new data."""
    acc_x_g, acc_y_g, acc_z_g, acc_magnitude_g = check_impact()
    elapsed_time = time.time() - start_time

    x_vals.append(elapsed_time)
    acc_vals.append(acc_magnitude_g)

    # Keep only the last WINDOW_SIZE values
    x_vals_trimmed = x_vals[-WINDOW_SIZE:]
    acc_vals_trimmed = acc_vals[-WINDOW_SIZE:]

    line_acc.set_data(x_vals_trimmed, acc_vals_trimmed)

    ax.relim()
    ax.autoscale_view()
    return (line_acc,)

ani = animation.FuncAnimation(fig, update_graph, init_func=init_graph, interval=1000 / SAMPLE_RATE_HZ, blit=True)

# -------------------------------------------------------------------------
#                5. MAIN PROGRAM
# -------------------------------------------------------------------------
try:
    print("Starting helmet impact monitoring... Press Ctrl+C to stop.")
    plt.show()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
finally:
    if USE_BUZZER:
        GPIO.cleanup()
```

---

## How It Works
1. The **MPU-6050 accelerometer** measures acceleration forces and sends data to the Raspberry Pi over the I2C bus.  
2. If the measured force exceeds the defined **IMPACT_THRESHOLD**, the buzzer is triggered to alert coaches and staff.  
3. Data is logged into a CSV file (`impact_data.csv`), and a graph is generated upon exit to visualize impact trends over time.

---

## Catholic Values Integration
- **Care for Others:** Reflects compassion for athletes by prioritizing their safety and well-being.  
- **Stewardship:** Demonstrates the responsible use of technology, a gift from God, to serve others.  
- **Human Dignity:** Emphasizes protecting the athlete’s body, honoring the belief that our bodies are temples of the Holy Spirit.

> *"Do you not know that your body is a temple of the Holy Spirit within you?"*  
> — 1 Corinthians 6:19

---

## Display Board and Presentation Script

### Display Board Layout
1. **Title Section**  
   - Title: “Concussion Detection Sensor for Athlete Safety”  
   - Tagline: *Using Technology and Faith to Protect God’s Gift of Life*

2. **Left Panel**  
   - Describe the problem of concussions in sports and the project’s objective.

3. **Center Panel**  
   - Show a visual diagram of the setup (Raspberry Pi, accelerometer, buzzer).  
   - Add a flowchart to explain how the system monitors impacts.  
   - Insert graphs displaying sample impact data.

4. **Right Panel**  
   - Highlight Catholic values with relevant quotes.  
   - Discuss broader implications and future improvements.

5. **Interactive Section**  
   - Live demonstration (if possible) or a QR code linking to a video demonstration.

### Presentation Script for JD
1. **Introduction**  
   - Briefly explain the problem of concussions in sports and why this project is important.  
   - Connect the project to Catholic values (care for others, stewardship, and human dignity).

2. **Demonstration**  
   - Show the prototype in action. Simulate an impact to trigger the buzzer alert.

3. **Discussion**  
   - Present how the collected data (from `impact_data.csv`) is visualized.  
   - Emphasize patterns or trends in the data that can help prevent future injuries.

---

## Additional Resources
- [Raspberry Pi Official Documentation](https://www.raspberrypi.com/documentation/)  
- [MPU-6050 Product Page](https://www.invensense.com/products/motion-tracking/6-axis/mpu-6050/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

---

## License
This project is open-source and available under the **MIT License**. Feel free to modify and distribute for educational or personal use.
