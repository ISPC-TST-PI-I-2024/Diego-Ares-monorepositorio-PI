#include <Arduino.h>


#define led1 18

void setup() {
  pinMode(led1, OUTPUT);// Configura el pin GPIO18 como salida
}

void loop() {
    digitalWrite(led1, HIGH);// Enciende el LED conectado al pin GPIO18 
}
