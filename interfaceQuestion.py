import random
import json
from paho.mqtt import client as mqtt_client

class Question:
    BROKER = "192.168.190.15"
    PORT = 1883
    CLIENT_ID = "chef-cantine-02"
    USERNAME = "CHEF"
    PASSWORD = "ABC"
    TOPIC_QUESTION = "cantine/chef/question"

    def __init__(self, controller):
        self.topic = self.TOPIC_QUESTION
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
        self.client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION1,
            client_id=self.client_id
        )
        self.client.username_pw_set(self.USERNAME, self.PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.controller = controller

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            self.client.subscribe(self.TOPIC_QUESTION)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        if msg.topic == self.TOPIC_QUESTION:
            payload = json.loads(msg.payload)
            question = payload['question']
            listeChoix = payload['choix']  
            print("Question reçue :", question)
            print("Liste des choix :", listeChoix)
        

    def modifier_question(self, nouvelle_question, nouveaux_choix):
        # Méthode pour publier une nouvelle question 
        payload = json.dumps({
            'question': nouvelle_question,
            'choix': nouveaux_choix
        })
        self.client.publish(self.TOPIC_QUESTION, payload)
        print("Nouvelle question envoyée : ", nouvelle_question)

    def connecter(self):
        self.client.connect(self.BROKER, self.PORT)
        self.client.subscribe(self.TOPIC_QUESTION)
        self.client.loop_start()

    def deconnecter(self):
        self.client.disconnect()
        self.client.loop_stop()