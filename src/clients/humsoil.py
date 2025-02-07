import paho.mqtt.client as mqtt
import random
import time

# Cliente que funciona como
# sensor de humedad de la planta

# def on_connect(client, userdata, flags, rc):
#    print("Conectado con el código resultado " + str(rc))
#    client.subscribe("planta/humedad")

# def on_message(client, userdata, msg):
#    print(msg.topic + " " + str(msg.payload))
#    humidity = int(msg.payload) + random.randint(-5,5)
#    print("Humedad: " + str(humidity))
#    mqttClient.publish("planta/humedad", str(humidity))

mqttBroker = "localhost"
mqttPort = 1883
topic = "planta/humedad"
publish_interval = 5

mqttClient = mqtt.Client()
# mqttClient.on_connect = on_connect
# mqttClient.on_message = on_message
mqttClient.connect(mqttBroker, mqttPort)

while True:
    humidity = random.randint(20, 80)
    print(f"Humedad enviada: {humidity}%")
    mqttClient.publish(topic, str(humidity))
    time.sleep(publish_interval)