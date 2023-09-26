#Fermin Covarrubias Ramos
#7K Sistemas Inteligentes
#Project 14 : Sending the Raspberry Pi Pico internal temperature to an Arduino Uno

from machine import ADC, UART
import utime

adc = ADC(4)  # Canal 4 del ADC para el sensor de temperatura interno del Raspberry Pi Pico

conv = 3.3 / 65535

uart = UART(0, 9600)

while True:
    v = adc.read_u16()
    v = v * conv
    temp = 27 - (v - 0.706) / 0.001721
    temp_str = "{:.2f}".format(temp)
    uart.write(temp_str + " grados Celsius\n")
    utime.sleep(10)
