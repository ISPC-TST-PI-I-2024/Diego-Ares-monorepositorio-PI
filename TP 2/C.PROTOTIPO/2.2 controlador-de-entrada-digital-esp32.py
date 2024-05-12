from machine import Pin
import time

# Definir los pines para el botón y el LED
button_pin = 14   # Pin donde está conectado el botón (GPIO14 en ESP32)
led_pin = 15      # Pin donde está conectado el LED (GPIO15 en ESP32)

# Configurar el pin del botón como entrada
button = Pin(button_pin, Pin.IN)
# Configurar el pin del LED como salida
led = Pin(led_pin, Pin.OUT)

while True:
    # Leer el estado del botón
    button_state = button.value()

    # Si el botón está presionado (estado bajo), encender el LED
    if button_state == 0:
        led.value(1)
    else:
        # De lo contrario, apagar el LED
        led.value(0)
    
    # Esperar un corto tiempo para evitar la saturación del procesador
    time.sleep(0.1)