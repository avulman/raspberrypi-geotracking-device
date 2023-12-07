# This is the code for GPS connection, inspired by Abdullah Jirjees
# https://github.com/AbdullahJirjees/VK-16_GPS/tree/main

# PySerial: manages serial communication between serial port and GPS module
# Pynmea2 library used for NMEA 0183 protocol, commonly used in GPS data.
# Geopy library used for geocoding and geographical data manipulation in the program.

# pip install pyserial pynmea2 geopy

import serial
import pynmea2
from geopy.distance import geodesic
from datetime import datetime
import os

# Velocity limit that sets minimum threshold for accounting for incidents
# PROGRAMMER: update velocity limit at a later time, 0.05 m/s is used during development
# 1 MPH = 0.44704 m/s
velocity_limit = 0.05

# Specify the USB drive path
usb_drive_path = "/media/anton/ESD-USB"

def read_gps_data(serial_port='/dev/ttyACM0'):

    # Set serial port name and timeout time
    ser = serial.Serial(serial_port, timeout=1)

    # Ensure reset location and time
    last_location = None
    last_time = None

    # Counter to keep track the number of violations and label them
    violation_count = 0

    while True:
        # Read data and parse data message
        data = ser.readline()
        if data.startswith(b'$GPGGA'):
            msg = pynmea2.parse(data.decode('utf-8'))
            
            # Assign current location and time
            current_location = (msg.latitude, msg.longitude)
            current_time = datetime.now()

            # If location and time exist, calculate velocity
            if last_location is not None and last_time is not None:
                distance = geodesic(last_location, current_location).meters
                time_difference = (current_time - last_time).total_seconds()
                velocity = distance / time_difference if time_difference > 0 else 0.0
                print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}, Velocity: {velocity} m/s")

                # Call write_velocity_violation and update violation count if velocity is greater than velocity limit
                if velocity > velocity_limit:
                    violation_count += 1
                    write_velocity_violation(current_time, current_location, velocity, violation_count)
                    
            # Set last location/time as current after most recent calculation
            last_location = current_location
            last_time = current_time

# Helper function to write and save velocity violation data
def write_velocity_violation(current_time, current_location, velocity, violation_count):

    # Construct the full file path on the USB drive
    file_path = os.path.join(usb_drive_path, "velocity_violations.txt")
    print(f"Writing to file: {file_path}")

    # If velocity_violations.txt file doesn't exist, create. if velocity_violations.txt file exists, append count, time, location, and velocity for each velocity violation
    with open(file_path, "a") as file:
        violation_info = f"Velocity Violation #{violation_count}: {current_time}, {current_location}, {velocity} m/s\n"
        file.write(violation_info)

if __name__ == "__main__":
    read_gps_data()
