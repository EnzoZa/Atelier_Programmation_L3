#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Impôts

#EXERCICE 3
import time

def imposable(sexe, age):
    """ 
    Cette fonction permet de savoir en fonction de l'age et du sexe d'un habitant si il est imposable ou non
    (Homme de plus de 20ans -> Imposable, Femme entre 18 et 35 ans -> Imposable, Reste -> Non Imposable)
    """

    if sexe == "H" and age > 20 or sexe == "F" and age >= 18 and age <= 35 :
        return "Vous êtes imposable"
    else : 
        return "Vous n'êtes pas imposable"


# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    sexe_test = ["H","F","F","F","H"]
    age_test = [20,17,36,19,21]
    resultat_test= ["Vous n'êtes pas imposable","Vous n'êtes pas imposable","Vous n'êtes pas imposable","Vous êtes imposable","Vous êtes imposable"]
    succes = 0
    
    for i in range(0,len(sexe_test)) :
        if imposable(sexe_test[i],age_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = 1
        time.sleep(0.1)

    if succes == 0 :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")


test_unitaire()
sexe = input("Votre sexe (H/F) :")
age = int(input("Votre age: "))
print("Votre salaire sera : {} € ".format(imposable(sexe, age)))

