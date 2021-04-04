# Imports necessary libraries
import machine
import utime

# Creates a value called photo_sensor by reading ADC2 which is Pin 34 on the Raspberry Pi Pico
# The other pin of the photoresistor connects ADC_VREF which is Pin 35 on the Pico
photo_sensor = machine.ADC(2)

# Creates a loop
while True:
    reading = photo_sensor.read_u16()

# Prints Pew Pew if the value is over 50000
    if reading >= 50000:
        print("Pew Pew")
# Runs program every 1 second     
    utime.sleep(1)