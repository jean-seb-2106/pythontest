class Compte:

    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    
    def affiche_solde(self):
        print("Le solde du compte de " + self.titulaire + " est de " + str(self.solde) + " €")
    
    def depot(self, montant):
        self.solde = self.solde + montant
    
    def retrait(self, montant):
        if montant <= self.solde:
            print("Retrait accepté")
            self.solde = self.solde - montant
        if montant > self.solde:
            print("Retrait refusé : fonds insuffisants.")
    
    def transfert(self, montant, destinataire):
        if montant <= self.solde:
            destinataire.solde = destinataire.solde + montant
            print("Transfert effectué")
        if montant > self.solde:
            print("Transfert refusé : fonds insuffisants.")
