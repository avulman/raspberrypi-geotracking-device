# This is the code for GPS connection, inspired Abdullah Jirjees
# https://github.com/AbdullahJirjees/VK-16_GPS/tree/main

# pynmea library used for NMEA 0183 protocol, a data specification for
# communication between marine electronics including GPS receivers. 
# pip install pynmea2
# pip install geopy

import serial
import pynmea2
from geopy.distance import geodesic
from datetime import datetime

def read_gps_data(serial_port='/dev/ttyACM0'):

    # set serial port name and timeout time
    ser = serial.Serial(serial_port, timeout=1)

    # ensure reset location and time
    last_location = None
    last_time = None

    while True:

        # read data and parse data message
        data = ser.readline()
        if data.startswith(b'$GPGGA'):
            msg = pynmea2.parse(data.decode('utf-8'))
            
            # assign current location and time
            current_location = (msg.latitude, msg.longitude)
            current_time = datetime.utcnow()

            # if location and time exist, calculate velocity
            if last_location is not None and last_time is not None:
                distance = geodesic(last_location, current_location).meters
                time_difference = (current_time - last_time).total_seconds()
                velocity = distance / time_difference if time_difference > 0 else 0.0
                print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}, Velocity: {velocity} m/s")

                if velocity > 0.05: # PROGRAMMER: update velocity limit at a later time, 0.05 m/s is used for testing
                    write_velocity_violation(current_time, current_location, velocity)

            # "save" feature
            last_location = current_location
            last_time = current_time

def write_velocity_violation(current_time, current_location, velocity):

    # if velocity_violations.txt file doesn't exist, create. if velocity_violations.txt file exists, append time, location, and velocity for each velocity violation
    with open("velocity_violations.txt", "a") as file:
        violation_info = f"Velocity Violation: {current_time}, {current_location}, {velocity} m/s\n"
        file.write(violation_info)

if __name__ == "__main__":
    read_gps_data()