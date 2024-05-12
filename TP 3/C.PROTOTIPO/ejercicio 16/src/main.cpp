#include <Arduino.h>

#define led1 18
#define led2 19
#define led3 20
// Define aquí el resto de los pines para los LEDs según tu circuito

void setup() {
  Serial.begin(115200);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  // Configura aquí el resto de los pines de los LEDs como salida
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    ejecutarComando(comando);
  }
}

void ejecutarComando(char comando) {
  switch(comando) {
    case '1':
      digitalWrite(led1, HIGH);
      Serial.println("Led 1 encendido");
      break;
    case '2':
      digitalWrite(led1, LOW);
      Serial.println("Led 1 apagado");
      break;
    case '3':
      digitalWrite(led2, HIGH);
      Serial.println("Led 2 encendido");
      break;
    case '4':
      digitalWrite(led2, LOW);
      Serial.println("Led 2 apagado");
      break;
    case '5':
      digitalWrite(led3, HIGH);
      Serial.println("Led 3 encendido");
      break;
    case '6':
      digitalWrite(led3, LOW);
      Serial.println("Led 3 apagado");
      break;
    // Agrega más casos según la cantidad de LEDs que tengas y sus respectivos pines
    default:
      Serial.println("Comando no reconocido");
  }
}

