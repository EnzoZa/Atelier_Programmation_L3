# Auteur : Jean-François Giammari & Axel Frau
# Date : 08/09/2020
#Version : 1
# Description : Compagnie d'assurance automobile

# EXERCICE 8

def tarification(age="", annee_permis="", nbr_accidents="", annee_assure=""):
    """ 
    Cette fonction permet de definir la famille d'assurance que peut obtenir un client en fonction de sont age, du nombre d'année de permis, 
    du nombre d'accidents, et du nombre d'année assuré dans cette assurance

    """
    if age == "":
        while age.isdigit() == False:
            age = input("Veuillez saisir votre age : ")
        while annee_permis.isdigit() == False:
            annee_permis = input(
                "Veuillez saisir le nombre d'année ou vous avez été titulaire de votre permis : ")
        while nbr_accidents.isdigit() == False:
            nbr_accidents = input("Veuillez saisir votre nombre d'accident: ")
        while annee_assure.isdigit() == False:
            annee_assure = input(
                "Veuillez saisir votre nombre d'année assurer chez nous : ")

    tarif_name = ["Refuser", "Bleu", "Vert", "Orange", "Rouge"]
    tarif = 4
    age = int(age)
    annee_permis = int(annee_permis)
    nbr_accidents = int(nbr_accidents)
    annee_assure = int(annee_assure)

    if age < 25:
        if nbr_accidents > 0:
            tarif = 0
        else:
            if annee_permis > 2:
                tarif = 3
    else:
        if annee_permis > 2:
            if nbr_accidents == 0:
                tarif = 2
            elif nbr_accidents ==1:
                tarif = 3
            elif nbr_accidents > 2:
                tarif = 0
        else:
            if nbr_accidents == 0:
                tarif = 3

    if annee_assure > 1 :
        if tarif != 0 and tarif-1 > 0 :
            tarif -=1
 


    if tarif > 0 :
        print("Votre assurance accepte de vous assurer avec le tarif {}".format(tarif_name[tarif]))
    else :
        print("Votre assurance a refuser de vous assurer")
    return tarif_name[tarif]



# test_unitaire() lance une série de tests comparant le résultat obtenue et attendue dans les cas les plus significatif.
def test_unitaire():
    age_test = [20, 20, 20,20, 26, 30, 32, 34, 35,26]
    accidents_test= [1,0,0,0,1, 0, 1, 2, 6,0]
    apermis_test = [1,1,4,4,1,3,4,5,6,1]
    aassure_test= [0,2,0,3,0,0,0,2,3,2]
    resultat_test = ["Refuser","Orange", "Orange", "Vert", "Rouge", "Vert","Orange","Orange","Refuser","Vert"]
    succes = True

    for i in range(0,len(age_test)) :
        if tarification(age_test[i], apermis_test[i], accidents_test[i], aassure_test[i]) == resultat_test[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = False

    if succes == True :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")




test_unitaire()
tarification()