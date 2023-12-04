# This is the code for GPS connection, inspired Abdullah Jirjees
# https://github.com/AbdullahJirjees/VK-16_GPS/tree/main

# pynmea library used for NMEA 0183 protocol, a data specification for
# communication between marine electronics including GPS receivers. 
# pip install pynmea2

import serial
import pynmea2

def read_gps_data(serial_port='COM3', baudrate=9600):
    # Set serial port, baudrate, and timeout

    ser = serial.Serial(serial_port, baudrate=baudrate, timeout=1)
    while True:
        # read data and parse data message
        data = ser.readline()
        if data.startswith(b'$GPGGA'):
            msg = pynmea2.parse(data.decode('utf-8'))
            print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")

if __name__ == "__main__":
    read_gps_data()
