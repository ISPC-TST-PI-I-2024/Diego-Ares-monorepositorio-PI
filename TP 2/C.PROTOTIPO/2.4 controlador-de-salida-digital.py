from machine import Pin
import time

# Configurar los pines de los LEDs como salida
led1 = Pin(pinX, Pin.OUT)
led2 = Pin(pinY, Pin.OUT)

# Función para alternar los LEDs
def toggle_leds(interval):
    while True:
        led1.value(1)
        led2.value(0)
        time.sleep(interval)
        led1.value(0)
        led2.value(1)
        time.sleep(interval)

# Llamar a la función toggle_leds con un intervalo de tiempo en segundos
toggle_leds(1)  # Puedes cambiar el intervalo según necesites