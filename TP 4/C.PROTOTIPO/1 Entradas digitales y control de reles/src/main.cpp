#include <Arduino.h>

#define boton1Pin 2 // Pin para el primer botón
#define boton2Pin 3 // Pin para el segundo botón

#define rele1Pin 4 // Pin para el primer relé
#define rele2Pin 5 // Pin para el segundo relé

bool estadoBoton1Anterior = HIGH; // Estado anterior del primer botón
bool estadoBoton2Anterior = HIGH; // Estado anterior del segundo botón

void setup() {
  Serial.begin(9600); // Iniciar comunicación serial
  pinMode(boton1Pin, INPUT_PULLUP); // Configurar el pin del botón 1 como entrada con pull-up
  pinMode(boton2Pin, INPUT_PULLUP); // Configurar el pin del botón 2 como entrada con pull-up
  pinMode(rele1Pin, OUTPUT); // Configurar el pin del primer relé como salida
  pinMode(rele2Pin, OUTPUT); // Configurar el pin del segundo relé como salida
}

void loop() {
  // Leer el estado de los botones
  bool estadoBoton1 = digitalRead(boton1Pin);
  bool estadoBoton2 = digitalRead(boton2Pin);
  // Si el estado del botón 1 ha cambiado
  if (estadoBoton1 != estadoBoton1Anterior) {
    if (estadoBoton1 == LOW) {
      // Encender el relé 1
      
      digitalWri {
digitalWrite(rele1Pin, HIGH);
      Serial.println("Relé 1 activado");
    } else {
      // Apagar el relé 1
      digitalWrite(rele1Pin, LOW);
      Serial.println("Relé 1 desactivado");
    }
    estadoBoton1Anterior = estadoBoton1; // Actualizar el estado anterior del botón 1
  }
  // Si el estado del botón 2 ha cambiado
  if (estadoBoton2 != estadoBoton2Anterior) {
    if (estadoBoton2 == LOW) {
      // Encender el relé 2
      digitalWrite(rele2Pin, HIGH);
      Serial.println("Relé 2 activado");
    } else {
      // Apagar el relé 2
      digitalWrite(rele2Pin, LOW);
      Serial.println("Relé 2 desactivado");
    }
    estadoBoton2Anterior = estadoBoton2; 
    }
    estadoB
// Actualizar el estado anterior del botón 2
  }
}