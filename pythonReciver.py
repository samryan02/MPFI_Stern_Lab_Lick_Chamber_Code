#imports(only numpy, matplot lib, and serial must be installed, serial is installed as pyserial))
import matplotlib.pyplot as plt
import serial
import re
import csv
from numpy import asarray
from numpy import savetxt
import numpy as np

#iniitalize plots
fig, axs = plt.subplots(2, 2)

axs[0, 0].set_title('Channel 1')
axs[0, 1].set_title('Channel 2')
axs[1, 0].set_title('Channel 3')
axs[1, 1].set_title('Channel 4')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
ser = serial.Serial("COM3")
values = [0,0,0,0,0,0]
data = np.zeros([1,6])

while True:
    #read serial data and strip it of it new line endigs
    newData = ser.readline().strip()
    #translate form bytes to stings
    text = newData.decode('UTF-8')
    #if end command is read break from look
    if(text == 'end'):
       break
    #split text array into indevidual values along the comas
    formatedData = re.split(',',text)

    #enter the data into the array
    for i in range(len(formatedData)):
        values[i] = float(formatedData[i].strip())
    #format time into seconds
    time = float(formatedData[5].strip())/1000.0
    #update scatter plots
    axs[0, 0].scatter(time, values[1])
    axs[0, 1].scatter(time, values[2])
    axs[1, 0].scatter(time, values[3])
    axs[1, 1].scatter(time, values[4])  
   
    plt.pause(.1)
    #updtate total data array
    temp = np.asarray(values)
    data = np.vstack([data, temp])
    
print('end')
#create CSV file
savetxt('data.csv', data, delimiter=',')


