#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Détéction de caractère

#EXERCICE 2

def char_analyser(char:str)->str:
    """ 
    Cette fonction permet de : vérifier le type de caracter qui est entré.
    -> Si c'est une lettre majuscule alors son code ascii est compris entre 65 et 91
    -> Si c'est une lettre minuscule alors son code ascii est compris entre 97 et 123
    -> Si c'est un chiffre alors son code ascii est compris entre 48 et 58
    -> Sinon on considère que c'est un caractère spécial
    """

    PALIER = [[48,58,"un nombre"],[65,91,"une majuscule"],[97,123,"une minuscule"]]
    result = "un caractère spécial"
    char_ascii = ord(char)
    
    for i in range(len(PALIER)): 
        if char_ascii >= PALIER[i][0] and char_ascii < PALIER[i][1]:
            result = PALIER[i][2]

    return result

def test_unitaire(): # Fonction comparant le résultat obtenue et attendue dans les cas les plus significatif.
    car_test = ["a", "B", "#", "1", "5", "G", "@", "$"]
    car_awaited_res = ["une minuscule", "une majuscule", "un caractère spécial", "un nombre", "un nombre", "une majuscule", "un caractère spécial", "un caractère spécial"]

    for i in range (0, len(car_test)) :  
        if char_analyser(car_test[i]) == car_awaited_res[i]:
            print(">",end="")
        else : 
            print("X",end="")
 

#Appel des fonctions
test_unitaire()
char = input("\nVeuillez saisir un caractère : ")
print("Vous avez saisie {}".format(char_analyser(char)))