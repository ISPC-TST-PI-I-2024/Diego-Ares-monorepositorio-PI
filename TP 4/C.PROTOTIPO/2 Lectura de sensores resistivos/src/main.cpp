#include <Arduino.h>

// Definir los pines de los botones y los relés
const int pinBoton1 = 2;
const int pinBoton2 = 3;
const int pinRele1 = 4;
const int pinRele2 = 5;

void setup() {
  // Inicializar los pines de los botones como entradas
  pinMode(pinBoton1, INPUT_PULLUP);
  pinMode(pinBoton2, INPUT_PULLUP);
  // Inicializar los pines de los relés como salidas
  pinMode(pinRele1, OUTPUT);
  pinMode(pinRele2, OUTPUT);
  // Iniciar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Leer el estado de los botones
  bool estadoBoton1 = digitalRead(pinBoton1);
  bool estadoBoton2 = digitalRead(pinBoton2);
  // Si se presiona el botón 1, activar el relé 1
  if (!estadoBoton1) {
    digitalWrite(pinRele1, HIGH);
    Serial.println("Relé 1 activado");
  } else {
    digitalWrite(pinRele1, LOW);
  }
  // Si se presiona el botón 2, activar el relé 2
  if (!estadoBoton2) {
    digitalWrite(pinRele2, HIGH);
    Serial.println("Relé 2 activado");
  } else {
    digitalWrite(pinRele2, LOW);
  }
  // Pequeña pausa para evitar rebotes en los botones
  delay(50);
}