# PUBLISHER
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

client = mqtt.Client()
client.username_pw_set("admin", "admin")
client.connect('localhost', 1883)

while True:
    #client.publish('patio/temperatura', input('Message : '))
    randNumber = round(uniform(19.0, 22.0),2)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(2)