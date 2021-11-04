Author: Samuel Breslin
Email: samrbreslin@gmail.com or samuel.breslin@mpfi.org

This repository contains the Code for the operation of the lick chambers designed by the Max Plank Institute for Nueroscience Mchanical Workeshop for the Stern Lab of the Max Planck Insitite for Nueroscience. The goal of this code is to 

The circutry is run on a  arduino mega using four interupt channels trigger by a voltage splitter circut whos output is run throught a lowpass filter for debouncing. Ardunio code is interupt based and is designed to run on an arduino mega with a serial speed of 9600

The Python code inputs the serial port as well as the file to which you would like to input the data. it then displays and saves values recoded by the arduino by using matplot lib and the creation of a CSV file. To run this tile one must import the pyserial, numpy, and matplotlib libraries.

For serial communitcation plase find the serial port for your particualr device and copy and paste this into the code, this can be done using the arduno IDE or the arduino web editor, please note that the serial ports have diffrent naming convention in windows and Mac OS.

Currently the arduino schetch is set to run a 20 second test run however this can be esialy changed

11/2/2021 version 1.2
