#include <Arduino.h>

#define puls 36
#define led1 18

bool touch = 0;
bool ledState = LOW; // Estado inicial del LED apagado

void setup() {
  Serial.begin(115200);
  pinMode(led1, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
}

void loop() {
  touch = digitalRead(puls);
  // Si se detecta un cambio en el estado del botón
  if (touch != ledState) {
    // Cambiar el estado del LED
    ledState = !ledState;
    // Si el estado del LED es alto, encenderlo y enviar mensaje
    if (ledState == HIGH) {
      digitalWrite(led1, HIGH);
      Serial.println("LED encendido");
    } else { // Si el estado del LED es bajo, apagarlo y enviar mensaje
      digitalWrite(led1, LOW);
      Serial.println("LED apagado");
    }
    delay(200); // Retardo para evitar rebotes del botón
  }
}
