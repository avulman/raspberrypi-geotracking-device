# This is the code for GPS connection, inspired Arijit Das' article

# pynmea library used for NMEA 0183 protocol, a data specification for
# communication between marine electronics including GPS receivers. 
# pip install pynmea2

# This module encapsulates the access for the serial port.
import serial

# This module provide various time-related functions
import time 
import string
import pynmea2

# Infinite loop to continuously read GPS data
while True: 
    # Specify the serial port on Raspberry Pi
    port = '/dev/ttyAMA0'

    # Initialize a serial connection with the specified port, baudrate, and timeout
    # 9600 baudrate is the default for many GPS modules
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)

    # Create an instance of NMEAStreamReader for parsing NMEA sentences
    dataOut = pynmea2.NMEAStreamReader()

    # Read a line of NMEA sentence from the serial port
    newData = ser.readline()

    # Check if the NMEA sentence starts with '$GPRMC'
    if newData[0:6] == '$GPRMC':
        # Parse the NMEA sentence, create a message object with GPS data
        newMsg = pynmea2.parse(newData)

        # Extract latitude and longitude information from the parsed message
        lat = newMsg.latitude
        long = newMsg.longtitude

        # Print the GPS coordinates 
        gpsCoord = 'Latitude=' + str(lat) + 'Longtitude=' + str(long)
        print(gpsCoord)
