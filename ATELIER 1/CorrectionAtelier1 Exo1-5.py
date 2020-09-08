# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:53:12 2020

Fontions demandées dans l'atelier numéro 1
Exercices 1 à 5

Version 1

@author: Ghinevra Comiti
        Johanna Fericean
        Enzo Zampaglione
        Vincent Bonnemayre
"""

#Exercice 1


def salaire():
    """calcule le salaire selon le nombre d'heures effectuées"""
    PALIER_HEURES_1=160
    PALIER_HEURES_2=200
    MAJORATION=0.25
    nb_heures=float(input("Combien d'heures avez-vous fait ?"))
    tx_hor=float(input("Quel est votre taux horaire ?"))
    total=nb_heures*tx_hor #salaire de base, sans majoration 
    if(nb_heures>PALIER_HEURES_1):
        total+=tx_hor*MAJORATION*(nb_heures-PALIER_HEURES_1) #majorations heures supp entre 160 et 200
        if(nb_heures>PALIER_HEURES_2):  #majoration heures supp supérieures à 200
            total+=(nb_heures-PALIER_HEURES_2)*tx_hor*MAJORATION
    return(total)
        
#print(salaire()) 
"""appel de la fonction salaire"""
        
#Exercice2
def asci():
    """indique la catégorie de chaque caractère en fonction de son code ascii"""
    FIN_CAR_SPEC=33 #code de fin des caractères spéciaux
    DEB_CHIFFRES=47 #code de début des chiffres
    FIN_CHIFFRES=58
    DEB_MAJ=64 #code de début des lettres majuscules
    FIN_MAJ=91
    DEB_MIN=96 #code de début des lettres minuscules
    FIN_MIN=123
    car=(input("Entrez le caractère désiré"))
    code=ord(car) #trouve le code ascii du caractère
    if(code< FIN_CAR_SPEC): #si le code ascii est inférieur à 33
         print("c'est un contrôle")
    elif(DEB_CHIFFRES<code<FIN_CHIFFRES): #si le code correspond à un chiffre
         print("c'est un chiffre")
    elif(DEB_MAJ<code<FIN_MAJ):
         print("C'est une lettre majuscule")
    elif(DEB_MIN<code<FIN_MIN):
         print("c'est une lettre minuscule")
    else: #si ça ne correpond pas aux autres caractères, c'est un caractère spécial
        print("c'est un caractère spécial")

#asci(" ") 
"""appel de la fonction asci"""
         
         
#Exercice 3

def impots():
    """détermine si l'habitant est imposable
    sexe=1: homme, sexe=2: femme"""
    AGE_MIN_H=20 #âge minimum pour qu'un homme soit imposable
    AGE_MIN_F=17 #âge minimum pour qu'une femme soit imposable
    AGE_MAX_F=36 #âge macimum pour qu'une femme soit imposable
    SEXE_H= 1 #nombre correspondant aux hommmes
    SEXE_F=2 #chiffre correspondant aux femmes
    sexe=int(input("Quel est le sexe de l'habitant ?")) 
    age=int(input("Quel est l'âge de l'habitant ?"))
    #imp=False #habitant non imposable
    imp=(sexe==SEXE_H and age>AGE_MIN_H)or (sexe==SEXE_F and AGE_MIN_F<age<AGE_MAX_F) #conditions qui font qu'un habitant est imposable
    
    print(imp)

#impots()
"""appel de la fonction impots"""

#Exercice 4

def repro():
    """calcul le coût de la reproduction de photos"""
    """nb_photo est de type entier"""
   
    PALIER_PRIX_1=10 #nombre de photos pour lesquelles s'applique le prix 1
    PRIX_1=0.1 #prix pour une photo si moins de 10 photos
    PALIER_PRIX_2= 30 #limite de photos pour l'application du prix 2
    PRIX_2=0.09 #prix pour une photo de la dixième à la vingtième
    PRIX_3=0.08 #prix pour les photos au-dessus de la trentième
    PRIX_10=1 #le prix des 10 premières photos, en lot
    PRIX_20=1.8 #le prix des 20 photos suivantes, en lot (de la 10ème à la 30ème)
   
    nb_photo=int(input("Combien de photos voulez-vous ?")) 
    
    if(nb_photo<=PALIER_PRIX_1): #s'il y a moins de 10 photos
        total=nb_photo*PRIX_1
    elif(nb_photo<=PALIER_PRIX_2): #si plus de 10 photos, 0.1*10=1
        total=PRIX_10+(nb_photo-PALIER_PRIX_1)*PRIX_2
    else: 
        total= PRIX_10+PRIX_20+(nb_photo-PALIER_PRIX_2)*PRIX_3
    print(total)

#repro()
"""appel de la fonction repro"""

#Exercice 5

def voilier():
    """détermination du coût annuel de la place de port du bateau"""
    PALIER_LONG_1=4 #petit bateau
    PALIER_LONG_2=10 #bateau moyen
    PALLIER_LONG_3=12 #grand bateau
    COUT_BASE=100 #coût de base
    AUGM_1=100 #première augmentation du coût mensuel
    AUGM_2=200 #deuxième augmentation du coût mensuel
    CAT_1=1 #première catégorie
    CAT_2=2 #deuxième catégorie
    CAT_3=3 #troisième catégorie
    TAXE_1=100 #taxe catégorie 1
    TAXE_2=150 #taxe catégorie 2
    TAXE_3=250 #taxe catégorie 3
    NB_MOIS=12 #nombre de mois sur lequel est appliqué le tarif
   
    nom=input("Quel est le nom du voilier ?")
    long=int(input("Quelle est la longueur du voilier ?"))
    cat=int(input("Quelle est la catégorie du voilier ?"))
    
    cout=COUT_BASE 
    if(long>PALIER_LONG_1): #augmentation du coût selon la longueur du bateau
        cout+=AUGM_1
        if(long>PALIER_LONG_2):
            cout+=AUGM_2
            if(long>PALLIER_LONG_3):
                cout+=AUGM_2
    print("Le cout mensuel est"+str(cout))
    taxe=0 #détermination de la taxe selon la catégorie
    if(cat==CAT_1):
        taxe=TAXE_1
    elif(cat==CAT_2):
        taxe=TAXE_2
    elif(cat==CAT_3):
        taxe=TAXE_3
    else:
        print("la categorie est incorrecte") #si la catégorie n'est pas valide
    cout_ann=taxe+cout*NB_MOIS
    phrase="Le cout annuel d'une place de port pour le voilier "+nom+" est de"+str(cout_ann)+"euros"
    print(phrase)
    
#voilier()