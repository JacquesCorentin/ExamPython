from colorama import init
init()
from colorama import Force, Black, Style

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



#nombre de tour
tour = 0

#tableaux
tableau_mystere = ["c","i","t","r","o","n"]
tableau_joueur = ["_","_","_","_","_","_"]
print(mot1, mot2, mot3, mot4, mot5, mot6, mot7, mot8, mot9,mot10)
print(tableau)
print("vous avez 8 tours pour trouver la solution, vous êtes au tour :" tour)

#Début de code
def tableaujoueur(tableau_mystere, tableau_joueur):
    for i in range (1,7):
        tableau_joueur[i-1] = input("inscrivez votre mot :")
    return tableau_joueur

def choixdecaractere (tableau_mystere, tableau_joueur, verif)
    for i in range (1,7):
        if tableau_joueur != tableau_mystere:
            verif = 2
        if tableau_joueur[i-1] != tableau_mystere[1] and tableau_mystere[2] and tableau_mystere[3] and tableau_mystere[4] and tableau_mystere[5] and tableau_mystere[6]:
            verif = 1
        if verif = 2 : 
        	tour += 1
            print("Try again")
            print ("vous êtes au tour :" tour)
    return


def gagner(tableau_mystere, tableau_joueur):
	for i in range (1,7):
		if tableau_joueur[i-1] == tableau_mystere[1] and tableau_mystere[2] and tableau_mystere[3] and tableau_mystere[4] and tableau_mystere[5] and tableau_mystere[6]:
            verif = 3
            print ("vous êtes au tour ",tour)
			print ("Trouvé !!")
	return
	

def retry(tableau_mystere, tableau_joueur):
	for i in range (1,7):	
		if tableau_joueur[i-1] == tableau_mystere[1] or tableau_mystere[2] or tableau_mystere[3] or tableau_mystere[4] or tableau_mystere[5] or tableau_mystere[6]:
            verif = 1
            tour += 1
			print("essaie encore, vous êtes au tour :",tour)
	return


def perdu(tableau_mystere, tableau_joueur):
	for i in range (1,7):
		if tour >= 8:
			print("partie perdu, vous êtes arrivé au tour :",tour)
	return




#Fin de code
#print(mot_joueur)
deftableaujoueur (tableau_mystere, tableau_joueur)
defperdu (tableau_mystere, tableau_joueur)
defretry (tableau_mystere, tableau_joueur)
defgagner (tableau_mystere, tableau_joueur)
defchoixdecaractere (tableau_mystere, tableau_joueur)
verif=3
print(tableau_joueur)
input()