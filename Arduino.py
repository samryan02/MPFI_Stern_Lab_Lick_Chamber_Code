import serial
import re

class Arduino():
    
    #class contstructor
    def __init__(self, commport):
        self.arduino = serial.Serial(commport)
        self.values = [0,0,0,0,0,0,0,0,0,0,0,0]

    def sendStartCommand(self):
        self.arduino.write(bytes(b'start'))
    def getFirstByte(self):
        Data1 = self.arduino.readline().strip()
        #print(Data1)
        text = Data1.decode('UTF-8')
        if(text == 'start'):
            return(True)
        else:
            return(False)

    def getData(self):
        try:
            newData1 = self.arduino.readline().strip()
            #print(newData1)
            text = newData1.decode('UTF-8')
            #print(text)

            if(text == 'end'):
                return([0,0,0,0,0,0,0,0,0,0,0,0])
            formatedData1 = re.split(',',text)
            #print(formatedData1)
            for i in range(len(formatedData1)):
                #print(formatedData1[i].strip())
                self.values[i] = float(formatedData1[i].strip())
            #print(formatedData1)
            self.values[11] = int(formatedData1[11].strip())/1000.0
            return(self.values)
        except:
            return([0,0,0,0,0,0,0,0,0,0,0,0])

