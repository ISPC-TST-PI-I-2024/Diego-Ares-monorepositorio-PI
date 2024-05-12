#include <Arduino.h>

#define puls 36
#define led 18

bool touch = 0;
bool lastState = HIGH;  // Estado anterior del botón
unsigned long lastDebounceTime = 0;  // Último tiempo en que se cambió el estado del botón
unsigned long debounceDelay = 50;  // Tiempo de debounce en milisegundos

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
}

void loop() {
  int reading = digitalRead(puls);
  // Verificar si el estado del botón ha cambiado
  if (reading != lastState) {
    // Resetear el temporizador de debounce
    lastDebounceTime = millis();
  }
  // Comprobar si ha pasado el tiempo de debounce
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // Si ha pasado, actualiza el estado del botón
    if (reading != touch) {
      touch = reading;
      // Si el botón se ha presionado
      if (touch == LOW) {
        digitalWrite(led, HIGH);
        Serial.println("prendido");
      } else {
        digitalWrite(led, LOW);
        Serial.println("apagado");
      }
    }
  }
  // Guardar el estado actual del botón para la próxima iteración
  lastState = reading;
}
