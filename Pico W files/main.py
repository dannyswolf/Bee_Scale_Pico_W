# https://github.com/ghubcoder/micropython-pico-deepsleep/issues/8#issuecomment-1430355998
import time
import machine
import network
import requests
from credentials import secrets

from scale import get_weight
from vsys_volts import measure_vsys
from ina219 import get_battery_volts
from temp import get_pico_temp, get_temp_humidity
from set_date_time import get_date_time
from mqtt import sent_to_HiveMQ_Cloud

DEBUG = secrets['DEBUG']

current_datetime = "0"


status = None
headers = None

temp = 0.0
humidity = 0.0
weight = 0.0
Pico_temp = 0.0
system_volts = 0.0
battery_volts = 0.0
shunt_voltage = 0.0
current = 0.0
power = 0.0
payload= "0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0"

led = machine.Pin("LED", machine.Pin.OUT)

def toggle_led(times):
    if DEBUG:
        print("toggle_led times", times)
    for i in range(times):
        if DEBUG:
            print("led.on i", i)
        led.on()
        time.sleep(1)
        led.off()
        if DEBUG:
            print("led.off i", i)
        time.sleep(1)
        

def collect_data_to_send():
    
    list_payload = []
    if DEBUG:
        print("collect_data_to_send")
    global temp, humidity, weight, Pico_temp, system_volts, payload, battery_volts, shunt_voltage, current, power
    toggle_led(2)
    temp, humidity = get_temp_humidity()
    time.sleep(3)
    list_payload.append(temp)
    list_payload.append(humidity)
    if DEBUG:
        print("temp, humidity", temp, humidity)
    toggle_led(3)
    weight = get_weight()
    time.sleep(3)
    if DEBUG:
        print("weight", weight)
    toggle_led(4)
    Pico_temp = get_pico_temp()
    time.sleep(3)
    if DEBUG:
        print("Pico_temp", Pico_temp)
    toggle_led(5)
    system_volts = measure_vsys()
    ti_ina_219_readings = get_battery_volts() # ειναι το chip https://wiki.dfrobot.com/Gravity%3A%20I2C%20Digital%20Wattmeter%20SKU%3A%20SEN0291
    battery_volts = ti_ina_219_readings[0] # Voltage of IN- to GND
    shunt_voltage = ti_ina_219_readings[1] # Voltage of the sampling resistor, IN+ to NI-
    current = ti_ina_219_readings[2] # Current flows across IN+ and IN-
    power = ti_ina_219_readings[3] #Power (in milliwatts)
    time.sleep(3)
    if DEBUG:
        print("system_volts", system_volts)
        print("battery_volts", battery_volts) # Voltage of IN- to GND
        print("shunt_voltage", shunt_voltage) # Voltage of the sampling resistor, IN+ to NI-
        print("current", current)			  # Current flows across IN+ and IN-
        print("power", power)
    list_payload.append(weight)
    list_payload.append(Pico_temp)
    list_payload.append(system_volts)
    list_payload.append(battery_volts)
    list_payload.append(shunt_voltage)
    list_payload.append(current)
    list_payload.append(power)
    #print("weight, Pico_temp, system_volts", weight, Pico_temp, system_volts)
    try :
        payload = f'{weight:.3f} {Pico_temp:.1f} {system_volts:.1f} {temp:.1f} {humidity:.1f} {battery_volts:.2f} {shunt_voltage:.4f} {current:.1f} {power:.1f}'
        if DEBUG:
            print("list_payload:", list_payload)
        return list_payload
    except Exception as e: # ValueError: unknown format code 'f' for object of type 'NoneType'
        payload = f'0 {Pico_temp:.1f} {system_volts:.1f} {temp:.1f} {humidity:.1f} {battery_volts:.2f} {shunt_voltage:.4f} {current:.1f} {power:.1f}'
        if DEBUG:
            print(f"Exception {e} list_payload:", list_payload)
        return list_payload

wlan = None
wlanSw = machine.Pin(23, machine.Pin.OUT)
wlan = network.WLAN(network.STA_IF)
# set power mode to get WiFi power-saving off (if needed)
wlan.config(pm = 0xa11140)


Max_Tries = 5
SEND_DATA_TRIES = 5

        

def disconnect():
    time.sleep(3)
    toggle_led(9)
    if DEBUG:
        print('Disconnecting...')
    
    global wlanSw, led, wlan
    wlanSw.low()
    led.low()
    
    time.sleep_ms(500)
    
    wlan.disconnect()
    wlan.active(False)
    wlan.deinit()
    wlan = None
    
    time.sleep_ms(500)
    if DEBUG:
        print("Disconnected!")
    
def connect():
    try:
        if DEBUG:
            print("Connecting...")
        global wlan, status, headers, current_datetime, Max_Tries
        global wlanSw
        wlanSw.high()
    
        tries = 0
        wlan.active(True)
        wlan.connect(secrets["ssid"], secrets["password"])
        time.sleep(5)
        
        if DEBUG:
            print("wlan.status()", wlan.status())
        if wlan.status() == 3:
            led.on()
            time.sleep(5)
            ip = wlan.ifconfig()[0]
            if DEBUG:
                print(f"Connected to {secrets["ssid"]}", ip)
            led.off()
            time.sleep(3)
            toggle_led(6)
            current_datetime = get_date_time()
            return 
        else:
            led.off()
            while tries < Max_Tries:
                tries +=1
                wlan.active(False)
                wlan.active(True)
                wlan.connect(secrets["ssid"], secrets["password"])
                # Printing anything to console however appears to break deep sleep
                # https://ghubcoder.github.io/posts/pico-w-deep-sleep-with-micropython/
                if DEBUG:
                    print(f"Connecting to {secrets["ssid"]} ... Προσπάθεια {tries} απο {Max_Tries} wlan.status()", wlan.status())
                time.sleep(5)
                if DEBUG:
                    print("wlan.ifconfig()", wlan.ifconfig())
                if wlan.isconnected():
                    led.on()
                    time.sleep(5)
                    ip = wlan.ifconfig()[0]
                    if DEBUG:
                        print(f"Connected to {secrets["ssid"]}", ip)
                    led.off()
                    time.sleep(3)
                    toggle_led(6)
                    current_datetime = get_date_time()
                    return 
                elif tries == Max_Tries and not wlan.isconnected():
                    wlan.active(False)
                    led.off()                
                    # filename = "log.txt"
                    # file = open(filename, "a")
                    # file.write(f"\n Unable to connect to {secrets["ssid"]}")
                    # file.close()
                    led.on()
                    time.sleep(2)
                    led.off()
                    time.sleep(2)
                    led.on()
                    time.sleep(2)
                    led.off()
                    time.sleep(2)
                    led.on()
                    time.sleep(2)
                    led.off()
                    disconnect()
                    doLightSleep(600)  #give seconds -- 10 minutes 600 seconds
    except Exception as e:
        # filename = "log.txt"
        # file = open(filename, "a")
        # file.write(f"\nException:{str(e)} Could not connect (Wifi status =" + str(wlan.status()) + " 3=connected)")
        # file.close()
        if DEBUG:
            print(f"\nException:{str(e)} Could not connect (Wifi status =" + str(wlan.status()) + " 3=connected)")
        disconnect()
        doLightSleep(600)

def doLightSleep(sleepSeconds):
    if DEBUG:
        print("doLightSleep sleepSeconds:", sleepSeconds) 
    time.sleep_ms(100)
    machine.lightsleep(sleepSeconds * 1000)
    time.sleep_ms(100)
    # https://docs.micropython.org/en/latest/library/machine.html
    machine.soft_reset()  # works αλλά δεν ξέρω πόσο ρέυμα ξωδεύει
    # machine.PWRON_RESET   #  επιστρέφει 1
    
def sent_data():
    time.sleep(3)
    toggle_led(7)
    global SEND_DATA_TRIES,  headers, payload, wlan, current_datetime
    status = wlan.ifconfig()
    headers = {'Connection': 'keep-alive',
               'Client': f'{status[0]}',
               'User-Agent': 'Pico W'}
    while SEND_DATA_TRIES > 0:
        SEND_DATA_TRIES -=1
        try:
            if DEBUG:
                print(f"url {secrets['url']} sending headers {headers} payload {payload}") 
            response = requests.get(url=secrets['url'], headers=headers, data=payload)
            if DEBUG:
                print("response.status_code", response.status_code)
            if response.status_code == 200:
                response.close()
                time.sleep(3)
                toggle_led(8)
                return
            else:
                if SEND_DATA_TRIES == 0:
                    time.sleep(1)
                    # filename = "log.txt"
                    # file = open(filename, "a")
                    # file.write(f"\n{current_datetime} response.status.code:{str(response.status_code)} SEND_DATA_TRIES ={SEND_DATA_TRIES} Could not Sent data {payload} (Wifi status =" + str(wlan.status()) + " 3=connected)")
                    # file.close()
                    if DEBUG:
                        print(f"\n{current_datetime} response.status.code:{str(response.status_code)} Could not Sent data to Django {payload} (Wifi status =" + str(wlan.status()) + " 3=connected)")
                    doLightSleep(3480)   # 3600 ==> 1 Hour  3480 ==> Δωκιμή σε 58 λεπτά)  
                else:
                    doLightSleep(600)  # Δωκιμή σε 10 λεπτά πάλι
        except Exception as e: # OSError: -2 An OSError with code -2 in MicroPython generally indicates that there was an error with the provided argument(s) or configuration
            # Ορισμός ημερομηνίας και ώρας
            # filename = "log.txt"
            # file = open(filename, "a")
            # file.write(f"\n{current_datetime} Exception:{str(e)}SEND_DATA_TRIES ={SEND_DATA_TRIES} Could not Sent data to Django {payload} (Wifi status =" + str(wlan.status()) + " 3=connected)")
            # file.close()
            if DEBUG:
                print(f"\n{current_datetime} Exception:{str(e)} Could not Sent data to Django {payload} (Wifi status =" + str(wlan.status()) + " 3=connected)")
            doLightSleep(600)  # Δωκιμή σε 10 λεπτά πάλι
            
            
while True:
    list_data = collect_data_to_send()
    connect()
    # sent_data() # To django
    # Δεν παίζει καλά το paho.mqtt που είναι στο django
    # δεν πέρνει τα μηνύματα απο τον server και για να τρέξεί θέλει να κάνεις request το app scale στο django
    # για να φορτώσει αφού είναι στο __init__.py
    sent_to_HiveMQ_Cloud(list_data) 
    disconnect()
    doLightSleep(sleepSeconds=3480)   # 3600 ==> 1 Hour  3480 ==> 58 λεπτά

