# Raspberry Pi Realtime GPS Tracker

## Overview

The issue of speeding poses a significant concern, particularly among teenagers and young undergraduate students. Newly licensed individuals often exhibit a tendency to engage in reckless driving practices, surpassing designated speed limits. Unfortunately, parents and other responsible family members find themselves with limited tools to effectively monitor and address this potentially perilous behavior.
In response to this challenge, our term project aim to develop a system capable of tracking the precise geographical coordinates of a vehicle, calculating its velocity, and flagging instances where the speed exceeds predefined limits by integrating a GPS module and the Raspberry Pi. The collected data will be presented through a user-friendly map GUI on a desktop, offering a visual representation of speeding violations. This initiative not only addresses the immediate safety concerns associated with speeding but also provides caregivers with a proactive means of monitoring and guiding young drivers on the road.

This project fufill the term project requirement of CS370 under Professor Shrideep Pallickara . 

## Table of Contents

- [Problem](#problem)
- [Solution and Implementation](#solution-and-implementation)
  - [Hardware](#hardware)
  - [Python Code for Raspberry Pi](#python-code-for-raspberry-pi)
  - [Making a Realtime Geolocation Tracking Webpage](#making-a-realtime-geolocation-tracking-webpage)
  - [Getting Started](#getting-started)
- [Conclusion](#conclusion)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Problem
Students often struggle to remember where they parked their cars, especially in crowded or unfamiliar parking lots.

## Solution and Implementation
This project can serve as a personal parking location memory assistant. The GPS tracker helps users mark the location where they parked, making it easier to locate their cars later. This feature can be particularly useful for students in large university parking lots or urban areas.
  
### Hardware

For the hardware, a Raspberry Pi 4 is used, but a Raspberry Pi Zero and 3 can also be used. Additionally, a Neo 6M GPS module (though other GPS module is suffice) is required for gathering location data. A standard desktop or laptop is used to receive and display data visually on a webpage. 

### Python Code for Raspberry Pi



### Making a Realtime Geolocation Tracking Webpage

To display the live location of the device, a webpage is created using the PubNub API, which facilitates realtime data delivery. 




## Getting Started

1. Connect the GPS module to the Raspberry Pi according to the hardware instructions.
2. Install the necessary Python library for PubNub using the provided command.
3. Modify the Python code to incorporate PubNub and enable data transmission to the webpage.
4. Run the Python code on the Raspberry Pi to start sending GPS data.

## Conclusion

With this setup, you can now track the realtime location of your Raspberry Pi device from anywhere in the world using the created webpage.

## Authors

- Anton Vulman
- Ezra Hsieh
- Mitchell Barrett

## Acknowledgments

- Special thanks to Arijit Das for the hardware and software instruction on utilizing GPS module with Raspberry Pi. Links for his [video](https://youtu.be/N8fH0nc9v9Q) and [article](https://sparklers-the-makers.github.io/blog/robotics/realtime-gps-tracker-with-raspberry-pi/).
- Thanks to Professor Shrideep Pallickara for support and feedback.
- [Link to video demonstration](link-to-video)

Feel free to contribute and provide feedback!