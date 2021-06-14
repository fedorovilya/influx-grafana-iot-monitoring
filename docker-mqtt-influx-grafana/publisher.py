import paho.mqtt.client as mqttClient
import time
import random


def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


Connected = False  # global variable for the state of the connection

broker_address = "0.0.0.0"
port = 1883
# password = "1"

client = mqttClient.Client()  # create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

try:
    token = 1
    value = 0
    while True:
        if token == 1:
            value += 1
        else:
            value -= 1
        if value == 10 or value == 0:
            token *= -1
        temp = "test_table,site=room1 value={0}".format(value)
        print(temp)
        client.publish("sensors", temp)

        value2 = random.randint(10, 30)
        temp2 = "table_second,site=room2 value=" + str(value2)
        print(temp2)
        client.publish("sensors", temp2)

        time.sleep(2)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
