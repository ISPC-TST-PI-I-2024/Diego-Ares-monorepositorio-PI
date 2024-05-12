from machine import Pin, ADC, PWM
import time

# Configurar el pin ADC para leer el potenciómetro
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)  # Configurar la atenuación para el rango completo de 0-3.3V

# Configurar el pin PWM para controlar el LED
led = PWM(Pin(25), freq=5000)  # Usar una frecuencia de 5000 Hz

while True:
    pot_value = pot.read()  # Leer el valor analógico (0-4095)
   
    # Convertir el valor del potenciómetro a un duty cycle de PWM (0-1023)
    pwm_value = int((pot_value / 4095.0) * 1023)
    
    led.duty(pwm_value)  # Ajustar la intensidad del LED
    
    time.sleep(0.1)  # Pequeña pausa para dar estabilidad a la lectura