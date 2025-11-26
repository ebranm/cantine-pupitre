import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()  # Création du lecteur
#import rfid ..

class RFID :

    def __init__(self):
        print("Activation du lecteur RFID")
        #initier le rfid


    def lireRfid(self):
        """Méthode qui permet de faire la lecture du badge
        Elle retourne l'id du badge"""
        print("Place your RFID tag or card near the reader...")
        badge_id, text = reader.read()  # Bloque ici jusqu'à ce qu'un badge soit posé
#lire la carte

       
        return badge_id