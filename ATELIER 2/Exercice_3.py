#Auteur : Jean-François Giammari & Axel Frau
#Date : 07/09/2020 
#Version : 1
#Description : Résolution d'une équation du second degré

#EXERCICE 3

import math

def discrimitant(a:float,b:float,c:float)->float :
    """ 
     Cette fonction permet de calculer le discriminant
    """
    return b*b - (4*a*c)

def racine_unique(a,b)->float :
    """ 
     Cette fonction permet de calculer la racine unique
    """
    return (-1*b)/2*a


def racine_double(a:float,b:float,delta:float,num:float)->float :
    """ 
     Cette fonction permet de calculer la racine double
    """
    result = 0
    if num == 1 :
        result = ((-1*b)+math.sqrt(delta))/2*a
    else :
        result = ((-1*b)-math.sqrt(delta))/2*a

    return result


def str_equation(a:float,b:float,c:float) :
    a = str(a)
    b = str(b)
    c = str(c)
    if int(a) == 1 :
        a = "x2"
    elif int(a) == -1 :
        a = "-x2"
    elif int(a) < -1 :
        a = " "+a+"x2"
    elif int(a) > 1 :
        a = a+"x2"
    elif int(a) == 0:
        a = 0

    if int(b) == 1 :
        b = " + x "
    elif int(b) == -1 :
        b = " - x "
    elif int(b) < -1 :
        b = " "+b+"x "
    elif int(b) > 1 :
        b = " + "+b+"x "
    elif int(b) == 0:
        b = " "

    if int(c) > 1 :
        c = "+ "+c
    elif int(c) == 0 :
        c =" "
    elif int(c) < -1 :
        c = " "+c
        
    return a + b + c

def solution_equation(a:float,b:float,c:float)->float :
    determinant = discrimitant(a,b,c)
    message = "Aucune solution réelle"
    if determinant == 0 :
        message = "Solution de l'équation : " + str_equation(a,b,c) + "\n Racine Unique =" + str(racine_unique(a,b))
    elif determinant >0 :
        message = "Solution de l'équation : " + str_equation(a,b,c) + "\n x1 =" +str(racine_double(a,b,determinant,1))  + "\n x2 =" +str(racine_double(a,b,determinant,2))

    print(message)



solution_equation(6,10,3)