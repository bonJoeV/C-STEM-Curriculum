#!/usr/bin/env python3
"""
Helmet Tap Detection with MPU6050 Sensor and Real-Time Graphing
===============================================================
This program detects taps on a helmet using the MPU6050 sensor and displays real-time graphs
of high-pass filtered acceleration values.

Features:
- Tap detection based on high-pass filtered acceleration.
- Real-time graphing of filtered acceleration values.
- Records and prints the top 10 maximum hits with timestamps.

Press Ctrl+C to stop the program.
"""

import smbus
import time
import RPi.GPIO as GPIO
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------------------------------------------------
#                1. CONSTANTS AND SETTINGS
# -------------------------------------------------------------------------
# Graph-related variables
GRAPH_MAIN_TITLE = "Athlete Helmet Safety Sensor"  # Main title of the graph
GRAPH_SUBTITLE = "Real-Time Concussion Detection with Technology and Faith"  # Subtitle of the graph
X_AXIS_LABEL = "Time (s)"  # X-axis label
Y_AXIS_LABEL = "Acceleration (g)"  # Y-axis label
LEGEND_TITLE = "Legend"  # Legend title
TOP_HITS_LABEL = "Top Hits:\n"  # Label for the top hits section
GRAPH_Y_LIMITS = (-15, 15)  # Fixed Y-axis limits
GRAPH_WINDOW_SIZE = 100  # Number of data points displayed in the graph window
NUM_TOP_HITS = 5  # Number of top hits to display in the graph
GRAPH_TITLE_FONT_SIZE = 14  # Font size for the main title
GRAPH_SUBTITLE_FONT_SIZE = 10  # Font size for the subtitle

# Numerical Constants
USE_BUZZER = False
DEBUG = False
BUZZER_PIN = 17  # GPIO pin for buzzer
MPU_ADDRESS = 0x68  # I2C address of the MPU6050 sensor
TAP_THRESHOLD_G = 2.0  # Threshold in g-forces for a tap
COOLDOWN_SECONDS = 0.5  # Cooldown period after a tap detection
SAMPLE_RATE_HZ = 100  # Data sampling rate in Hz
HIGH_PASS_ALPHA = 0.85  # High-pass filter coefficient (0.8–0.99)
CALIBRATION_SAMPLES = 100  # Number of samples for sensor calibration
BEEP_DURATION = 0.2  # Duration of buzzer beep in seconds

# -------------------------------------------------------------------------
#                2. INITIALIZATION
# -------------------------------------------------------------------------
# Set up the buzzer
if USE_BUZZER:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Initialize the I2C bus
bus = smbus.SMBus(1)

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

# Wake up the sensor and configure sensitivity
bus.write_byte_data(MPU_ADDRESS, 0x6B, 0)  # Wake up the MPU6050
bus.write_byte_data(MPU_ADDRESS, 0x1C, 0x18)  # Set accelerometer range to ±16g

# Calibration offsets
acc_offset_x = 0
acc_offset_y = 0
acc_offset_z = 0

def calibrate_sensor():
    """Calibrates the MPU6050 to determine acceleration offsets."""
    global acc_offset_x, acc_offset_y, acc_offset_z
    if DEBUG:
        print("Calibrating sensor...")
    acc_x, acc_y, acc_z = 0, 0, 0
    for _ in range(CALIBRATION_SAMPLES):
        acc_x += read_raw_data(0x3B)
        acc_y += read_raw_data(0x3D)
        acc_z += read_raw_data(0x3F)
        time.sleep(1 / SAMPLE_RATE_HZ)
    acc_offset_x = acc_x / CALIBRATION_SAMPLES
    acc_offset_y = acc_y / CALIBRATION_SAMPLES
    acc_offset_z = acc_z / CALIBRATION_SAMPLES
    if DEBUG:
        print(f"Calibration complete: Offsets -> X: {acc_offset_x}, Y: {acc_offset_y}, Z: {acc_offset_z}")

calibrate_sensor()

# High-pass filter states
last_acc_x = 0
last_acc_y = 0
last_acc_z = 0

# Timestamp of the last detected tap
last_tap_time = 0

# Graph data buffers
x_vals = []
acc_x_vals = []
acc_y_vals = []
acc_z_vals = []

# List to store maximum hits
max_hits = []

def high_pass_filter(new_value, last_value):
    """
    Applies a high-pass filter to isolate high-frequency changes (like taps).
    """
    return HIGH_PASS_ALPHA * (last_value + new_value - last_value)

def detect_tap():
    """
    Reads acceleration data, applies a high-pass filter, checks for taps, 
    and updates graph data.
    """
    global last_acc_x, last_acc_y, last_acc_z, last_tap_time

    # Read raw acceleration data
    raw_x = read_raw_data(0x3B) - acc_offset_x
    raw_y = read_raw_data(0x3D) - acc_offset_y
    raw_z = read_raw_data(0x3F) - acc_offset_z

    # Convert to g-forces
    acc_x_g = raw_x / 2048.0  # Sensitivity for ±16g is 2048 LSB/g
    acc_y_g = raw_y / 2048.0
    acc_z_g = raw_z / 2048.0

    # Apply high-pass filter
    acc_x_filtered = high_pass_filter(acc_x_g, last_acc_x)
    acc_y_filtered = high_pass_filter(acc_y_g, last_acc_y)
    acc_z_filtered = high_pass_filter(acc_z_g, last_acc_z)

    # Update last values
    last_acc_x = acc_x_filtered
    last_acc_y = acc_y_filtered
    last_acc_z = acc_z_filtered

    # Compute magnitude of filtered acceleration
    acc_magnitude = (acc_x_filtered**2 + acc_y_filtered**2 + acc_z_filtered**2) ** 0.5

    # Get current time
    current_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update graph data
    x_vals.append(current_time)
    acc_x_vals.append(acc_x_filtered)
    acc_y_vals.append(acc_y_filtered)
    acc_z_vals.append(acc_z_filtered)

    # Trim graph data to window size
    x_vals[:] = x_vals[-GRAPH_WINDOW_SIZE:]
    acc_x_vals[:] = acc_x_vals[-GRAPH_WINDOW_SIZE:]
    acc_y_vals[:] = acc_y_vals[-GRAPH_WINDOW_SIZE:]
    acc_z_vals[:] = acc_z_vals[-GRAPH_WINDOW_SIZE:]

    # Check for a tap
    if acc_magnitude > TAP_THRESHOLD_G and (current_time - last_tap_time > COOLDOWN_SECONDS):
        last_tap_time = current_time
        print(f"Tap detected! Magnitude: {acc_magnitude:.2f}g at {timestamp}")
        max_hits.append((timestamp, acc_magnitude))
        if USE_BUZZER:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(BEEP_DURATION)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

    # Debug output
    if DEBUG:
        print(f"Raw Acceleration: X={acc_x_g:.2f}g, Y={acc_y_g:.2f}g, Z={acc_z_g:.2f}g")
        print(f"Filtered Acc: X={acc_x_filtered:.2f}g, Y={acc_y_filtered:.2f}g, Z={acc_z_filtered:.2f}g, Magnitude={acc_magnitude:.2f}g")

# -------------------------------------------------------------------------
#                3. LIVE GRAPHING
# -------------------------------------------------------------------------
fig, ax = plt.subplots()

# Define the graph lines
line_x, = ax.plot([], [], label="G-force X", color="blue")
line_y, = ax.plot([], [], label="G-force Y", color="green")
line_z, = ax.plot([], [], label="G-force Z", color="red")

# Set titles and labels
ax.set_title(GRAPH_MAIN_TITLE, fontsize=GRAPH_TITLE_FONT_SIZE)
fig.suptitle(GRAPH_SUBTITLE, fontsize=GRAPH_SUBTITLE_FONT_SIZE)
ax.set_xlabel(X_AXIS_LABEL)
ax.set_ylabel(Y_AXIS_LABEL)
ax.legend(title=LEGEND_TITLE, loc="upper right")
ax.grid(True)
ax.set_ylim(GRAPH_Y_LIMITS)

# Text box for displaying top hits
top_hits_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=10,
                        verticalalignment="top", horizontalalignment="left")

def init_graph():
    """Initialize the graph with empty data."""
    line_x.set_data([], [])
    line_y.set_data([], [])
    line_z.set_data([], [])
    top_hits_text.set_text("")  # Clear the top hits text box
    return line_x, line_y, line_z, top_hits_text

def update_graph(frame):
    """Update the graph with new filtered data and show top hits."""
    detect_tap()

    # Update graph lines
    line_x.set_data(x_vals, acc_x_vals)
    line_y.set_data(x_vals, acc_y_vals)
    line_z.set_data(x_vals, acc_z_vals)

    # Show the last 10 seconds on the x-axis
    if x_vals:
        ax.set_xlim(max(x_vals[-1] - 10, x_vals[0]), x_vals[-1])

    # Update the top hits text box
    max_hits.sort(key=lambda x: x[1], reverse=True)  # Sort by magnitude, descending
    top_hits_display = "\n".join([f"{t[0]}: {t[1]:.2f}g" for t in max_hits[:NUM_TOP_HITS]])
    top_hits_text.set_text(f"{TOP_HITS_LABEL}{top_hits_display}")

    return line_x, line_y, line_z, top_hits_text

ani = animation.FuncAnimation(fig, update_graph, init_func=init_graph, interval=1000 / SAMPLE_RATE_HZ, blit=True)

# -------------------------------------------------------------------------
#                4. MAIN PROGRAM
# -------------------------------------------------------------------------
try:
    print("Starting helmet tap detection with graphing... Press Ctrl+C to stop.")
    plt.show()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
finally:
    if USE_BUZZER:
        GPIO.cleanup()
    max_hits.sort(key=lambda x: x[1], reverse=True)
    print("\nTop 10 Maximum Hits:")
    print("{:<20} {}".format("Timestamp", "Magnitude (g)"))
    for timestamp, magnitude in max_hits[:10]:
        print(f"{timestamp:<20} {magnitude:.2f}")
