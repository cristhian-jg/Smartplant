import streamlit as st
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import time

data = {
    "temperatura": [],
    "humedad": [],
    "color": [],
    "motor": []
}

latest_values = {
    "temperatura": None,
    "humedad": None,
    "color": None,
    "motor": None
}

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    
    if topic == "planta/temperatura":
        latest_values["temperatura"] = float(payload)
        data["temperatura"].append(float(payload))
    elif topic == "planta/humedad":
        latest_values["humedad"] = float(payload)
        data["humedad"].append(float(payload))
    elif topic == "planta/color":
        latest_values["color"] = payload
    elif topic == "planta/motor":
        latest_values["motor"] = payload

mqttBroker = "localhost"
mqttClient = mqtt.Client()
mqttClient.on_message = on_message
mqttClient.connect(mqttBroker, 1883)
mqttClient.subscribe("planta/temperatura")
mqttClient.subscribe("planta/humedad")
mqttClient.subscribe("planta/color")
mqttClient.subscribe("planta/motor")
mqttClient.loop_start()

st.title("Smartplant")

placeholder = st.empty()

while True:
    time.sleep(2)
    
    with placeholder.container():
        st.subheader("Últimos valores recibidos:")
        st.write(f"**Temperatura:** {latest_values['temperatura']}°C")
        st.write(f"**Humedad:** {latest_values['humedad']}%")
        st.write(f"**Color de las hojas:** {latest_values['color']}")
        st.write(f"**Estado del motor:** {latest_values['motor']}")

        if len(data["temperatura"]) > 0 and len(data["humedad"]) > 0:
            avg_temp = sum(data["temperatura"]) / len(data["temperatura"])
            avg_humidity = sum(data["humedad"]) / len(data["humedad"])
            st.subheader("Valores promedio")
            st.write(f"**Temperatura promedio:** {avg_temp:.2f}°C")
            st.write(f"**Humedad promedio:** {avg_humidity:.2f}%")

        st.subheader("Gráficas de valores registrados")
        fig, ax = plt.subplots()
        ax.plot(data["temperatura"], label="Temperatura (°C)", color='r')
        ax.plot(data["humedad"], label="Humedad (%)", color='b')
        ax.set_xlabel("Muestras")
        ax.set_ylabel("Valores")
        ax.legend()
        st.pyplot(fig)