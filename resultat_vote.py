class Resultat:
    def __init__(self):
        self.nb_incr = 0
        self.nb_bien = 0
        self.nb_bof = 0
        self.nb_berk = 0

    def calculer_statistique(self, votes):
        for vote in votes:
            if vote == 1:
                self.nb_incr += 1
            elif vote == 2:
                self.nb_bien += 1
            elif vote == 3:
                self.nb_bof += 1
            elif vote == 4:
                self.nb_berk += 1
       