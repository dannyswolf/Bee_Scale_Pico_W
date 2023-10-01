# https://github.com/FDelporte/HiveMQ-examples/tree/main/picow-to-hivemq

import time
# Load the WiFi and HiveMQ Cloud credentials from secrets.py
from credentials import secrets

from umqtt.simple import MQTTClient
from time import sleep
from set_date_time import get_date_time

# Get data to send
# from main import collect_data_to_send
# list_payload = collect_data_to_send()

DEBUG = secrets['DEBUG']

# ------------ Need Internet ------------ #
# Send to HiveMQ Cloud 
def sent_to_HiveMQ_Cloud(data_to_send):
    if DEBUG:
        print("sent_to_HiveMQ_Cloud...")
    # When using the sslparams below, a connection can be made to HiveMQ Cloud, but it's not secure
    sslparams = {'server_hostname': secrets["broker"]}
    # Connect to HiveMQ Cloud
    # Based on https://www.tomshardware.com/how-to/send-and-receive-data-raspberry-pi-pico-w-mqtt
    # print('----------------------------------------------------------------------------------------------')
    # print("Connecting to " + secrets["broker"] + " as user " + secrets["mqtt_username"])
    mqtt_client = MQTTClient(client_id="picow",
                    server=secrets["broker"],
                    port=secrets["port"],
                    user=secrets["mqtt_username"],
                    password=secrets["mqtt_key"],
                    keepalive=3600,
                    ssl=True,
                    ssl_params=sslparams)
    if DEBUG:
        print("Connecting ...")
    mqtt_client.connect()
    # print('Connected to MQTT Broker: ' + secrets["broker"])
    # print("Starting Send to HiveMQ Cloud")
    try:
        #json = "{\"picow/system_volts\": " + str(data_to_send) + "}"
        if DEBUG:
            print("Sending picow/temperature", data_to_send[0])
        mqtt_client.publish("picow/temperature", str(f"{data_to_send[0]}"))
        sleep(1)
        if DEBUG:
            print("Sending picow/humidity", data_to_send[1])
        mqtt_client.publish("picow/humidity", str(f"{data_to_send[1]}"))
        sleep(1)
        if DEBUG:
            print("Sending picow/weight", data_to_send[2])
        mqtt_client.publish("picow/weight", str(f"{data_to_send[2]}"))
        sleep(1)
        if DEBUG:
            print("Sending picow/Pico_temp", data_to_send[3])
        mqtt_client.publish("picow/Pico_temp", str(f"{data_to_send[3]}"))
        sleep(1)
        if DEBUG:
            print("Sending picow/system_volts", data_to_send[4])
        mqtt_client.publish("picow/system_volts", str(f"{data_to_send[4]}"))
        sleep(1)
        if DEBUG:
            print("Messages send")
        mqtt_client.disconnect()
    except Exception as e:
        # print("\tMQTT publish Failed, retrying\n", e)
        current_datetime = get_date_time()
        filename = "log.txt"
        file = open(filename, "a")
        file.write(f"\n{current_datetime} MQTT publish Failed Exception: {e}")
        file.close()
        if DEBUG:
            print(f"{current_datetime} MQTT publish Failed Exception: {e}")

# sent_to_HiveMQ_Cloud(list_payload)