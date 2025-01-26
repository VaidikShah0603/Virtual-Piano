PROJECT OVERVIEW:
This project aims to create a virtual piano using Arduino UNO R3 and programming language like C++ and Python. The main objective of this project is to simulate the piano which produces different musical notes without using piano keys and according to the distance of the finger tip from the ultrasonic sensor 

MECHANISM:
For making this project we used the Arduino IDE software in which we wrote a code for detecting the distance of the fingertip from the sensor.
Then using the Python programming language, we connected the Serial Monitor of the Arduino IDE software with the Python code. For the Python code we imported 3 Libraries mainly Serial, Pygame, Time. Python code mainly comprises of the code of connecting the Serial Monitor and then storing the various notes in wav audio format like Sa, Re, Ga, Ma, Pa, Dh, Ni in an array. And using else if condition we set the code to play different notes according to the distance detected of the fingertip. 

Source Code folder contains the Arduino code and python code.
Demo/Setup/Documentation contains the schematic circuit diagram and actual setup.
