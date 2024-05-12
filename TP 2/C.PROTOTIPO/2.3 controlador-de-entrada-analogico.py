from machine import Pin, ADC
import time

# Configura el pin analógico (modificar según sea necesario)
sensorPin = ADC(Pin(34))  # Use ADC1 (Pins 32, 33, 34, 35, 36, 39)
sensorPin.atten(ADC.ATTN_11DB)  # Configura la atenuación para el rango de voltaje completo (0-3.3V en ESP32)

def leer_temperatura(sensor):
    # Lee el valor del sensor y lo convierte a voltaje
    valor = sensor.read()
    voltaje = valor * 3.3 / 4095
    
    # Convertir el voltaje a temperatura
    # Para LM35, cada grado Celsius equivale a 10mV.
    temperatura = voltaje * 100
    return temperatura

while True:
    temperatura = leer_temperatura(sensorPin)
    print("Temperatura: {:.2f} ºC".format(temperatura))
    time.sleep(1)  # Espera un segundo antes de la próxima lectura