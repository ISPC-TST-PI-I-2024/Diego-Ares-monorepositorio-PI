#include <Arduino.h>

#define puls 36
#define led 18

bool touch = 0;
// Definir los pines de los LEDs
int leds[] = {5, 23, 21}; // Cambiar los números de los pines según el esquemático del circuito

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
  // Configurar los pines de los LEDs como salida
  for (int i = 0; i < 3; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {
  touch = digitalRead(puls);
  if (touch == LOW) {
    // Encender los LEDs del led1 al led3 de forma sucesiva
    for (int i = 0; i < 3; i++) {
      digitalWrite(leds[i], HIGH);
      Serial.print("Led ");
      Serial.print(i + 1);
      Serial.println(" encendido");
      delay(500); // Esperar 500 ms
      digitalWrite(leds[i], LOW);
    }
  } else {
    digitalWrite(led, LOW);
    Serial.println("apagado");
    delay(500);
  }
}
