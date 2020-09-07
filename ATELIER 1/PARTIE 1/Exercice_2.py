#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Impôts

#EXERCICE 3

def imposable(sexe, age):
    """ 
    Ce fonction permet de savoir en fonction de l'age et du sexe d'un habitant si il est imposable ou non
    (Homme de plus de 20ans -> Imposable, Femme entre 18 et 35 ans -> Imposable, Reste -> Non Imposable)
    """

    if sexe == "H" and age > 20 or sexe == "F" and age >= 18 and age <= 35 :
        print("Vous êtes imposable") 
    else : 
        print("Vous n'êtes pas imposable")



sexe = input("Votre sexe (H/F) :")
age = int(input("Votre age: "))
imposable(sexe, age)

