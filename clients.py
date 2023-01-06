from comptebancaire import Compte #bonne pratique
import comptebancaire as cb

client1 = Compte(titulaire = "Jean",solde = 150)
client2 = cb.Compte(titulaire, solde)
print(client1.titulaire)
print(client1.solde)
client1.affiche_solde()