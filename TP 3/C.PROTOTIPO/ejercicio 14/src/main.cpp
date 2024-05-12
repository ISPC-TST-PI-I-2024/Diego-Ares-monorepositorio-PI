#include <Arduino.h>

#define puls 36
#define led 18


int password[] = {1, 2, 3}; // Esta es la secuencia de pulsaciones correcta
int passwordIndex = 0; // Esta variable llevará la cuenta de en qué parte de la secuencia de la contraseña estamos

void setup() {
pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(btn3, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT)
}

void loop()  {
if (digitalRead(btn1) == LOW) {
    checkButtonPress(1);
  }
  if (digitalRead(btn2) == LOW) {
    checkButtonPress(2);
  }
  if (digitalRead(btn3) == LOW) {
    checkButtonPress(3);
  }
}

void checkButtonPress(int button) {
  if (button == password[passwordIndex]) {
    passwordIndex++;
    if (passwordIndex == sizeof(password) / sizeof(password[0])) {
      // Se ha ingresado la contraseña correctamente
      digitalWrite(led1, HIGH);
      passwordIndex = 0; // Reinicia el índice de la contraseña para la próxima vez
    }
  } else {
    // Se ha ingresado una pulsación incorrecta
    digitalWrite(led2, HIGH);
    delay(1000); // Tiempo de espera antes de apagar el led2
    digitalWrite(led2, LOW);
    passwordIndex = 0; // Reinicia el índice de la contraseña
  }
}
