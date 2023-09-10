#!/bin/bash

### MAKE SURE THE FILE HAS EXECUTE PERMISSIONS ###
# $ sudo chmod +x adb_connect_wifi.sh
# $ ./adb_connect_wifi.sh

# Get the list of connected devices
devices=$(adb devices | awk 'NR>1 {print $1}')

# Iterate over each device
for device in $devices
do
  # Get the device IP address
  ip=$(adb -s $device shell ifconfig wlan0 | awk '/inet addr/{print substr($2,6)}')

  # Connect to ADB over Wi-Fi
  adb -s $device tcpip 5555
  adb -s $device connect $ip:5555

  # Print the device name and connection status
  echo "Connected to $device over Wi-Fi"
done