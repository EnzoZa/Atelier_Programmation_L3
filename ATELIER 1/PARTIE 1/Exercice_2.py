#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Détéction de caractère

#EXERCICE 2

def exercice_2(char):
    """ 
    Cette fonction permet de : vérifier le type de caracter qui est entré.
    (Si c'est une lettre majuscule alors son code ascii est compris entre 65 et 91)
    (Si c'est une lettre minuscule alors son code ascii est compris entre 97 et 123)
    (Si c'est un chiffre alors son code ascii est compris entre 48 et 58)
    (Sinon on considère que c'est une caractère spécial)
    """
    if len(char) < 1:
        print("Vous avez rentrer plus d'un caractère veuillez recommencer avec 1 seul !")
        return "wrong input"
    else:
        char_ascii = ord(char)
        if 48 >= char_ascii < 58 :
            return "number"
        elif 65 >=char_ascii < 91 :
            return "uppercase"
        elif 97 >= char_ascii < 123:
            return "lowercase"
        else :
            return "special"

def test_unitaire():
    car_test = ["a", "B", "#", "1", "5", "G", "@", "$"]
    car_awaited_res = ["lowercase", "uppercase", "special", "number", "number", "uppercase", "special", "special"]
    succes = True
    for i in range (0, len(car_test)) :  
        if exercice_2(car_test[i]) == car_awaited_res[i]:
            print(">",end="")
        else : 
            print("X",end="")
            succes = False
    
    if succes == True :
        print(" TEST IS SUCCESSFUL")
    else :
        print(" TEST FAILED")

test_unitaire()
character = input("rentrer un caractère : ")
res = exercice_2(character)
if res == "number" :
    to_print = "un chiffre"
elif res == "uppercase" :
    to_print = "Une lettre majuscule"
elif res == "lowercase" :
    to_print = "une lettre minuscule"
else:
    to_print = "un caractère spécial"
print("charactère rentré est ", to_print)