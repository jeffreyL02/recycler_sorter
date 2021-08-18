#include <Servo.h>

#define ON_LED_PIN 9
#define STOP_LED_PIN 8
#define BARRIER_PIN 2
#define RELEASE_PIN 3
#define COKE_PIN 4
#define SPRITE_PIN 5
#define FANTA_PIN 6
#define BUTTON_PIN 7

Servo barrierGate;
Servo releaseGate;
Servo cokeRamp;
Servo spriteRamp;
Servo fantaRamp;

int buttonState = 0;

void resetSys(){
  digitalWrite(ON_LED_PIN, LOW);
  digitalWrite(STOP_LED_PIN,  HIGH);

  barrierGate.write(0);
  releaseGate.write(90); 
  cokeRamp.write(90); 
  spriteRamp.write(90); 
  fantaRamp.write(90); 
}

void setup() {
  Serial.begin(9600);

  pinMode(ON_LED_PIN, OUTPUT);
  pinMode(STOP_LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT);
  
  barrierGate.attach(BARRIER_PIN);
  releaseGate.attach(RELEASE_PIN);
  cokeRamp.attach(COKE_PIN);
  spriteRamp.attach(SPRITE_PIN);
  fantaRamp.attach(FANTA_PIN);

  resetSys();
}

void loop() {
  if(!buttonState){
    buttonState = digitalRead(BUTTON_PIN);
    while(!buttonState){
      buttonState = digitalRead(BUTTON_PIN);
    }
    Serial.println(buttonState); // SEND COMMAND TO START MACHINE
    /* LED change */ 
    digitalWrite(ON_LED_PIN, HIGH);
    digitalWrite(STOP_LED_PIN, LOW);
  }

  /* Drop a bottle */
  for(int pos = 0; pos <= 70; pos += 1.5){
    barrierGate.write(pos);
    delay(2.6);
  }
  for(int pos = 70; pos >= 0; pos -= 1){
    barrierGate.write(pos);
    delay(2);
  }

  Serial.println("DETECT"); // SEND COMMAND TO DETECT OBJ

  while(Serial.available() <= 0){
    // WAIT FOR OBJ REKOG
  }
  String data = Serial.readStringUntil('\n');
  
  for(int pos = 90; pos >= 0; pos -= 1.3){
    releaseGate.write(pos);
    delay(3);
  }
  for(int pos = 0; pos <= 90; pos += 1){
    releaseGate.write(pos);
    delay(3);
  }
  
  if(data == "Coke Can"){
    cokeRamp.write(0);
    delay(4000); 
    cokeRamp.write(90); 
  }
  else if(data == "Coke Bottle"){
    cokeRamp.write(180);
    delay(4000); 
    cokeRamp.write(90); 
  }
  else if(data == "Sprite Can"){
    spriteRamp.write(0);
    delay(4000); 
    spriteRamp.write(90);
  }
  else if(data == "Sprite Bottle"){
    spriteRamp.write(180);
    delay(4000); 
    spriteRamp.write(90);
  }
  else if(data == "Fanta Can"){
    fantaRamp.write(0);
    delay(4000);
    fantaRamp.write(90);
  }
  else if(data == "Fanta Bottle"){
    fantaRamp.write(180);
    delay(4000);
    fantaRamp.write(90);
  }
  else{
    delay(4000);
  }
}
