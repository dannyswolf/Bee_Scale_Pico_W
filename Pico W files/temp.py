"""
If you print the value of the temperature value you are going to get
an integer number between 0 and 65535
The temperature sensor works by delivering a voltage to the ADC4 pin
that is proportional to the temperature.
From the datasheet, a temperature of 27 degrees Celsius delivers a voltage of 0.706 V.
With each additional degree the voltage reduces by 1.721 mV or 0.001721 V.
The first step in converting the 16-bit temperature is to convert it back to volts,
which is done based on the 3.3 V maximum voltage used by the Pico board.
With this conversion, the temperature value holds a value between 0 and 3.3.
We again have to do the second conversion which brings the temperature to the Celsius scale.
https://how2electronics.com/read-temperature-sensor-value-from-raspberry-pi-pico/
"""


import machine
import utime
from time import sleep
import dht
from credentials import secrets

DEBUG = secrets['DEBUG']

def get_pico_temp():
    if DEBUG:
        print("Getting Pico Temp")
    pico_sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = pico_sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    if DEBUG:
        print("pico temperature", temperature)
    return temperature


# https://randomnerdtutorials.com/esp32-esp8266-dht11-dht22-micropython-temperature-humidity-sensor/



def get_temp_humidity():
    if DEBUG:
        print("Getting DHT22 Temperature")
    max_tries = 6
    sensor = dht.DHT22(machine.Pin(2))
    #sensor = dht.DHT11(machine.Pin(14))
    while max_tries > 0:
        max_tries -=1
        if DEBUG:
            print("Starting loop max_tries", max_tries)
        try:
            # DHT22 Sampling period 2 seconds
            sleep(2)
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            # temp_f = temp * (9/5) + 32.0
            if DEBUG:
                print('Temperature:' , temp)
                # print('Temperature: %3.1f F' %temp_f)
                print('Humidity:', hum)
            return temp, hum
            if max_tries == 0:
                # filename = "log.txt"
                # file = open(filename, "a")
                # file.write(f"\nFailed to read AM2302 (DHT22) sensor 5 times in a row")
                # file.close()
                if DEBUG:
                    print(f"\n Failed to read AM2302 (DHT22) sensor 5 times in a row")
                return 0.0, 0.0
        except Exception as e:
            # print(f"\nFailed to read sensor. Exception : {e}")
            # filename = "log.txt"
            # file = open(filename, "a")
            # file.write(f"\nFailed to read AM2302 (DHT22) sensor. Exception : {e} max_tries: {max_tries}")
            # file.close()
            if DEBUG:
                print(f"\nFailed to read AM2302 (DHT22) sensor. Exception : {e} max_tries: {max_tries}")
            if max_tries == 0:
                return 0.0, 0.0
                
            
    
    
# while True:
#    sleep(1)
#    get_temp_humidity()
#    get_pico_temp()