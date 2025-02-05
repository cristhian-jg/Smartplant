import paho.mqtt.client as mqtt
import random
import time

# Cliente que funciona como
# sensor de temperatura

def on_connect(client, userdata, flags, rc):
    print("Conectado con el código resultado " + str(rc))
    client.subscribe("plantas/temperatura")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    temperature = int(msg.payload) + random.randint(-5, 5)
    print("Temperatura: " + str(temperature))
    mqttClient.publish("plantas/temperatura", str(temperature))


mqttBroker = "localhost"
mqttPort = 1883
topic_in = "plantas/temperatura"
topic_out = "plantas/temperatura"
publish_interval = 10

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

mqttClient.connect(mqttBroker, mqttPort)

while True:
    temperature = random.randint(10,35) 
    print(f"Temperatura enviada: {temperature}º")
    mqttClient.publish(topic_out, str(temperature))
    time.sleep(publish_interval)