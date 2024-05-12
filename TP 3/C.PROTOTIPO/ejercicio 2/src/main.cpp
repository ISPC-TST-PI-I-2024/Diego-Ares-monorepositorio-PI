#include <Arduino.h>

#define puls 36
#define led 18

bool touch = 0;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
}

void loop() {
  touch = digitalRead(puls);
  if (touch == LOW) {
    // Enciende el LED1
    digitalWrite(led, HIGH);
    Serial.println("prendido");
    delay(500); // Espera medio segundo
    // Apaga el LED1
    digitalWrite(led, LOW);
    delay(500); // Espera medio segundo
  } else {
    digitalWrite(led, LOW);
    Serial.println("apagado");
    delay(500); // Espera medio segundo
  }
}

