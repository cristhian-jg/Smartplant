import paho.mqtt.client as mqtt

# Cliente que funciona como motor

# def on_connect(client, userdata, flags, rc):
#    print("Conectado con el código resultado " + str(rc))
#    client.subscribe("planta/motor")

topic_humidity = "planta/humedad"
topic_motor = "planta/motor"

def on_message(client, userdata, msg):
    humedad = float(msg.payload.decode())
    print(f"Humedad recibida: {humedad}%")

    if humedad < 30:
        print("Motor ON")
        client.publish(topic_motor, "ON")
    else:
        print("Motor OFF")
        client.publish(topic_motor, "OFF") 

mqttBroker = "localhost"
mqttPort = 1883

mqttClient = mqtt.Client()
mqttClient.on_message = on_message
mqttClient.connect(mqttBroker, mqttPort)
mqttClient.subscribe(topic_humidity)

print("Esperando datos de humedad...")
mqttClient.loop_forever()