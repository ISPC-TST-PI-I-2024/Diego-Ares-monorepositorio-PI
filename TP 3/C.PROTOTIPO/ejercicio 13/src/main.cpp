#include <Arduino.h>

#define btnPin 36
#define ledPin1 18
#define ledPin2 19
#define ledPin3 21
#define ledPin4 22

int contador = 0;
bool ultimoEstado = HIGH;
bool estadoActual;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(btnPin, INPUT_PULLUP);
}

void loop() {
  estadoActual = digitalRead(btnPin);
  if (estadoActual == LOW && ultimoEstado == HIGH) {
    // Incrementar el contador solo si el botón ha sido presionado
    contador++;
    actualizarLEDs(contador);
    Serial.print("Contador: ");
    Serial.println(contador);
  }
  ultimoEstado = estadoActual;
}

void actualizarLEDs(int contador) {
  digitalWrite(ledPin1, contador >= 1 ? HIGH : LOW);
  digitalWrite(ledPin2, contador >= 2 ? HIGH : LOW);
  digitalWrite(ledPin3, contador >= 3 ? HIGH : LOW);
  digitalWrite(ledPin4, contador >= 4 ? HIGH : LOW);
}