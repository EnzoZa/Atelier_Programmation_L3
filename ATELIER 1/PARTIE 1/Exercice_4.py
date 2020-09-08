#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Reprographie

#EXERCICE 4
"""
Cette exerice permet de calculer rapidement le prix d'impression de photocopie en sachant que après 10 photocopies
elles ne coutent plus 0.10€ mais 0.9€ et après 20 photocopies de plus c'est à dire après 30 photocopies elles coutent 
0.08€

Ici j'ai décidé de faire pour chaques tranches de prix la vérification du nombre de photocopies restantes ainsi quand la tranche
finale est atteinte je return le prix total en l'arondissant à la deuxième décimal.

"""
def exercice_4(nbr_photocopie):
    if nbr_photocopie < 0 :
        return 0.0
    if nbr_photocopie <= 10:
        prix = nbr_photocopie * 0.10
        res = round(prix, 2)
    else :
        prix = 10 * 0.10
        nbr_photocopie_remaining = nbr_photocopie - 10
        if nbr_photocopie_remaining <= 20 :
            prix += nbr_photocopie_remaining * 0.09
            res = round(prix, 2)
        else :
            prix += 20 * 0.09
            nbr_photocopie_remaining -= 20
            prix += nbr_photocopie_remaining * 0.08
        res = round(prix, 2)
    return res

def test_unitaire():
    nbr_photoco_test = [-1, 0, 100, 10, 30, 667, 45, 27]
    nbr_photoco_res = [0.0, 0.0, 8.4, 1.0, 2.8, 53.76, 4.0, 2.53]
    success = True
    for i in range (0, len(nbr_photoco_test)) :  
        if exercice_4(nbr_photoco_test[i]) == nbr_photoco_res[i]:
            print(">",end="")
        else : 
            print("X",end="")
            success = False
    
    if success == True :
        print(" TEST IS SUCCESSFUL")
    else :
        print(" TEST FAILED")

test_unitaire()
nbr_photoco = int(input('Combien de photocopie voulez vous ? '))
print("Le prix total pour", nbr_photoco, "photocopie(s) est de " + str(exercice_4(nbr_photoco)) + "€")
