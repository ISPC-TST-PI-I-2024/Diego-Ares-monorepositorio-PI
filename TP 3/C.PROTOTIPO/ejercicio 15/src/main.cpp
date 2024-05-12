#include <Arduino.h>
#include <Ticker.h>

#define puls 36
#define led 18

bool touch = 0;
Ticker ledTicker;

void setup(){
    Serial.begin(115200);
    pinMode(led, OUTPUT);
    pinMode(puls, INPUT_PULLUP);
    // Configura el temporizador para que llame a la función blinkLed cada 500 ms
    ledTicker.attach(0.5, blinkLed);
}

void loop(){
    touch = digitalRead(puls);
    if (touch == LOW){
        digitalWrite(led, HIGH);
        Serial.println("prendido");
    }else{
        digitalWrite(led, LOW);
        Serial.println("apagado");
    }
}

void blinkLed(){
    static bool ledState = LOW;
    // Invierte el estado del LED cada vez que se llama a esta función
    ledState = !ledState;
    digitalWrite(led, ledState);
}


