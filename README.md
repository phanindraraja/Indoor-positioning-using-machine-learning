# Indoor-positioning-using-Bluetooth-Low-Energy-and-machine-learning

An indoor positioning system model was developed using Bluetooth Low Energy. Machine learning is used to predict the location from the training data. Received Signal Strength Indicator (RSSI) was used as a parameter for location estimation. CC2540 beacons were used as BLE modules.

Refer Project report for detailed description

## Getting started

Hex_code.hex is the hex code to be loaded onto the CC2540 beacons.

Data_for_analysis.py is to get the RSSI training data from beacons and save it in a csv file on the PC through serial communication

Demo_data.py is for getting the test data

Demo.py is to develop the logistic regression model from the training data, predict the location from the test data and send the location as a text file to an android device connected via bluetooth.

The android app developed reads the text file from the bluetooth directory on the android device and display the location on the app.
