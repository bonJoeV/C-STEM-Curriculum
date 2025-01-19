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
This program measures impacts on a football helmet to see if a hit might be hard enough 
to check for a concussion. It uses a special sensor called the MPU-6050 to measure 
both how much the helmet moves (acceleration) and how much it spins (rotation).

What It Does:
1. Wakes up the sensor (it sleeps by default).
2. Measures how fast the helmet moves (in g-forces).
3. Measures how fast the helmet spins (in degrees per second).
4. Beeps a buzzer if the hit is above a dangerous level.
5. Logs all the data into a file.
6. Shows live graphs of movement and spin to see the impacts in real time.

You can stop the program by closing the graph window or pressing Ctrl+C.
"""

import smbus                     # Helps us talk to the sensor
import time                      # Helps us keep track of time
import RPi.GPIO as GPIO          # Lets us control the buzzer
import pandas as pd              # Saves data to a file
import matplotlib.pyplot as plt  # Draws the live graph
import matplotlib.animation as animation  # Updates the graph
from datetime import datetime    # Keeps track of the current time

# -------------------------------------------------------------------------
#                1. USER SETTINGS: Things You Can Change
# -------------------------------------------------------------------------
USE_BUZZER = True                # Turn this to False if you don't have a buzzer
BUZZER_PIN = 17                  # The pin where the buzzer is connected
MPU_ADDRESS = 0x68               # The sensor's I2C address
IMPACT_THRESHOLD_G = 60          # Dangerous g-force level (concussion threshold)

# Name the file where the data will be saved
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = f"{current_time}_helmet_impact_data.csv"

# Colors for the graph lines
LINE_COLOR_ACCEL = "blue"        # Acceleration data
LINE_COLOR_GYRO = "orange"       # Rotational data

# -------------------------------------------------------------------------
#                2. SETTING UP THE SENSOR AND BUZZER
# -------------------------------------------------------------------------
# Set up the buzzer (if we're using it)
if USE_BUZZER:
    GPIO.setmode(GPIO.BCM)       # Use Broadcom pin numbering
    GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set the buzzer pin to output

# Create an SMBus object to talk to the sensor
bus = smbus.SMBus(1)

# Wake up the sensor (it starts asleep)
bus.write_byte_data(MPU_ADDRESS, 0x6B, 0)

# -------------------------------------------------------------------------
#                3. FUNCTIONS TO READ DATA
# -------------------------------------------------------------------------
def read_raw_data(register_address):
    """
    Reads data from the sensor.
    - High byte and low byte combine to give the full number.
    - If the number is too big, it means it's negative, so we fix that.
    """
    high_byte = bus.read_byte_data(MPU_ADDRESS, register_address)
    low_byte = bus.read_byte_data(MPU_ADDRESS, register_address + 1)
    value = (high_byte << 8) | low_byte
    if value > 32768:
        value -= 65536
    return value

def check_impact(threshold_g):
    """
    Measures acceleration and rotation from the sensor, converts them to real units, 
    and checks if the impact is dangerous.
    - Acceleration is converted to g-forces.
    - Rotation is converted to degrees per second.
    - If the values are too high, it triggers the buzzer.
    """
    # Read acceleration data
    raw_x = read_raw_data(0x3B)
    raw_y = read_raw_data(0x3D)
    raw_z = read_raw_data(0x3F)

    # Read gyroscope data
    gyro_x = read_raw_data(0x43)
    gyro_y = read_raw_data(0x45)
    gyro_z = read_raw_data(0x47)

    # Convert raw acceleration to g-forces
    acc_x_g = raw_x / 16384.0
    acc_y_g = raw_y / 16384.0
    acc_z_g = raw_z / 16384.0

    # Convert raw gyroscope data to degrees per second
    gyro_x_dps = gyro_x / 131.0
    gyro_y_dps = gyro_y / 131.0
    gyro_z_dps = gyro_z / 131.0

    # Get the current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the data to the file
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp},{acc_x_g},{acc_y_g},{acc_z_g},{gyro_x_dps},{gyro_y_dps},{gyro_z_dps}\n")

    # Check if the g-force is too high
    if abs(acc_x_g) > threshold_g or abs(acc_y_g) > threshold_g or abs(acc_z_g) > threshold_g:
        print(f"[{timestamp}] DANGER! Impact detected!")
        print(f"G-Forces: X={acc_x_g:.2f}, Y={acc_y_g:.2f}, Z={acc_z_g:.2f}")
        print(f"Rotation: X={gyro_x_dps:.2f}, Y={gyro_y_dps:.2f}, Z={gyro_z_dps:.2f}")
        if USE_BUZZER:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer
            time.sleep(1)                      # Wait 1 second
            GPIO.output(BUZZER_PIN, GPIO.LOW)  # Turn off buzzer

    return acc_x_g, acc_y_g, acc_z_g, gyro_x_dps, gyro_y_dps, gyro_z_dps

# -------------------------------------------------------------------------
#                4. SETTING UP THE LIVE GRAPH
# -------------------------------------------------------------------------
# Create the graph figure and its axis
fig, ax = plt.subplots()
x_vals = []  # Time values
acc_x_vals, acc_y_vals, acc_z_vals = [], [], []  # Acceleration
gyro_x_vals, gyro_y_vals, gyro_z_vals = [], [], []  # Gyroscope

# Create lines for acceleration and rotation
(line_acc_x,) = ax.plot([], [], label="Accel X (g)", color=LINE_COLOR_ACCEL)
(line_gyro_x,) = ax.plot([], [], label="Gyro X (dps)", color=LINE_COLOR_GYRO)

# Add labels and a legend
ax.set_title("Helmet Impact Data")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True)

# Start time for the graph
start_time = time.time()

def init():
    """Initialize the graph with empty data."""
    line_acc_x.set_data([], [])
    line_gyro_x.set_data([], [])
    return (line_acc_x, line_gyro_x)

def update(frame):
    """
    Update the graph with new data from the sensor.
    """
    acc_x_g, acc_y_g, acc_z_g, gyro_x_dps, gyro_y_dps, gyro_z_dps = check_impact(IMPACT_THRESHOLD_G)
    elapsed_time = time.time() - start_time
    x_vals.append(elapsed_time)

    # Update acceleration and gyroscope data
    acc_x_vals.append(acc_x_g)
    gyro_x_vals.append(gyro_x_dps)

    # Update the lines on the graph
    line_acc_x.set_data(x_vals, acc_x_vals)
    line_gyro_x.set_data(x_vals, gyro_x_vals)

    # Adjust the graph limits
    ax.relim()
    ax.autoscale_view()

    return (line_acc_x, line_gyro_x)

# Create an animation for the live graph
ani = animation.FuncAnimation(fig, update, init_func=init, interval=200, blit=True)

# -------------------------------------------------------------------------
#                5. START MONITORING
# -------------------------------------------------------------------------
try:
    print("Monitoring helmet impacts... Press Ctrl+C to stop.")
    plt.show()
except KeyboardInterrupt:
    print("\nProgram stopped by user. Exiting...")
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
