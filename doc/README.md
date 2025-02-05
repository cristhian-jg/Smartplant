# SMARTPLANT

## Sistema domótico de control de plantas con MQTTT

Smartplant trata de una simulación de  un sistema domótico para el control de plantas, se nos pide implementar un broker y 4 clientes MQTT, ademas de un interfaz con gráficos.

Para empezar necesitamos Mosquitto para trabajar con MQTT, y la librería PAHO para trabajar con mqtt en el código Python. En MacBook para instalar mosquito debemos tener homebrew y usar el comando: brew install mosquitto, para instalar PAHO con python se instala la librería con el comando: pip install paho-mqtt.

Al instalar el broker mosquitto hay que iniciarlo con brew services start mosquitto. Con esto en marcha empecé a crear el proyecto en Visual Studio Code donde cree varios archivos .py que serán los clientes que se conecten al broker.