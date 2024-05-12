#include <Arduino.h>


#define puls 36
#define led 18

#define SW1_1 21
#define SW1_2 22
#define SW1_3 23

bool touch = 0;
int velocidad = 500; // Velocidad predeterminada

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
  pinMode(SW1_1, INPUT_PULLUP);
  pinMode(SW1_2, INPUT_PULLUP);
  pinMode(SW1_3, INPUT_PULLUP);
}

void loop() {
  // Leer el estado de los dip switches
  bool switch1 = digitalRead(SW1_1);
  bool switch2 = digitalRead(SW1_2);
  bool switch3 = digitalRead(SW1_3);
  // Determinar la velocidad según el estado de los dip switches
  if (!switch1 && !switch2 && !switch3) {
    velocidad = 1000; // Todos los switches apagados
  } else if (!switch1 && !switch2 && switch3) {
    velocidad = 500; // Solo SW1.3 encendido
  } else if (!switch1 && switch2 && !switch3) {
    velocidad = 250; // Solo SW1.2 encendido
  } else if (!switch1 && switch2 && switch3) {
    velocidad = 100; // SW1.2 y SW1.3 encendidos
  } else if (switch1 && !switch2 && !switch3) {
    velocidad = 750; // Solo SW1.1 encendido
  } // Puedes agregar más casos según tu necesidad
  // Leer el estado del botón
  touch = digitalRead(puls);
  if (touch == LOW) {
    digitalWrite(led, HIGH);
    Serial.println("prendido");
    delay(velocidad); // Usar la velocidad determinada por los dip switches
  } else {
    digitalWrite(led, LOW);
    Serial.println("apagado");
    delay(velocidad); // Usar la velocidad determinada por los dip switches
  }
}
