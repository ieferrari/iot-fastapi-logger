# PUBLISHER
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from math import sin
from datetime import datetime

client = mqtt.Client()
client.username_pw_set("admin", "admin")
client.connect('localhost', 1883)

def X(t):
    return sin(t/60)+2*sin(1/20*t)

while True:
    #client.publish('patio/temperatura', input('Message : '))
    hour = datetime.now().strftime('%M %S').split(' ')
    hour = int(hour[0])*60 + int(hour[1])
    randNumber =X(hour) + round(uniform(0, 0.5),2)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(0.5)