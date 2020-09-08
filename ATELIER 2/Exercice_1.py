# Auteur : Jean-François Giammari & Axel Frau
# Date : 08/09/2020
#Version : 1
# Description : Calcul d'IMC

# EXERCICE 1

def message_imc(imc: float) -> str:
    """ 
    Cette fonction permet d'interpréter l'état de santé d'une personne en fonction de son IMC
    """
    message = "dénutrition ou famine"
    if imc > 16.5:
        message = "maigreur"
    if imc > 18.5:
        message = "corpulence normale"
    if imc > 25:
        message = "surpoids"
    if imc > 30:
        message = "obésité modérée"
    if imc > 35:
        message = "obésité sévère"
    if imc > 40:
        message = "obésité morbide"

    return message


def test_unitaire():
    imc_test = [16, 17, 19, 26, 31, 36, 45]
    resultat_test = ["dénutrition ou famine", "maigreur", "corpulence normale",
                     "surpoids", "obésité modérée", "obésité sévère", "obésité morbide"]
    succes = True

    for i in range(0, len(imc_test)):
        if message_imc(imc_test[i]) == resultat_test[i]:
            print(">", end="")
        else:
            print("X", end="")
            succes = False

    if succes == True:
        print(" TEST IS SUCCES")
    else:
        print(" TEST IS FAILED")


test_unitaire()
print("Actuellement vous êtes diagnostiquer avec un état de ",
      message_imc(float(input("Entrer votre IMC : "))))
