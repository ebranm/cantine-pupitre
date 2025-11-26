import json
from paho.mqtt import client as mqtt_client

class Commentaire:
    TOPIC_COMMENTAIRE = "cantine/chef/commentaire"

    def __init__(self, client):
        #déja connecter
        self.client = client  

    def publier_commentaire(self, commentaire):
        payload = json.dumps({'commentaire': commentaire})
        self.client.publish(self.TOPIC_COMMENTAIRE, payload)
        print("Commentaire envoyé :", commentaire)
