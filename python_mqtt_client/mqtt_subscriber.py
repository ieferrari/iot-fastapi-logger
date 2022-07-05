# SUBSCRIBER, 
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set("admin", "admin")
client.connect('localhost', 1883)

def on_connect(client, userdata, flags, rc):
    print("Conexión exitosa al Broker")
    client.subscribe('#')

def on_message(client, userdata, message):
    print(message.payload, message.payload.decode(), message.topic, message.qos)

while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


