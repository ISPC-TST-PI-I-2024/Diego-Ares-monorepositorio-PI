#include <Arduino.h>

#define SW1_PIN_START 21 // Pin donde comienzan los dip switches en tu código de conexión
#define LED_PIN_START 4  // Pin donde comienzan los LEDs en tu código de conexión

void setup() {
   Serial.begin(115200);
    pinMode(led, OUTPUT);
    pinMode(puls, INPUT_PULLUP);
    // Configura los pines de los LEDs como salidas
    for (int i = LED_PIN_START; i <= LED_PIN_START + 7; i++) {
        pinMode(i, OUTPUT);
    }
}

void loop() {
   touch = digitalRead(puls);
    if (touch == LOW){
        digitalWrite(led, HIGH);
        Serial.println("prendido");    
        delay(500);
    } else {
        digitalWrite(led, LOW);
        Serial.println("apagado");
        delay(500);
    }
    // Lee el estado de los dip switches y refleja en los LEDs
    for (int i = 1; i <= 8; i++) {
        int switchState = digitalRead(SW1_PIN_START + i - 1);
        digitalWrite(LED_PIN_START + i - 1, switchState);
    }
}
