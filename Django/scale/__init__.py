from . import mqtt_client
mqtt_client.client.loop_start()

# https://stackoverflow.com/questions/41015779/how-to-use-paho-mqtt-client-in-django
# Using loop_start() instead of loop_forever() will give you not blocking background thread.