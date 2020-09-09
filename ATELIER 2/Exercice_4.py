#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Calcul de Dates
import datetime
import Exercice_2
#EXERCICE 4
"""
Cet ensemble de fonction nous permet de verifier au final si une personne est majeur ou non, on va faire 
appelle a fonction depuis un autre fonction pour tester la validité des données saisies.
"""
def date_est_valide(day,month,year) :
    if month > 12 or month < 1:
        return False

    if Exercice_2.est_bissextile(year) and month == 2:
        if day > 29 or day < 1:
            return False
        else:
            return True
    elif not Exercice_2.est_bissextile(year) and month == 2:
        if day > 28 or day < 1:
            return False
        else:
            return True
    else:
        if (not (month % 2) and month != 7) and (day > 31 or day < 1):
            return False
        elif ((month % 2) and month != 7) and (day > 30 or day < 1) :
            return False
        else: 
            return True

def saisie_date_naissance(day,month,year) :
    if date_est_valide(day,month,year) :
        return datetime.date(year,month,day)
    else : 
        return False

def age(birthdate) :
    today = datetime.datetime.today()
    print(((today.month, today.day) < (birthdate.month, birthdate.day)))
    #Comme false = 0 et true = 1 alors je l'utilise pour décrementer ou non l'age en fonction du mois et du jour.
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)) 
    return age

def est_majeur(birthdate) :
    if age(birthdate) >= 18 :
        return True
    else :
        return False

def test_access() :
    day = int(input("Veuillez rentrer jour de naissance : "))
    month = int(input("Veuillez rentrer mois de naissance (en chiffre) : "))
    year = int(input("Veuillez rentrer année de naissance : "))
    age_res = age(saisie_date_naissance(day,month,year))
    majeur_res = est_majeur(saisie_date_naissance(day,month,year))
    if majeur_res :
        print("Bonjour, vous avez", age_res ,"ans, Accès autorisé")
    else :
        print("Désolé, vous avez", age_res ,"ans, Accès interdit")

test_access()




