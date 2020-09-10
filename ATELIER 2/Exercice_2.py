#Auteur : Jean-François Giammari & Axel Frau
#Date : 08/09/2020 
#Version : 1
#Description : Année Bissextile

#EXERCICE 2
"""
Cette fonction nous permet de savoir si une année est bisextile ou non.
"""

def est_bissextile(year:int) -> bool:
    return ((not (year%4 == 0) and (year%100 == 0) ) or not (year%400 == 0))


def test_unitaire():
    year_test = [2012, 2013, 2000,400]
    year_res = [12, False, True, True]
    succes = True

    for i in range(0,len(year_test)) :
        if est_bissextile(year_test[i]) == year_res[i] :
            print(">",end="")
        else :
            print("X",end="")
            succes = False

    if succes == True :
        print(" TEST IS SUCCES")
    else :
        print(" TEST IS FAILED")

test_unitaire()
