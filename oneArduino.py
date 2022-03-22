#library Imports
import PySimpleGUI as sg  #this is the import for the Grpafical User interface library
import serial #this is the import for the pibrary which handels the communication with the arduin
from serial.tools import list_ports #Needed for the automatic identication of serial adresses
import Arduino #this is the import for a custom writen class, whihc further abstracts communication with the arduino.
from numpy import asarray, record #this is the import for numpy tool, these tools are used to create and save arrays to csv files.
from numpy import savetxt
import numpy as np
import time #this is import allows for delays(pauses in the code)

#Create Layout for GUI
sg.theme('DarkAmber') # set color scheme for the gaphical user interface (GUI)

layout = [[sg.Text("Lick Chamber Control")], #sets the title for the GUI
        [sg.Text("Enter Experment length (in Minutes)"), sg.InputText()], #first input
        [sg.Text("Enter file name for first box"), sg.InputText()], #second input
        #[sg.Text("Enter file name for second box"), sg.InputText()], #second input
        [sg.Button("Begin Experiment")] #confirmation input
]

window = sg.Window('Window Title', layout) # loads the GUI window
#test
event, values = window.read() #reads any inputs to the window
window.close() # closes the window
    
#print("value 1: ", values[0], "\n", "Value 2: ", values[1]) #prints the valus input by the GUI
minutes = values[0]
first_file_name = values[1]
#second_file_name = values[2]

#confirmation window
sg.popup('Experiment Running')

#automatic identification of serial porsts
port_names = [] # create list to hold the port names of all arduinos connects
ports = list(serial.tools.list_ports.comports()) #use serial tools to read all the port names
for p in ports:
    if(p.description[0:3] == "USB"):
        port_names.append(p.name) #add all ports to the list
print(port_names)
#creation of arduino object
arduino1 = Arduino.Arduino(port_names[0]) #create arduino object from custom class
#arduino2 = Arduino.Arduino(port_names[1])
#creation of empty data array, first value = packet ID, values 2-11 = data for each channel, value 12 = time stamp
data1 = [0,0,0,0,0,0,0,0,0,0,0,0]
#data2 = [0,0,0,0,0,0,0,0,0,0,0,0]
#crate numpy array for saving data
saveData = np.zeros([1,12])
#saveData2 = np.zeros([1,12])
#wait for start command signifing the arduino is ready to begin sending data
firstArduinoReady = False
#secondArduinoReady = False
firstArduinoReady = arduino1.getFirstByte()
#secondArduinoReady = arduino2.getFirstByte()
while(firstArduinoReady == False):
    if(firstArduinoReady == False):
        firstArduinoReady = arduino1.getFirstByte()
    #if(secondArduinoReady == False):
    #    secondArduinoReady = arduino2.getFirstByte()
    
#record time at which the experiment began
start_time = time.time()

#continouly read in data through the serial port
while True:
    #read serial port
    data1 = arduino1.getData()
    #data2 = arduino2.getData()
    #create temporary numpy array
    temp = np.asarray(data1)
    #temp2 = np.asarray(data2)
    
    #add temportay numpy array to the stack of data to be saved
    saveData = np.vstack([saveData, temp])
    #saveData2 = np.vstack([saveData2, temp2])

    #check if time has elapsed
    if(time.time()-start_time > float(values[0])*60):
        break

    #debuging statment
    print(data1, "\r", end='')
  
#indicate that the progam has ended    
print('end')
#create CSV file and save it
savetxt(values[1], saveData, delimiter=',')
#savetxt(values[2], saveData2, delimiter=',')
