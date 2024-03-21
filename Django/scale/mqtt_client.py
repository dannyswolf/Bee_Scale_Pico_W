# https://console.hivemq.cloud/clients/python-paho?uuid=d492b524dbce45018cd0f1c917cb94c1
#
# Copyright 2021 HiveMQ GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""

Using loop_start() instead of loop_forever() will give you not blocking background thread.
https://stackoverflow.com/questions/41015779/how-to-use-paho-mqtt-client-in-django
βάζουμε στο __init__.py και ξεκινάει όταν διαβάζει το module scale
from . import mqtt_client
mqtt_client.client.loop_start()

"""

from datetime import datetime
import time
import paho.mqtt.client as paho
from paho import mqtt
from .credentials import secrets

# Call connect_mqtt() in your Django app to establish the MQTT connection
# Call disconnect_mqtt() to disconnect from MQTT when needed

# MQTT client setup
username = secrets["mqtt_username"]
password = secrets["mqtt_key"]
broker_url = secrets["broker"]
port = 8883

DEBUG = False

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, reason_code, properties):
    if DEBUG:
        print(5 * "*" + "Connecting to HiveMQ" + 5 * "*")
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        # subscribe to all topics of 'picow' by using the wildcard "#"
        #    At most once (QoS 0)
        #    At least once (QoS 1)
        #    Exactly once (QoS 2)
        client.subscribe("picow/#", qos=2)

    # print(f'client: {client}')  # <paho.mqtt.client.Client object at 0x7fba01943950>
    # print(f'userdata: {userdata}') # userdata: None
    # print(f'flags: {flags}')  # flags: 'session present': 0



    if DEBUG:
        # print(5 * '-' + f'rc: {rc}' + 5 * '-')  # rc: Success
        print(5 * "*" + "Finish Connected to HiveMQ" + 5 * "*")


# with this callback you can see if your publishing was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    if DEBUG:
        print(10 * "*" + "Subscribed to HiveMQ" + 30 * "*")
    # print(f'client:, {client}') #  client:, <paho.mqtt.client.Client object at 0x7fba0193bb90>
    # print(f'userdata:, {userdata}') # userdata:, None
    # print(f'mid:, {mid}') # mid:, 1
    # print(f'granted_qos:, {granted_qos}') # granted_qos:, [<paho.mqtt.reasoncodes.ReasonCodes object at 0x7fba008b0dd0>]
    if DEBUG:
        print(5 * "*" + "Finish subscribed to HiveMQ" + 5 * "*")


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    # έρχονται 2 ίδια μηνύματα με διαφορά milliseconds
    today_month_number = datetime.today().month  # Επιστέφει μόνο τον αριθμό του μήνα, 12 αν είναι Δεκέμβρης
    from .models import January, February, March, April, May, June, July, August, September, October, November, December
    lists_of_months = [January, February, March, April, May, June, July, August, September, October, November, December]
    # πρέπει αυτά να είναι εκτός γιατί σε κάθε μήνυμα θα αλλάζουν
    global temperature, humidity, weight, Pico_temp, system_volts, new_obj, battery_volts, shunt_voltage
    if DEBUG:
        print(10 * "*" + "Message from HiveMQ" + 10 * "*")
        # print(f"client:, {client}")  # <paho.mqtt.client.Client object at 0x7fb9f38c3f10>
        # print(f"userdata:, {userdata}, msg.qos:, {msg.qos}")  # userdata:, None, msg.qos:, 0

    if msg.topic == 'picow/temperature':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/temperature,  msg.payload, {msg.payload}" + 5 * '-')
        temperature = round(float(msg.payload), 2)
    elif msg.topic == 'picow/humidity':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/humidity,  msg.payload, {msg.payload}" + 5 * '-')
        humidity = msg.payload
    elif msg.topic == 'picow/weight':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/weight,  msg.payload, {msg.payload}" + 5 * '-')
        try:
            weight = round(float(msg.payload), 3)
        except ValueError: #  could not convert string to float: b'None'
            weight = 0.000
    elif msg.topic == 'picow/Pico_temp':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/Pico_temp,  msg.payload, {msg.payload}" + 5 * '-')
        Pico_temp = round(float(msg.payload), 1)
    elif msg.topic == 'picow/system_volts':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/system_volts,  msg.payload, {msg.payload}" + 5 * '-')
        system_volts = round(float(msg.payload), 1)
    elif msg.topic == 'picow/battery_volts':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/battery_volts,  msg.payload, {msg.payload}" + 5 * '-')
        battery_volts = round(float(msg.payload), 2)

    elif msg.topic == 'picow/shunt_voltage':
        if DEBUG:
            print(5 * '-' + f"topic:, picow/shunt_voltage,  msg.payload, {msg.payload}" + 5 * '-')
        shunt_voltage = round(float(msg.payload), 2)
        # Το picow/shunt_voltage είναι το τελευταίο που στέλνει αρα μπορούμε να κάνουμε new_obj
        # αφού ελέγξουμε οτι δεν υπάρχει ίδιο object ελέγχοντας τη διαφορά χρόνου με το τελευταίο

        month_obj = lists_of_months[today_month_number - 1]

        # Αν έχει αλλάξει ο μήνας και δεν έχουμε ακόμα τιμές βγάζει σφάλματα
        if not month_obj.objects.first():  # έλεγχος αν έχει αντικείμενο
            month_obj = lists_of_months[today_month_number - 2]  # να παίρνει τιμές απο τον προηγούμενο μήνα

        latest_obj = month_obj.objects.first()  # first() γιατί το model επιστρέψει [-pk]
        latest_obj_date = latest_obj.Ημερομηνία  # datetime.date(2023, 8, 18)
        latest_obj_time = latest_obj.Ωρα

        # Πρέπει η σύγκριση να γίνει με ίδια οχι datetime με date
        # datetime.today() => datetime.datetime(2023, 8, 18, 8, 40, 19, 243878)
        # datetime.today().date() => datetime.date(2023, 8, 18)
        if DEBUG:
            print(f"latest_obj_date {latest_obj_date}")
            print(f"datetime.today().date() {datetime.today().date()}")

        # To calculate the difference, you have to convert the datetime.time object to a datetime.datetime object.
        object_time = datetime.combine(latest_obj_date, latest_obj_time)
        datetime_time_now = datetime.today()
        time_difference = datetime_time_now - object_time
        time_difference_in_minutes = time_difference.total_seconds() / 60
        if DEBUG:
            print(f"time_difference_in_minutes {time_difference_in_minutes}")
        # if time_difference_in_minutes > 50:  # αν η διαφορά είναι μεγαλύτερη απο 50 λεπτά τότε να κάνει new_obj
        new_obj = lists_of_months[today_month_number - 1].objects.create(Βάρος=weight,
                                                                         Pico_Θερμοκρασία=Pico_temp,
                                                                         Volts=system_volts, Temp=temperature,
                                                                         Humidity=humidity, Battery_Volts=battery_volts,
                                                                         Shunt_Voltage=shunt_voltage)
        if DEBUG:
            print(10 * '-' + f"new_obj created \n Weight: {new_obj.Βάρος} \n Pico temp: {new_obj.Pico_Θερμοκρασία} \n"
                            f"System volts: {new_obj.Volts} \n Temp: {new_obj.Temp} \n Humidity: {new_obj.Humidity} \n "
                             f"Battery Volts: {new_obj.Battery_Volts} \n Shunt Voltage: {new_obj.Shunt_Voltage}" + 10 * '-')

    # print(5 * "*" + "Finish Message from HiveMQ" + 5 * "*")


# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
# Version 2 need paho.CallbackAPIVersion.VERSION2
# client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(username, password)
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(broker_url, 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
# client.on_publish = on_publish # Δεν έχω δώσει δικαιώματα για publish



# a single publish, this can also be done in loops, etc.
# client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_start()

# client.loop_forever()