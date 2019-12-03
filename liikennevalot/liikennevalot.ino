#include "Adafruit_Sensor.h"
#include "Adafruit_AM2320.h"
Adafruit_AM2320 am2320 = Adafruit_AM2320();

int vihrea = 8,
    keltainen = 4,
    punainen = 2;
    
void setup() {
  Serial.begin(9600);
  pinMode(vihrea, OUTPUT);
  pinMode(keltainen, OUTPUT);
  pinMode(punainen, OUTPUT);

  //odottelee, että portti on auki
  while (!Serial) {
    delay(10);
  }
  am2320.begin();
}

void loop() {
  vihreavalo();
  lampokosteus();
  delay(5000);

  keltainenvalo();
  lampokosteus();
  delay(5000);

  punainenvalo();
  lampokosteus();
  delay(5000);
}

void vihreavalo() {
  digitalWrite(vihrea, HIGH);
  digitalWrite(keltainen, LOW);
  digitalWrite(punainen, LOW);
  Serial.println("Vihrea");
}

void keltainenvalo() {
  digitalWrite(vihrea, LOW);
  digitalWrite(keltainen, HIGH);
  digitalWrite(punainen, LOW);
  Serial.println("Keltainen");
}

void punainenvalo() {
  digitalWrite(vihrea, LOW);
  digitalWrite(keltainen, LOW);
  digitalWrite(punainen, HIGH);
  Serial.println("Punainen");
}

void lampokosteus() {
  Serial.print("I: "); 
  Serial.print(am2320.readTemperature());
  Serial.print(",");
  Serial.print(am2320.readHumidity());
}
