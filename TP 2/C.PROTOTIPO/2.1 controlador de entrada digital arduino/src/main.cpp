#include <Arduino.h>

// Definir los pines para el botón y el LED
const int buttonPin = 2; // Pin donde está conectado el botón
const int ledPin = 13;   // Pin donde está conectado el LED

void setup() {
  // Configurar el pin del botón como entrada
  pinMode(buttonPin, INPUT);
  // Configurar el pin del LED como salida
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Leer el estado del botón
  int buttonState = digitalRead(buttonPin);

  // Si el botón está presionado (estado bajo), encender el LED
  if (buttonState == LOW) {
    digitalWrite(ledPin, HIGH);
  } else {
    // De lo contrario, apagar el LED
    digitalWrite(ledPin, LOW);
  }
}
