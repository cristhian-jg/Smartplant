import paho.mqtt.client as mqtt

BROKER_ADDRESS = "localhost"
PORT = 1883
TOPIC = "test/mensaje"

def on_message(client, userdata, message):
    print(f"Mensaje recibido: {message.payload.decode()} en el tópico {message.topic}")