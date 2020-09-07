#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Calcule Salaire

#EXERCICE 1



def calculer_salaire(nombre_heures,salaire_horaire ):
    """ 
    Cette fonction permet de calculer le salaire a partir du salaire horaire et du nombre d'heure de travail, en prenant en compte les majorations des heures supplémentaires
    (25% au-delà de 160h, 50% au-delà de 200h)
    """
    salaire = 0.0
    if nombre_heures > 160 : 
        salaire = 160 * salaire_horaire
        nombre_heures-=160
        if nombre_heures > 40 : 
            salaire = salaire + (40 * (salaire_horaire*1.25))
            nombre_heures-=40
            salaire += (nombre_heures * (salaire_horaire*1.50))
        else :
            salaire += (nombre_heures * (salaire_horaire*1.25))
    else :
        salaire = nombre_heures * salaire_horaire
    
    return salaire
    
   

# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    horaire_test = [0,10,0,10,159,165,200,210]
    salaire_test = [0,0,10,10,10,10,10,10]
    resultat_test= [0,0,0,100,1590,1662.5,2100,2250]
    succes = False
    for i in range(0,len(horaire_test)) :
        if calculer_salaire(horaire_test[i],salaire_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = True

    if succes == False :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")
    

test_unitaire()
nombre_heures = int(input("Votre nombre d'heure :"))
salaire_horaire = int(input("Votre salaire horaire :"))
print("Votre salaire sera : {} € ".format(calculer_salaire(nombre_heures,salaire_horaire )))





