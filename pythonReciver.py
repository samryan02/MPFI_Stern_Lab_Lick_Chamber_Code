#library Imports
import PySimpleGUI as sg
import serial
from serial.tools import list_ports #Needed for the automatic identication of serial adresses
import Arduino
from numpy import asarray, record
from numpy import savetxt
import numpy as np
import time

#Create Layout for GUI
sg.theme('DarkAmber')

layout = [[sg.Text("Lick Chamber Control")],
        [sg.Text("Enter Experment length (in Minutes)"), sg.InputText()],
        [sg.Text("Enter file name"), sg.InputText()],
        [sg.Button("Begin Experiment")]
]

window = sg.Window('Window Title', layout)

event, values = window.read()    
window.close()
    
print("value 1: ", values[0], "\n", "Value 2: ", values[1])
minutes = values[0]
files_name = values[1]

#confirmation window
sg.popup('Experiment Running')

#automatic identification of serial porsts
port_names = []
ports = list(serial.tools.list_ports.comports())
for p in ports:
    port_names.append(p.name)

#creation of arduino object
arduino1 = Arduino.Arduino(port_names[0])

#creation of empty data array, first value = packet ID, values 2-11 = data for each channel, value 12 = time stamp
data1 = [0,0,0,0,0,0,0,0,0,0,0,0]

#crate numpy array for saving data
data = np.zeros([1,12])

#wait for start command signifing the arduino is ready to begin sending data
startline = arduino1.getFirstByte()
while(startline != True):
    startline = arduino1.getFirstByte()
    print(startline)

#record time at which the experiment began
start_time = time.time()

#continouly read in data through the serial port
while True:
    #read serial port
    data1 = arduino1.getData()
  
    #create temporary numpy array
    temp = np.asarray(data1)
    
    #add temportay numpy array to the stack of data to be saved
    data = np.vstack([data, temp])

    #check if time has elapsed
    if(time.time()-start_time > float(values[0])*60):
        break

    #debuging statment
    print(data1)

#indicate that the progam has ended    
print('end')
#create CSV file and save it
savetxt(values[1], data, delimiter=',')
