#include <Arduino.h>

#define puls 36
#define led 18

#define SW1_PIN_1 28
#define SW1_PIN_2 29
#define SW1_PIN_3 30
#define SW1_PIN_4 31

bool touch = 0;
bool lastState[4] = {0}; // Almacena el último estado de los switches
bool ledState[8] = {0};  // Almacena el estado de los LEDs
unsigned long previousMillis = 0;
const long interval = 500;

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(puls, INPUT_PULLUP);
  // Configurar los pines de los switches como entradas
  pinMode(SW1_PIN_1, INPUT_PULLUP);
  pinMode(SW1_PIN_2, INPUT_PULLUP);
  pinMode(SW1_PIN_3, INPUT_PULLUP);
  pinMode(SW1_PIN_4, INPUT_PULLUP);
}

void loop() {
  // Leer el estado de los switches
  bool currentState[4] = {digitalRead(SW1_PIN_1), digitalRead(SW1_PIN_2), digitalRead(SW1_PIN_3), digitalRead(SW1_PIN_4)};
  // Comprobar si el estado de los switches ha cambiado
  bool stateChanged = false;
  for (int i = 0; i < 4; i++) {
    if (currentState[i] != lastState[i]) {
      stateChanged = true;
      break;
    }
  }
  // Si el estado de los switches ha cambiado, actualizar el patrón de LEDs
  if (stateChanged) {
    updateLEDState(currentState);
    for (int i = 0; i < 4; i++) {
      lastState[i] = currentState[i];
    }
  }
  // Parpadear los LEDs basado en el patrón actual
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    toggleLEDs();
  }
  // Leer el estado del pulsador y encender o apagar el LED
  touch = digitalRead(puls);
  if (touch == LOW) {
    digitalWrite(led, HIGH);
    Serial.println("prendido");
  } else {
    digitalWrite(led, LOW);
    Serial.println("apagado");
  }
}

void updateLEDState(bool currentState[]) {
  // Lógica para actualizar el estado de los LEDs basado en el estado de los switches
  // Aquí puedes definir diferentes patrones de parpadeo para cada combinación de estados de los switches
  // Por ejemplo, puedes usar un arreglo booleano para representar si cada LED debe estar encendido o apagado
  // y actualizar este arreglo según los estados de los switches
  // A continuación, se muestra un ejemplo simple:
  // Si sw1.1 está activo, encender led1
  ledState[0] = currentState[0];
  // Si sw1.2 está activo, encender led2
  ledState[1] = currentState[1];
  // Si sw1.3 está activo, encender led3
  ledState[2] = currentState[2];
  // Si sw1.4 está activo, encender led4
  ledState[3] = currentState[3];
  // El resto de los LEDs se pueden configurar según tus requerimientos
}
void toggleLEDs() {
  // Función para cambiar el estado de los LEDs según el patrón actual
  // Aquí puedes utilizar el arreglo ledState para controlar el estado de cada LED
  // Por ejemplo, puedes usar digitalWrite para encender o apagar cada LED según el valor correspondiente en ledState
  // Esta función se llama periódicamente para actualizar el estado de los LEDs
  // A continuación, se muestra un ejemplo simple:
  for (int i = 0; i < 8; i++) {
    digitalWrite(led + i, ledState[i] ? HIGH : LOW);
  }
}

