import paho.mqtt.client as mqtt
import time
import random

# Cliente que funcTerminaiona como
# sensor del color de la hojas

# def on_connect(client, userdata, flags, rc):
#    print("Conectado con el código resultado " + str(rc))
#    client.subscribe("colplant")

# def on_message(client, userdata, msg):
#    print(msg.topic + " " + str(msg.payload))

mqttBroker = "localhost"
mqttPort = 1883
topic = "planta/color"
publish_interval = 10

mqttClient = mqtt.Client()
# mqttClient.on_connect = on_connect
# mqttClient.on_message = on_message

mqttClient.connect(mqttBroker, mqttPort)

colores = ["verde", "amarillo", "marrón", "negro"]

while True:
    color = random.choice(colores)
    print(f"Enviando color de las hojas: {color}")
    mqttClient.publish(topic, color)
    time.sleep(publish_interval)