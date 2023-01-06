class Compte:

    def __init__(self,titulaire,solde):
        self.titulaire = titulaire
        self.solde = solde
    
    def affiche_solde(self):
        print("Le solde du compte de " + str(self.titulaire) + " est de " + str(self.solde) + " €")

