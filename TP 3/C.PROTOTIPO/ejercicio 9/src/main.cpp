#include <Arduino.h>

#define led1

int estadoSecuencia = 0; // Estado actual de la secuencia
bool ultimoEstadoBtn1 = HIGH; // Estado previo del botón btn1


void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
}

void loop() {
  bool estadoBtn1 = digitalRead(btn1);
if (estadoBtn1 == LOW && ultimoEstadoBtn1 == HIGH) {
  // El botón btn1 ha sido presionado
  avanzarSecuencia(); // Llama a la función para avanzar la secuencia
}
ultimoEstadoBtn1 = estadoBtn1; // Actualiza el estado previo del botón btn1
}

void avanzarSecuencia() {
  digitalWrite(leds[estadoSecuencia], LOW); // Apaga el LED actual
  estadoSecuencia++; // Avanza al siguiente LED
  if (estadoSecuencia >= numLEDS) {
    estadoSecuencia = 0; // Vuelve al primer LED si se llega al último
  }
  digitalWrite(leds[estadoSecuencia], HIGH); // Enciende el próximo LED
}
