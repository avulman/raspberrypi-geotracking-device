# Raspberry Pi 4 Model B Speeding Detection with VK-162 GPS Module 

## Overview

The issue of speeding poses a significant concern, particularly among teenagers and young undergraduate students. Newly licensed individuals often exhibit a tendency to engage in reckless driving practices, surpassing designated speed limits. Unfortunately, parents and other responsible family members find themselves with limited tools to effectively monitor and address this potentially perilous behavior.
In response to this challenge, our term project aim to develop a system capable of tracking the precise geographical coordinates of a vehicle, calculating its velocity, and flagging instances where the speed exceeds predefined limits by integrating a GPS module and the Raspberry Pi. The collected data will be presented through a user-friendly map GUI on a desktop, offering a visual representation of speeding violations. This initiative not only addresses the immediate safety concerns associated with speeding but also provides caregivers with a proactive means of monitoring and guiding young drivers on the road.

This project fufill the term project requirement of CS370 under Professor Shrideep Pallickara. 

## Files and Directories
- gps.py: script to record GPS data and calculate velocity
- map_app.py: Web app to display location of speed violation on an embedded Google map, includes velocity and legal speed limit of the roads in interest.
- templates
  - map.html: Main template for the web map app. 
- README.md: This file. 

## Table of Contents

- [Problem](#problem)
- [Solution and Implementation](#solution-and-implementation)
  - [Hardware](#hardware)
  - [Pairing a local server with Google Maps API](#pairing-a-local-server-with-google-maps-api)
  - [Getting Started](#getting-started)
- [Conclusion](#conclusion)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Problem
In an effort to promote safe driving, there is a need to monitor and track vehicle speed, especially in scenarios where speed limits need to be enforced.

## Solution and Implementation
This project addresses the problem by creating a system that utilizes a Raspberry Pi and a USB GPS module to track real-time location data. When the velocity exceeds a predefined speed limit, the incident details are recorded onto a USB drive. The recorded data can then be visualized on a desktop computer using Google Maps.
  
### Hardware

For the hardware, a Raspberry Pi 4 Model B 8GB single board computer is used, but a Raspberry Pi Zero and 3 can also be used. Additionally, VK-162 G-Mouse USB GPS Dongle Navigation Module (though other GPS module is suffice) is required for gathering location data. A 16GB SanDisk USB flash drive is used, for the purpose of transferring a text file with an incident report from the Pi to the desktop for visual data analysis. A standard desktop or laptop is used to display data visually on a local server webpage, with the use of Google Maps API.


### Pairing a local server with Google Maps API

There's no better way to analyze the context of speeding incidents than to display all related data visually with Google Maps API. Simply create your own Google Maps API key, generate a map, and input these values into map_app.py. Modification of serial port and external storage for file transfer is more than likely going to be necessary to replicate.


## Solution and Implementation

1. Connect the USB GPS module and USB flash drive (or any other external storage) to the Raspberry Pi according to the hardware instructions.
2. Install the necessary Python libraries (pip install pyserial pynmea2 geopy)
3. Modify gps.py and map_app.py code to include wanted/correct predefined speed limit (in m/s), Google Maps API key, file path velocity_violations.txt (to read and write), and serial port.
4. Run gps.py program using a headless setup in a car, configuring start on power is highly recommended.
5. Collect data, ensure to exceed predefined set limit for incidents to populate velocity_violations.txt.
6. Transfer velocity_violations.txt to desktop.
7. Run map_app.py on a local server.
8. Use visual data as desired.

## Conclusion

This setup enables accurate and reliable tracking and recording of speeding incidents, providing a useful tool for monitoring and improving driving habits.

## Authors

- Anton Vulman
- Ezra Hsieh
- Mitchell Barrett

## Acknowledgments

- Special thanks to Abdullah Jirjees for the hardware and software instruction on utilizing GPS module with a desktop on Windows 11. It ignited our desire to make this possible with a more portable device: Raspberry Pi 4 Model B. Links for his [video](https://youtu.be/mUsKgzem9ig?si=Tt_C2jrQ-fzjQ4eM) and [GitHub](https://github.com/AbdullahJirjees/VK-16_GPS/tree/main).
- Thanks to Professor Shrideep Pallickara and TA's for support and feedback.
- [Link to video demonstration](link-to-video)

Feel free to contribute and provide feedback!
