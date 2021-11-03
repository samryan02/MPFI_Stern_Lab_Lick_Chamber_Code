import matplotlib.pyplot as plt
import serial
import re
import csv
from numpy import asarray
from numpy import savetxt
import numpy as np

plt.axis([0, 18000000, 0, 32000])

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
    
    newData = ser.readline().strip()
    text = newData.decode('UTF-8')
    if(text == 'end'):
       break
    formatedData = re.split(',',text)
    
    for i in range(len(formatedData)):
        values[i] = float(formatedData[i].strip())
    time = float(formatedData[5].strip())/1000.0
    axs[0, 0].scatter(time, values[1])
    axs[0, 1].scatter(time, values[2])
    axs[1, 0].scatter(time, values[3])
    axs[1, 1].scatter(time, values[4])  
   
    plt.pause(.1)
    
    temp = np.asarray(values)
    data = np.vstack([data, temp])
    
print('end')

savetxt('data.csv', data, delimiter=',')


