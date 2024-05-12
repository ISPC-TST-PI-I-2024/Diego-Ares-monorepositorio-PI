#include <Arduino.h>

#define puls 36
#define led 18

// Definir los pines de los interruptores y los LEDs
#define sw1_1 21
#define sw1_2 22
#define sw1_3 23
#define sw1_4 24

#define led1 5
#define led2 6
#define led3 7
#define led4 8
#define led5 9
#define led6 10
#define led7 11
#define led8 12

bool touch = 0;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
  // Configurar los pines de los interruptores como entrada
  pinMode(sw1_1, INPUT_PULLUP);
  pinMode(sw1_2, INPUT_PULLUP);
  pinMode(sw1_3, INPUT_PULLUP);
  pinMode(sw1_4, INPUT_PULLUP);
}

void loop() {
  // Leer el estado de los interruptores
  bool sw1_1_state = digitalRead(sw1_1);
  bool sw1_2_state = digitalRead(sw1_2);
  bool sw1_3_state = digitalRead(sw1_3);
  bool sw1_4_state = digitalRead(sw1_4)
  // Determinar el patrón de parpadeo según la combinación de estados de los interruptores
  int pattern = 0;
  if (!sw1_1_state) pattern += 1;
  if (!sw1_2_state) pattern += 2;
  if (!sw1_3_state) pattern += 4;
  if (!sw1_4_state) pattern += 8
  // Aplicar el patrón de parpadeo
  applyPattern(pattern);
  // Otros procesos del programa
}

void applyPattern(int pattern) {
  // Aplicar el patrón de parpadeo según el valor de 'pattern'
  switch(pattern) {
    case 0:
      // Patrón por defecto (todos los LEDs apagados)
      turnOffAllLEDs();
      break;
    case 1:
      // Patrón para la combinación 0001 (parpadeo rápido)
      blinkAllLEDs(100);
      break;
    case 2:
      // Patrón para la combinación 0010 (parpadeo lento)
      blinkAllLEDs(500);
      break;
    // Agregar más casos para otras combinaciones de interruptores según sea necesario
    default:
      // En caso de una combinación no definida, apagar todos los LEDs
      turnOffAllLEDs();
  }
}

void turnOffAllLEDs() {
  // Apagar todos los LEDs
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led5, LOW);
  digitalWrite(led6, LOW);
  digitalWrite(led7, LOW);
  digitalWrite(led8, LOW);
}

void blinkAllLEDs(int interval) {
  // Parpadeo de todos los LEDs con el intervalo especificado
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, HIGH);
  digitalWrite(led5, HIGH);
  digitalWrite(led6, HIGH);
  digitalWrite(led7, HIGH);
  digitalWrite(led8, HIGH);
  delay(interval);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led5, LOW);
  digitalWrite(led6, LOW);
  digitalWrite(led7, LOW);
  digitalWrite(led8, LOW);
  delay(interval);
}
