# Concussion Detection Sensor for Athlete Safety

**Using Technology and Faith to Protect God's Gift of Life**

---

## Objective

Design and demonstrate a concussion detection sensor prototype that can monitor impacts in sports and alert coaches to potential concussions. Use historical data to analyze trends and integrate Catholic values of compassion, stewardship, and human dignity.

---

## Materials

### Hardware
- Raspberry Pi 400 (or another Raspberry Pi model).
- MPU-6050 Accelerometer/Gyroscope Module.
- Buzzer (for audible alerts).
- Breadboard and jumper wires.
- MicroSD card with Raspberry Pi OS.
- Helmet (for mounting the sensor).
- Portable battery pack (to power the Raspberry Pi for portability).
- Velcro or glue (for attaching the sensor to the helmet).
- USB flash drive or cloud setup (to save historical data).

### Software
- Python libraries:
  - `smbus2`
  - `RPi.GPIO`
  - `matplotlib`
  - `pandas`
  - `datetime`

---

## Display Board and Presentation Script

### Display Board Layout
1. **Title Section**
   - Title: "Concussion Detection Sensor for Athlete Safety"
   - Tagline: *Using Technology and Faith to Protect God's Gift of Life*

2. **Left Panel**
   - Describe the problem of concussions in sports and the project objective.

3. **Center Panel**
   - Include a visual diagram of the setup, flowchart of how the system works, and graphs of impact data.

4. **Right Panel**
   - Integrate Catholic values with quotes and broader implications of the project.

5. **Interactive Section**
   - Include a live demonstration or a QR code linking to a video of the project.

---

### Presentation Script for JD
1. **Introduction**
   - Explain the purpose of the project and its connection to Catholic values.
   
2. **Demonstration**
   - Show how the prototype works by detecting impacts and triggering the alert system.

3. **Discussion**
   - Discuss how historical data graphs can help identify patterns and prevent injuries.

---


# Raspberry Pi <-> MPU-6050 Connections

This document outlines how to wire the MPU-6050 sensor to a Raspberry Pi for I2C communication, as well as how to connect a buzzer for impact alerts.

## Pinout Table

| **Raspberry Pi Pin (Physical #)** | **BCM GPIO** | **MPU-6050 Pin** | **Description**                           |
|:---------------------------------:|:-----------:|:---------------:|-------------------------------------------|
| **Pin 1**                         | 3V3 Power   | **VCC**          | Power to the MPU-6050 (3.3V)<br>*Check if your module can accept 5V* |
| **Pin 3**                         | GPIO2 (SDA) | **SDA**          | I2C Data Line                             |
| **Pin 5**                         | GPIO3 (SCL) | **SCL**          | I2C Clock Line                            |
| **Pin 6**                         | GND         | **GND**          | Ground reference                          |

> **Note**: Some MPU-6050 boards have onboard voltage regulators, allowing 5V input on VCC.  
> Always confirm the acceptable voltage input for your specific module.

## Optional Pins

- **INT (Interrupt)** on the MPU-6050 can be connected to any free GPIO pin on the Raspberry Pi if you want to use interrupt-driven events (e.g., GPIO4, GPIO17, etc.). This is not required for basic polling or simple I2C reads.

## Buzzer Pin (from Example Script)

If you are using a buzzer for impact alerts as in the provided script:

| **Raspberry Pi Pin (Physical #)** | **BCM GPIO** | **Buzzer Pin** | **Description**              |
|:---------------------------------:|:-----------:|:--------------:|------------------------------|
| **Pin 11**                        | GPIO17       | **+** (Buzzer) | Positive leg of the buzzer   |
| **Any GND** pin (e.g. Pin 6)      | GND         | **-** (Buzzer) | Ground leg of the buzzer     |

> **Note**: If your buzzer requires more current than the GPIO pin can safely supply, you should use a transistor driver circuit with an appropriate resistor rather than driving the buzzer directly from the GPIO.

## Quick Wiring Overview

1. **MPU-6050 VCC** → **3.3V** on Raspberry Pi (Physical Pin 1).  
   *Check whether your MPU-6050 board supports 5V if you plan to use that.*
2. **MPU-6050 GND** → **GND** on Raspberry Pi (Physical Pin 6 or any other GND).
3. **MPU-6050 SCL** → **BCM GPIO3** (Physical Pin 5).
4. **MPU-6050 SDA** → **BCM GPIO2** (Physical Pin 3).
5. **Buzzer +** → **BCM GPIO17** (Physical Pin 11).
6. **Buzzer -** → **GND** on the Raspberry Pi (Physical Pin 6 or any other GND).

## Additional Notes

- **I2C Interface**: Make sure I2C is enabled on the Raspberry Pi. You can enable this via:
  - `sudo raspi-config` → **Interfacing Options** → **I2C** → **Enable**
  - Or the Raspberry Pi configuration tool in the desktop environment.
- **Pull-Up Resistors**: Many MPU-6050 breakout boards include pull-up resistors on SDA and SCL. If yours does not, you may need to add external pull-up resistors (typically 4.7kΩ) to 3.3V.
- **Voltage Levels**: If the MPU-6050 board lacks level shifting or regulators, ensure you use 3.3V to avoid damaging the sensor.
- **Buzzer Requirements**: If you have a passive buzzer or one that draws more current than the GPIO can supply, use a transistor or MOSFET driver circuit and an appropriate flyback diode, if needed.

With these connections and considerations, your MPU-6050 should be able to communicate with the Raspberry Pi over I2C, and the buzzer can be activated under your impact threshold logic.


> **Explanation**  
> - **Raspberry Pi 3.3V (Pin 1)** connects to **MPU-6050 VCC**.  
> - **Raspberry Pi GPIO2 (SDA, Pin 3)** connects to **MPU-6050 SDA**.  
> - **Raspberry Pi GPIO3 (SCL, Pin 5)** connects to **MPU-6050 SCL**.  
> - **Raspberry Pi GND** goes to **MPU-6050 GND** and **Buzzer negative pin**.  
> - **Raspberry Pi GPIO17 (Pin 11)** goes to **Buzzer positive pin**.

---

### Additional Wiring Tips

- Ensure I2C is enabled in your Pi configuration (`sudo raspi-config`).
- Check whether your MPU-6050 supports 3.3V **or** 5V on VCC.  
- If your module doesn’t have onboard pull-up resistors for SDA/SCL, you may need 4.7 kΩ pull-ups to 3.3V.  
- For the buzzer, if it’s a high-current or high-voltage buzzer, use a transistor (NPN or MOSFET) with an appropriate current-limiting resistor and a diode if needed.

## Python Code

Below is the Python code for the concussion detection sensor. Copy and paste it into your Raspberry Pi Python environment.

```python
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
GPIO.setmode(GPIO.BCM)          # Use Broadcom GPIO numbering
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
---

## Software Installation Instructions

Follow these steps to install all the necessary software and libraries on your Raspberry Pi for the project:

### Update and Upgrade the System
Run these commands to ensure your Raspberry Pi has the latest updates:
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### Install Python and Libraries
Install the required Python libraries and tools:
```bash
sudo apt-get install -y python3-pip python3-dev
sudo apt-get install -y python3-smbus2  # For I2C communication with MPU-6050
sudo apt-get install -y python3-RPi.GPIO  # For Raspberry Pi GPIO control
sudo apt-get install -y python3-pandas  # For handling and saving data
sudo apt-get install -y python3-matplotlib  # For graph generation
sudo apt-get install -y python3-numpy  # Optional: For advanced data processing
```

### Install I2C Tools
Install tools to debug and manage I2C communication:
```bash
sudo apt-get install -y i2c-tools
```

### Enable the I2C Interface
Enable the I2C interface on your Raspberry Pi:
1. Run the Raspberry Pi configuration tool:
   ```bash
   sudo raspi-config
   ```
2. Navigate to **Interface Options** -> **I2C** -> **Enable**.
3. Reboot the Raspberry Pi for the changes to take effect:
   ```bash
   sudo reboot
   ```

### Verify Installation
After installation, verify that the I2C interface and the MPU-6050 sensor are working:
```bash
# Check if I2C is enabled
ls /dev/i2c*

# Detect the MPU-6050 sensor
sudo i2cdetect -y 1
```

The MPU-6050 sensor should appear at address `0x68`.

---

## How It Works
1. The **MPU-6050 accelerometer** measures acceleration forces and sends data to the Raspberry Pi.
2. If the measured force exceeds the **IMPACT_THRESHOLD**, the buzzer is triggered to alert coaches or staff.
3. Data is logged into a CSV file for later analysis, and graphs are generated to visualize impact trends over time.

---

## Catholic Values Integration
- **Care for Others:** This project reflects compassion for athletes by prioritizing their safety and well-being.
- **Stewardship:** Demonstrates the responsible use of technology, a gift from God, to serve others.
- **Quote from 1 Corinthians 6:19:** *"Do you not know that your body is a temple of the Holy Spirit within you?"*

---

## Additional Resources
- Refer to the [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/) for help setting up your device.
- Learn more about the [MPU-6050 Accelerometer](https://www.invensense.com/products/motion-tracking/6-axis/mpu-6050/).

---

### License
This project is open-source and available under the MIT License.
