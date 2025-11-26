from tkinter import *

class ControllerChef:
    def __init__(self):
        self.votes = []  # Vide au départ
        self.question_courante = "Donnez votre avis sur le plat ?"

class IHM_Chef:
    def __init__(self, controller):
        self.controller = controller
        self.fenetre = Tk()
        self.fenetre.geometry("400x200")
        self.fenetre.title("Chef de cantine")
        self.fenetre.grid_columnconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(1, weight=1)
        
        # Écran d'accueil chef (à gauche)
        Label(self.fenetre, text="Chef de cantine identifié", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=12)
        Button(self.fenetre, text="Visualiser les résultats des votes", width=28, height=2,
               command=self.page_resultats).grid(row=1, column=0, columnspan=2, pady=10)
        Button(self.fenetre, text="Modifier la question du vote", width=28, height=2,
               command=self.page_modifier_question).grid(row=2, column=0, columnspan=2, pady=5)
        self.fenetre.mainloop()

    def calculer_statistique(self, votes):
        nb_incroyable = nb_bien = nb_bof = nb_berk = 0
        for vote in votes:
            if vote == 1: nb_incroyable += 1
            elif vote == 2: nb_bien += 1
            elif vote == 3: nb_bof += 1
            elif vote == 4: nb_berk += 1
        total = nb_incroyable + nb_bien + nb_bof + nb_berk
        if total > 0:
            return {
                "Incroyable": nb_incroyable / total * 100,
                "Bien": nb_bien / total * 100,
                "Bof": nb_bof / total * 100,
                "Berk": nb_berk / total * 100
            }
        else:
            return {
                "Incroyable": 0,
                "Bien": 0,
                "Bof": 0,
                "Berk": 0
            }

    def page_resultats(self):
        # Écran de droite après clic sur le bouton
        win = Toplevel(self.fenetre)
        win.geometry("350x230")
        win.title("Résultats des votes")
        Label(win, text="Résultats des votes", font=("Arial", 12)).pack(pady=10)
        votes = self.controller.votes
        stats = self.calculer_statistique(votes)
        for choix in ["Incroyable", "Bien", "Bof", "Berk"]:
            pourcent = stats.get(choix, 0)
            Label(win, text=f"{choix} : {pourcent:.0f} %").pack()
        Button(win, text="Ajouter un commentaire", command=self.page_ajouter_commentaire).pack(pady=16)

    def page_modifier_question(self):
        win = Toplevel(self.fenetre)
        win.geometry("370x290")
        win.title("Modifier la question")
        Label(win, text="Question actuelle :", font=("Arial", 12)).pack(pady=5)
        question_label = Label(win, text=self.controller.question_courante, font=("Arial", 12))
        question_label.pack(pady=2)

        Label(win, text="Nouvelle question :", font=("Arial", 11)).pack(pady=5)
        entree = Entry(win, width=34)
        entree.pack(pady=6)

        # Ajoute les 3 propositions en boutons sous l'Entry
        propositions = [
            "Donnez votre avis sur le plat ?",
            "Ce repas était-il à votre goût ?",
            "Aimerais-tu manger ce plat à nouveau ?"
        ]
        Label(win, text="Propositions :", font=("Arial", 10, "italic")).pack(pady=4)
        for prop in propositions:
            Button(win, text=prop, width=34,
                command=lambda p=prop: entree.delete(0, END) or entree.insert(0, p)).pack(pady=2)

        def valider():
            q = entree.get()
            if q:
                self.controller.question_courante = q
                question_label.config(text=q)
        Button(win, text="Valider", command=valider).pack(pady=10)


    def ouvrir_dialogue_modif_question(self, win):
        from tkinter.simpledialog import askstring
        question = askstring("Nouvelle question", "Entrer la nouvelle question :", parent=win)
        if question:
            self.controller.question_courante = question  # modifie la vraie question ici !
            win.destroy()


    def page_ajouter_commentaire(self):
        win = Toplevel(self.fenetre)
        win.geometry("350x160")
        win.title("Ajouter un commentaire")
        Label(win, text="Écrire votre commentaire :", font=("Arial", 12)).pack(pady=12)
        entree = Entry(win, width=32)
        entree.pack(pady=8)
        def valider():
            texte = entree.get()
            print("Commentaire ajouté :", texte)
            win.destroy()
        Button(win, text="Valider", command=valider).pack(pady=8)
        Button(win, text="Fermer", command=win.destroy).pack(pady=2)


