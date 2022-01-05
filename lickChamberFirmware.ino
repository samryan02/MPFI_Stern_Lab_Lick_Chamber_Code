/*
Samuel Breslin
MPFI Mechanical Workshop Core
MPFI Fitzpatick Lab
*/

#include "PinChangeInterrupt.h"

volatile int channel_1_past = 0;
volatile int channel_2_past = 0;
volatile int channel_3_past = 0;
volatile int channel_4_past = 0;
volatile int channel_5_past = 0;
volatile int channel_6_past = 0;
volatile int channel_7_past = 0;
volatile int channel_8_past = 0;
volatile int channel_9_past = 0;
volatile int channel_10_past = 0;

int double_lick_threshold = 50;

int packetNumber = 0;
int values[11] = {packetNumber, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), channel_1, FALLING);
  attachInterrupt(digitalPinToInterrupt(3), channel_2, FALLING);
  attachInterrupt(digitalPinToInterrupt(18), channel_3, FALLING);
  attachInterrupt(digitalPinToInterrupt(19), channel_4, FALLING);
  attachPCINT(digitalPinToPCINT(13), channel_5, CHANGE);
  attachPCINT(digitalPinToPCINT(12), channel_6, CHANGE);
  attachPCINT(digitalPinToPCINT(11), channel_7, CHANGE);
  attachPCINT(digitalPinToPCINT(10), channel_8, CHANGE);
  attachPCINT(digitalPinToPCINT(A8), channel_9, CHANGE);
  attachPCINT(digitalPinToPCINT(A9), channel_10, CHANGE);
  Serial.println("start");
  
}

void loop() {
  packetNumber++;
  Serial.print(packetNumber);
  Serial.print(", ");
    
  for(int i = 1; i< 11; i++){
      
    Serial.print(values[i]);
    Serial.print(", ");
        
  }
    
  Serial.print(millis());
  Serial.println();
  delay(200);
}

void channel_1(){
  if(millis() - channel_1_past > double_lick_threshold) { 
    values[1]++;
    channel_1_past = millis();
  }
}
void channel_2(){
  if(millis() - channel_2_past > double_lick_threshold) {
    values[2]++;
    channel_2_past = millis();
  }
}
void channel_3(){
  if(millis() - channel_3_past > double_lick_threshold) { 
    values[3]++;
    channel_3_past = millis();
  }
}
void channel_4(){
  if(millis() - channel_4_past > double_lick_threshold) {
    values[4]++;
    channel_4_past = millis();
  }
}
void channel_5(){
  if(millis() - channel_5_past > double_lick_threshold) {
    values[5]++;
    channel_5_past = millis();
  }
}
void channel_6(){
  if(millis() - channel_6_past > double_lick_threshold) {
    values[6]++;
    channel_6_past = millis();
  }
}
void channel_7(){
  if(millis() - channel_7_past > double_lick_threshold) {
    values[7]++;
    channel_7_past = millis();
  }
}
void channel_8(){
  if(millis() - channel_8_past > double_lick_threshold) {
    values[8]++;
    channel_8_past = millis();
  }
}
void channel_9(){
  if(millis() - channel_9_past > double_lick_threshold) {
    values[9]++;
    channel_9_past = millis();
  }
}
void channel_10(){
  if(millis() - channel_10_past > double_lick_threshold) {
    values[10]++;
    channel_10_past = millis();
  }
}