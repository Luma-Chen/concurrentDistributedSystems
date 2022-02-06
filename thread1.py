import paho.mqtt.client as mqtt
from struct import pack
from struct import unpack
from random import randint
from time import sleep

TOPIC_SUBSCRIBE = "temperatura"
TOPIC_PUBLISH = "umidade"

def conexao(self):
    self.subscribe(TOPIC_SUBSCRIBE, 0)

def mensagem(msg):
    v = unpack(">H", msg.payload)[0]
    print ("Mensagem recebida: " + msg.topic + " => " + str(v))

client = mqtt.Client(client_id = 'PROCESSO 1', protocol = mqtt.MQTTv31)
client.on_connect = conexao
client.on_message = mensagem
client.connect("127.0.0.1", 1883)

while True:
    aleatorio = randint(0,100)
    carga = pack(">H", aleatorio)
    client.publish(TOPIC_PUBLISH, carga, qos = 0)
    print ("Mensagem enviada: " + TOPIC_PUBLISH + " => " + str(aleatorio))
    sleep (5)