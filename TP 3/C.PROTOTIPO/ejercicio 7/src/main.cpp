#include <Arduino.h>

#define puls 36
#define btn1 39  // Botón 1
#define btn2 34  // Botón 2
#define led1 18  // LED 1
#define led2 19  // LED 2

bool touch1 = 0;
bool touch2 = 0;

void setup() {
  Serial.begin(115200);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
}

void loop() {
  // Lectura del estado de los botones
  touch1 = digitalRead(btn1);
  touch2 = digitalRead(btn2);
  // Control del estado de LED 1
  if (touch1 == LOW) {
    digitalWrite(led1, HIGH);
    Serial.println("LED 1 prendido");
  } else {
    digitalWrite(led1, LOW);
    Serial.println("LED 1 apagado");
  }
  // Control del estado de LED 2
  if (touch2 == LOW) {
    digitalWrite(led2, HIGH);
    Serial.println("LED 2 prendido");
  } else {
    digitalWrite(led2, LOW);
    Serial.println("LED 2 apagado");
  }
  delay(500);
}
