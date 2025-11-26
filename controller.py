from interfaceGraphiqueChef import IHM_Chef


class Controller:
    def __init__(self):
        self.votes = []  # Vide au départ !
        self.question_courante = "Donnez votre avis sur le plat ?"
        self.ihm = IHM_Chef(self)


    def recevoir_vote(self, numero):
        self.votes.append(numero)


    def visualiser_resultats(self):
        print("Affichage des résultats des votes")  


    def modifier_question(self):
        print("Affichage de la fenêtre de modification de la question")  
        

if __name__ == "__main__":
    app = Controller()
