"""
Created on Mon Nov 29 01:46:16 2021

@author: Mirror
"""
# !!!WARNING: DO NOT CHANGE THE ORDER: HIGH AIRPOLLUTION, LOW AIR POLLUTION, NOISY !!!
# set your threshold here please
high_air_pollution_threshold = 700
low_air_pollution_threshold = 300
noisy_threshold = 400

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.hivemq.com'
port = 1883
topic = "testtopic/7ZW5M0/StudentGroup_7&8/control"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while msg_count == 0:
        time.sleep(1)
        msg_1 = 'The threshold of high air pollution is: ' +str(high_air_pollution_threshold)+' now.\n'
        msg_2 = 'The threshold of low air pollution is: ' +str(low_air_pollution_threshold)+' now.\n'
        msg_3 = 'The threshold of being noisy is: ' +str(noisy_threshold)+' now.' 
        msg = 'Dag! '+msg_1+msg_2+msg_3
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()