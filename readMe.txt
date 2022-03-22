Author: Samuel Breslin
Email: samrbreslin@gmail.com or samuel.breslin@mpfi.org

This repository contains the Code for the operation of the lick chambers designed by the Max Plank Institute for Nueroscience Mchanical Workeshop for the Stern Lab of the Max Planck Insitite for Nueroscience. The goal of this code is to collect accurate data durring experiments on the feeding habits of mice.

The circutry is run on a  arduino mega using 10 interupt channels trigger by a voltage splitter circut whos output is run throught a lowpass filter for debouncing. Ardunio code is interupt based and is designed to run on an arduino mega with a serial speed of 9600. Currently the issue#1 branch will contain experimental code for automatic detection of the serial ports.

Four channels are based on arduino hardware interupt pins(2, 3, 18, 19), six channels are based on the arduino PIN change interupt libraries(13,12,11,10,A9,A12).

The Python code inputs the serial port as well as the file to which you would like to input the data. it then displays and saves values recoded by the arduino by using matplot lib and the creation of a CSV file. To run this tile one must import the pyserial, numpy, and matplotlib libraries. the data printed and the data save in the csv file will be in this format: [packet number from first arduino, data form the four channels, time packet was sent, paket number from second arduino, data from four channels of the second arduino, and time paket was sent form second arduino

This code will automaticly Identify the all arduinos plugged into the deivce However you will have to use the Graphical user interface to slect how many arduinos you would like to use, the length of the exeriment and the name of the file where you would like the data to be stored.

Instructions for instalation(python Side):
1. Clone the repository using the command: git clone https://github.com/samryan02/MPFI_Stern_Lab_Lick_Chamber_Code.git
2. Install dependencies:
  1. pip3 install PySimpleGUI
  2. pip3 install pyserial
  3. pip3 install numpy
3. chose the file: if you are running one arduino use the oneArduino file, if you are using two use the standard pythonReciver.py file.

  

11/2/2021 version 1.2
