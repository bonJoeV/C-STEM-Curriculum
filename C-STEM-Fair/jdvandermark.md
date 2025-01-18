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
  - `smbus`
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

## Python Code

Below is the Python code for the concussion detection sensor. Copy and paste it into your Raspberry Pi Python environment.

```python
# Importing necessary libraries
import smbus  # Library to communicate with the sensor (MPU-6050)
import time   # Library to add delays (wait times)
import RPi.GPIO as GPIO  # Library to control the buzzer (alerts)
import pandas as pd  # Library to save data in a table (like Excel)
import matplotlib.pyplot as plt  # Library to create graphs
from datetime import datetime  # Library to work with date and time

# Setup the buzzer (makes a sound when an impact is detected)
BUZZER_PIN = 17  # GPIO pin number for the buzzer
GPIO.setmode(GPIO.BCM)  # Use Broadcom GPIO pin numbering
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set the buzzer pin as output

# Setup the accelerometer (sensor that detects impacts)
MPU_ADDRESS = 0x68  # Address of the MPU-6050 sensor
ACCEL_XOUT_H = 0x3B  # Address to read acceleration data
PWR_MGMT_1 = 0x6B  # Address to turn on the sensor
bus = smbus.SMBus(1)  # Use I2C communication to talk to the sensor
bus.write_byte_data(MPU_ADDRESS, PWR_MGMT_1, 0)  # Turn on the sensor

# Threshold to detect dangerous impacts
IMPACT_THRESHOLD = 15000  # Change this number to make the system more or less sensitive

# File to save the impact data
log_file = "impact_data.csv"

# Function to read raw data from the sensor
def read_raw_data(addr):
    high = bus.read_byte_data(MPU_ADDRESS, addr)
    low = bus.read_byte_data(MPU_ADDRESS, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value -= 65536
    return value

# Function to save impact data
def log_data(timestamp, accel_x):
    with open(log_file, "a") as f:
        f.write(f"{timestamp},{accel_x}\\n")

# Function to create a graph from saved data
def generate_graph():
    data = pd.read_csv(log_file)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    plt.figure(figsize=(10, 5))
    plt.plot(data['Timestamp'], data['Acceleration_X'], label="Acceleration X")
    plt.axhline(y=IMPACT_THRESHOLD, color="r", linestyle="--", label="Impact Threshold")
    plt.title("Impact History")
    plt.xlabel("Timestamp")
    plt.ylabel("Acceleration (X-Axis)")
    plt.legend()
    plt.grid()
    plt.savefig("impact_graph.png")
    plt.show()

# Function to check impacts
def check_impact(threshold):
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_total = abs(acc_x)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_data(timestamp, acc_total)
    if acc_total > threshold:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        print(f"Impact detected! Value: {acc_total}")
        time.sleep(1)
        GPIO.output(BUZZER_PIN, GPIO.LOW)

try:
    print("Monitoring impacts... Press Ctrl+C to stop.")
    while True:
        check_impact(IMPACT_THRESHOLD)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
    generate_graph()
## How It Works
1. The **MPU-6050 accelerometer** measures acceleration forces and sends data to the Raspberry Pi.
2. If the measured force exceeds the **IMPACT_THRESHOLD**, the buzzer is triggered to alert coaches or staff.
3. Data is logged into a CSV file for later analysis, and graphs are generated to visualize impact trends over time.

---

## Catholic Values Integration
- **Care for Others:** This project reflects compassion for athletes by prioritizing their safety and well-being.
- **Stewardship:** Demonstrates the responsible use of technology, a gift from God, to serve others.
- **Quote from 1 Corinthians 6:19:** *\"Do you not know that your body is a temple of the Holy Spirit within you?\"*

---

## Additional Resources
- Refer to the [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/) for help setting up your device.
- Learn more about the [MPU-6050 Accelerometer](https://www.invensense.com/products/motion-tracking/6-axis/mpu-6050/).

---

### License
This project is open-source and available under the MIT License.
"""
