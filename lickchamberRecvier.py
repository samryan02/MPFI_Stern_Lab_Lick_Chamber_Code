import serial
import re

ser = serial.Serial("COM4")
values = [0,0,0,0]
while True:
    newData = ser.readline().strip('/n/l')
    print(newData)
    formatedData = re.split(':',newData)
    if(formatedData[0] == "channel 1"){
        values[0] = formatedData[1]
    }
    if(formatedData[0] == "channel 2"){
        values[1] = formatedData[1]
    }
    if(formatedData[0] == "channel 3"){
        values[2] = formatedData[1]
    }
    if(formatedData[0] == "channel 4"){
        values[3] = formatedData[1]
    }
