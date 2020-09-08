#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Calcul de frais portuaires

# EXERCICE 5

def frais_portuaire(nom = "Default" ,longueur= -1, categorie = -1):
    """ 
    Cette fonction permet de calculer les frais portuaire annuel d'une place dans un port en fonction de la longueur et de la catégorie du bateau
    """

    PETIT_BATEAU = 5
    MOYEN_BATEAU = 10
    GRAND_BATEAU = 12

    if longueur == -1:
        nom = input("Veuillez saisir le nom de votre bateau : ")
        longueur = float(input("Veuillez saisir la longueur de votre bateau en m :  "))
        categorie = int(input("Veuillez saisir la catégorie de votre bateau (1,2,3) : "))

    cout_mensuel = 100
    taxe_annuel = 100

    if longueur >= PETIT_BATEAU :
        cout_mensuel = 200
    if longueur > MOYEN_BATEAU :
        cout_mensuel = 400
    if longueur > GRAND_BATEAU :
        cout_mensuel = 600

    if categorie == 2 :
        taxe_annuel = 150
    elif categorie == 3 :
        taxe_annuel = 250

    frais = cout_mensuel*12+taxe_annuel
    print("Le coût annuel d'une place au port pour le violier {} est de {} euros".format(nom, frais))
    return frais

# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    longueur_test = [4, 5, 11, 15]
    categorie_test = [1,2,3,1]
    resultat_test= [1300,2550,5050,7300]
    succes = True

    for i in range(0,len(longueur_test)) :
        if frais_portuaire("Default" ,longueur_test[i], categorie_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = False

    if succes == True :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")


test_unitaire()
frais_portuaire()

