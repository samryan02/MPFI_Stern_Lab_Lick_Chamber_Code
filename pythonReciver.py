#imports(only numpy, matplot lib, and serial must be installed, serial is installed as pyserial))
import serial.tools.list_ports
import serial
import re
import csv
from numpy import asarray
from numpy import savetxt
import numpy as np



#get serial port
port_names = []
ports = list(serial.tools.list_ports.comports())
for p in ports:
    port_names.append(p.name)

ser1 = serial.Serial(port_names[0])
ser2 = serial.Serial(port_names[1])

#get data file name
print('Enter Data file name (please use .csv ending):')
data_file = input()

#create serial port

values = [0,0,0,0,0,0,0,0,0,0,0,0]
data = np.zeros([1,12])

while True:
    #read serial data and strip it of it new line endigs
    newData1 = ser1.readline().strip()
    newData2 = ser2.readline().strip()
    #translate form bytes to stings
    text1 = newData1.decode('UTF-8')
    text2 = newData2.decode('UTF-8')
    #if end command is read break from look
    if(text1 == 'end' or text2== 'end'):
       break
    #split text array into indevidual values along the comas
    formatedData1 = re.split(',',text1)
    formatedData2 = re.split(',',text2)
    
    

    #enter the data into the array
    for i in range(len(formatedData1)):
        values[i] = float(formatedData1[i].strip())
    for i in range(len(formatedData2)):
        values[i+6] = float(formatedData2[i].strip())
    #format time into seconds
    time1 = float(formatedData1[5].strip())/1000.0
    time2 = float(formatedData2[5].strip())/1000.0
    #update scatter plots
    print(values)
    values[5] = time1
    values[11] = time2
   
    #updtate total data array
    temp = np.asarray(values)
    data = np.vstack([data, temp])
    
print('end')
#create CSV file
savetxt(data_file, data, delimiter=',')


