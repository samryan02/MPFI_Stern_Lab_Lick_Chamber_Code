/*
Samuel Breslin
MPFI Mechanical Workshop Core
MPFI Fitzpatick Lab
*/

volatile int channel_1_past = 0;
volatile int channel_2_past = 0;
volatile int channel_3_past = 0;
volatile int channel_4_past = 0;

int double_lick_threshold = 50;



int packetNumber = 0;
int values[5] = {packetNumber, 0, 0, 0, 0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), channel_1, FALLING);
  attachInterrupt(digitalPinToInterrupt(3), channel_2, FALLING);
  attachInterrupt(digitalPinToInterrupt(18), channel_3, FALLING);
  attachInterrupt(digitalPinToInterrupt(19), channel_4, FALLING);
  while(millis()< 18000000){
    
    packetNumber++;
    Serial.print(packetNumber);
    Serial.print(", ");
    
    for(int i = 1; i< 5; i++){
      
      Serial.print(values[i]);
      Serial.print(", ");
        
    }
    
    Serial.print(millis());
    Serial.println();
    delay(200);
  }
}

void loop() {
  
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