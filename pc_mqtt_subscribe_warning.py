# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:30:18 2021

@author: Mirror
"""
from paho.mqtt import client as mqtt_client


broker = 'broker.hivemq.com'
port = 1883
topic = "testtopic/7ZW5M0/StudentGroup_7&8/angel&aq&sound"
# generate client ID with pub prefix randomly
client_id = 'clientId-f7frY8vHS6'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        change=msg.payload.decode()
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()