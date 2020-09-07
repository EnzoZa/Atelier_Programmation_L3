#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Concessionnaire automobile

#EXERCICE 6

def frais_mensuel(kilometre,type_carburant,cylindre,prix_caburant):
    """ 
   Cette fonction permet de savoir les frais mensuels d'utilisation des voitures d'un concessionnaire
   en fonction du nombre de kilomètres parcourue en une année, le type de carburant, la cylindrée et le prix du carburant
    """

    frais_mensuel = 0
    surcout = 1.50
    consommation = 8

    if cylindre > 2000 :
        consommation = 10
    elif type_carburant == "D":
        surcout = 1.70
    
    frais_mensuel = ((kilometre/100) * (consommation*prix_caburant) * surcout) / 12
    return frais_mensuel 

# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    kilometre_test = [5000,6500,1500]
    type_carburant_test = ["E","E","D"]
    cylindre_test = [1500,2300,0]
    prix_caburant_test = [1.20,2.30,5]
    resultat_test= [60,186.875,85]
    succes = True

    for i in range(0,len(kilometre_test)) :
        if frais_mensuel(kilometre_test[i],type_carburant_test[i],cylindre_test[i],prix_caburant_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = False

    if succes == True :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")


test_unitaire()
kilometre = float(input("Nombre de kilomètres que vous parcourer en une année : "))
type_carburant = input("Votre type de caburant utiliser (D/E - Diesel/Essence) : ")
cylindre = int(input("La cylindrée de votre voiture en cm3 (Inconnu = 0): "))
prix_caburant = float(input("Le prix du carburant : "))

print("Vos frais mensuels seront de {} € ".format(frais_mensuel(kilometre,type_carburant,cylindre,prix_caburant)))