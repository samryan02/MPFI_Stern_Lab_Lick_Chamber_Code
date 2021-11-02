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

unsigned int values[4] = {0,0,0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(2), channel_1, FALLING);
  attachInterrupt(digitalPinToInterrupt(3), channel_2, FALLING);
  attachInterrupt(digitalPinToInterrupt(18), channel_3, FALLING);
  attachInterrupt(digitalPinToInterrupt(19), channel_4, FALLING);
  while(millis()< 18000000){
    Serial.print("Channel One Licks: ");
    Serial.println(values[0]);
    Serial.print("Channel two Licks: ");
    Serial.println(values[1]);
    Serial.print("Channel three licks: ");
    Serial.println(values[2]);
    Serial.print("Channel four licks:");
    Serial.println(values[3]);
    Serial.print("time since count began: ");
    Serial.println(millis()/1000.0);
  }
}

void loop() {
  
}

void channel_1(){
  if(millis() - channel_1_past > double_lick_threshold) { 
    values[0]++;
    channel_1_past = millis();
  }
}
void channel_2(){
  if(millis() - channel_2_past > double_lick_threshold) {
    values[1]++;
    channel_2_past = millis();
  }
}
void channel_3(){
  if(millis() - channel_3_past > double_lick_threshold) { 
    values[0]++;
    channel_3_past = millis();
  }
}
void channel_4(){
  if(millis() - channel_4_past > double_lick_threshold) {
    values[1]++;
    channel_4_past = millis();
  }
}
