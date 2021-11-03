import matplotlib.pyplot as plt
import serial
import re
import csv
from numpy import asarray
from numpy import savetxt
import numpy as np

plt.axis([0, 18000000, 0, 32000])

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

    plt.scatter(float(formatedData[1].strip()), values[0])  
   
    plt.pause(.1)
    temp = np.asarray(values)
    data = np.vstack([data, temp])
    
print('end')

savetxt('data.csv', data, delimiter=',')


