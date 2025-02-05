import paho.mqtt.client as mqtt

# Cliente que funciona como
# sensor del color de la hojas

def on_connect(client, userdata, flags, rc):
    print("Conectado con el código resultado " + str(rc))
    client.subscribe("colplant")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

mqttClient =mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

mqttBroker = "localhost"
mqttPort = 1883
mqttClient.connect(mqttBroker, mqttPort)

mqttClient.loop_forever()