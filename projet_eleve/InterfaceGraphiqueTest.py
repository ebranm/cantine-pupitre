# coding: utf-8
from interfaceVotes import InterfaceVotes
from tkinter import *

class IHM:

    def __init__(self, question="", message=""):
        self.question = question 
        self.choix_fait = None
        self.message = message
        

        self.fenetre = Tk()
        self.fenetre.geometry("400x200")   # Taille de la fenêtre

        # Chaque colonne prend toute la largeur disponible → boutons centrés
        self.fenetre.grid_columnconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(1, weight=1)



        # Questions
        self.label_question = Label(self.fenetre, text=self.question)
        self.label_question.grid(row=0, column=0, columnspan=2, pady=10)


    
        # Boutons 
        self.bouton1 = Button(self.fenetre, text='', borderwidth=1)
        self.bouton1.grid(row=1, column=0, pady=5)

        self.bouton2 = Button(self.fenetre, text='', borderwidth=1)
        self.bouton2.grid(row=1, column=1, pady=5)

        self.bouton3 = Button(self.fenetre, text='', borderwidth=1)
        self.bouton3.grid(row=2, column=0, pady=5)

        self.bouton4 = Button(self.fenetre, text='', borderwidth=1)
        self.bouton4.grid(row=2, column=1, pady=5)

        self.label_message = Label(self.fenetre, text=self.message)
        self.label_message.grid(row=4, column=0, columnspan=2, pady=0)




        # demander choix
    def demander_choix(self, question,listeChoix):
        """ Modifier les textes des boutons et des labels pour afficher
         la question et la liste des choix"""

        self.label_question.config(text=question[0])

        
        def faire_choix(numero, texte_choix):
            """faire en sorte de retourner  que le vote a été pris en compte 
            et bien envoyé"""

            self.choix_fait = numero
            self.afficher_message(f"Choix {texte_choix}")
            self.fenetre.quit()



        self.bouton1.config(text=listeChoix[0], command= lambda: faire_choix(listeChoix[0],1))
        self.bouton2.config(text=listeChoix[1], command= lambda: faire_choix(listeChoix[1],2))
        self.bouton3.config(text=listeChoix[2], command= lambda: faire_choix(listeChoix[2],3))
        self.bouton4.config(text=listeChoix[3], command= lambda: faire_choix(listeChoix[3],4))

        



        self.fenetre.mainloop()
        return self.choix_fait


    def afficher_message(self, message):
        print(message)
        self.label_message.config(text=message)

