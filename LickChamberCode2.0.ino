int count  = 0;
volatile int past = 0;
volatile int past2 = 0;
uint8_t checksum1 = 0;
uint8_t checksum2 = 0;
unsigned int values[6] = {0,0,0,0,0,0};
byte ser_send_buff[100];
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), test, FALLING);
  attachInterrupt(digitalPinToInterrupt(3), test2, FALLING);
  ser_send_buff[1] = 0xC;
}

void loop() {
  sendSerialPacket(ser_send_buff);
}

void test(){
  if(millis() - past > 50) { 
    values[0]++;
    past = millis();
  }
}
void test2(){
  if(millis() - past2 > 50) {
    values[1]++;
    past2 = millis();
  }
}
void sendSerialPacket(uint8_t send_buff[]){
    dataEntry();
    Serial.write(255); //send header 255
    Serial.write(send_buff[1]); //send data length
    for(int i=0;i<send_buff[1];i++){
        Serial.write(send_buff[i+2]); //send data bytes
    }
    
 
}

void dataEntry(){
  for(int i = 0; i<6; i++){
    ser_send_buff[(i*2)+2] = lowByte(values[i]);
    ser_send_buff[(i*2)+3] = highByte(values[i]);
  }

}
