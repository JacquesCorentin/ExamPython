ramdom()
#mots inconnus

mot1 = "castor"
mot2 = "cinema"
mot3 = "cypres"
mot4 = "planer"
mot5 = "retard"
mot6 = "python"
mot7 = "entree"
mot8 = "renard"
mot9 = "soleil"
mot10 = "citron"

mot_joueur = ""
mot_mystere = "citron"

tableau_mystere = ["c","i","t","r","o","n"]
tableau = ["_","_","_","_","_","_"]
tableau_joueur = [""]

#nombre de tour
tour = 0

print(mot1, mot2, mot3, mot4, mot5, mot6, mot7, mot8, mot9,mot10)
print(tableau)

#Définition
def tableaujoueur(tableau_mystere, tableau_joueur):
    for i in range (1,7):
        tableau_joueur[i-1] = input("inscrivez votre mot :")
    return tableau_joueur

def gagner(tableau, tableau_mystere):
	if (tableau_joueur[i-1] = tableau_joueur[1])
	print ("Trouvé !!")
	pass

def perdu(tableau,tableau_mystere):
	if tour >= 8:
		print("partie perdu, vous êtes arrivé au tour :",tour)
	pass


def retry(tableau, tableau_mystere):
	if tableau_joueur != tableau_mystere[1] and tableau_mystere[2] and tableau_mystere[3] and tableau_mystere[4] and tableau_mystere[5] and tableau_mystere[6]:
		tour += 1
		print("essaie encore, vous êtes au tour :",tour)
		pass
	pass
#Début de code
mot_mystere = ramdom(1,10)
mot_joueur = input("inscrivez votre mot :")



	



#Fin de code
#print(mot_joueur)
def function():
	pass

input()