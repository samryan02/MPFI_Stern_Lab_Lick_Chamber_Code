#imports(only numpy, matplot lib, and serial must be installed, serial is installed as pyserial))
import matplotlib.pyplot as plt
import serial
import re
import csv
from numpy import asarray
from numpy import savetxt
import numpy as np

#iniitalize plots
fig, axs = plt.subplots(2, 4)

axs[0, 0].set_title('Channel 1')
axs[0, 1].set_title('Channel 2')
axs[0, 2].set_title('Channel 3')
axs[0, 3].set_title('Channel 4')
axs[1, 0].set_title('Channel 5')
axs[1, 1].set_title('Channel 6')
axs[1, 2].set_title('Channel 7')
axs[1, 3].set_title('Channel 8')

#lable axis
for ax in axs.flat:
    ax.set(xlabel='time', ylabel='total number of licks')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

#get serial port
print('Enter First Serial Port:')
serial_port = input()

print('Enter Second Serial Port:')
second_serial_port = input()

#get data file name
print('Enter Data file name (please use .csv ending):')
data_file = input()

#create serial port
ser1 = serial.Serial(serial_port)
ser2 = serial.Serial(second_serial_port)
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
    axs[0, 0].scatter(time1, values[1])
    axs[0, 1].scatter(time1, values[2])
    axs[0, 2].scatter(time1, values[3])
    axs[0, 3].scatter(time1, values[4])
    axs[1, 0].scatter(time2, values[7])
    axs[1, 1].scatter(time2, values[8])
    axs[1, 2].scatter(time2, values[9])
    axs[1, 3].scatter(time2, values[10])  
    values[5] = time1
    values[11] = time2
    plt.pause(.1)
    #updtate total data array
    temp = np.asarray(values)
    data = np.vstack([data, temp])
    
print('end')
#create CSV file
savetxt(data_file, data, delimiter=',')


