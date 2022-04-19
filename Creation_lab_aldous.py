# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:03:21 2022

@author: Maël Ziad Pierre
"""

import random

def creer_case() :
    """
    Entrée : Rien
    Sortie : Un dictionnaire 
    Rôle : Créer des dictionnaires qui représentent les cases et si elles sont ouvertes dans une direction
    """
    return {'N' : False,'E': False , 'S' : False,'O' : False} # Dans cet ordre : {'Nord':False, 'Est':False, 'Sud':False, 'Ouest':False}


    
def mur_ouvert(case, direction) :
    """
    Entrée : Une case  (avec le dictionnaire des directions) et une direction (N,E,S,O) 
    Sortie : Un booléens
    Rôle : Indique si il y a une liaison dans la direction indiqué pour la case
    """
    temp = None
    if case[direction] == False :
        temp = False
    else :
        temp = True
    return temp

def mur_ferme(case, direction) :
    """
    Entrée : Une case  (avec le dictionnaire des directions) et une direction (N,E,S,O) 
    Sortie : Un booléens
    Rôle : Indique si il y a une cloison dans la direction indiqué pour la case
    """
    temp = None
    if case[direction] == False :
        temp = True
    else :
        temp = False
    return temp

def ouvrir_mur(case, direction) :
    """
    Entrée : Une case  (avec le dictionnaire des directions) et une direction (N,E,S,O) 
    Sortie : Un dictionnaire avec les directions et les booléens
    Rôle : Tansforme les murs fermés en murs ouverts et ne fait rien si les murs sont déjà ouverts 
    """
    if case[direction] == False :
        case[direction] = True 
    return case


def fermer_mur(case, direction) :
    """
    Entrée : Une case  (avec le dictionnaire des directions) et une direction (N,E,S,O) 
    Sortie : Un dictionnaire avec les directions et les booléens
    Rôle : Tansforme les murs ouverts en murs fermés et ne fait rien si les murs sont déjà fermés 
    """
    if case[direction] == True :
        case[direction] = False 
    return case

def valeurs_hasard(b) :
    """
    Entrée : Un entier qui corespondait au dimensions du labyrinthe
    Sortie : Une liste d'entier tous différents
    Rôle : obtenir une liste d'entiers pour le tri fusion
    """
    liste_val = []
    while len(liste_val) != b**2 :   
        temp = random.randint(0,b**2)
        if temp not in liste_val :
            liste_val.append(temp)
    return liste_val


def direction_inverse(direction) :
    """
    Entrée : Une direction (N,E,S,O) 
    Sortie : Une direction (N,E,S,O) opposée à celle qui est entrée (O,S,E,N)
    Rôle : Donne la direction inverse
    """
    temp = None      
    if direction == 'N' :
        temp = 'S'
        
    elif direction == 'E' :
        temp = 'O'
        
    elif direction == 'S' :
        temp = 'N'
        
    elif direction == 'O' :
        temp = 'E'
    
    return temp


        

def voisins_case_toutes_directions(case, index_lab_final) :
    """
    Entrée : Une case (avec le tuple de coordonnées) et une liste de tuples de coordonées (= la labyrinthe)
    Sortie : Une liste de tuples de coordonnées qui sont les voisins de la case
    Rôle : Indique les voisins de la case si ils sont dans le dictionnaire
    """
    list_voisins = []
    if (case[0],case[1]-1) in index_lab_final :
        list_voisins.append((case[0],case[1]-1))
        
    if (case[0]+1,case[1]) in index_lab_final :
        list_voisins.append((case[0]+1,case[1]))

    if (case[0],case[1]+1) in index_lab_final :
        list_voisins.append((case[0],case[1]+1))

    if (case[0]-1,case[1]) in index_lab_final :
        list_voisins.append((case[0]-1,case[1]))
    return list_voisins


def direction_fusions_2_cases(case1, case2) :  #Case1 --> case actuel et Case2 --> case d'arrivée
    """
    Entrée : Deux cases qui doivent êtres voisines
    Sortie : Une direction (N,E,S,O)
    Rôle : Indique la direction de la case2 par rapport à la case1 
    """

    direction = None
    if case1[0] == case2[0] and case1[1] == case2[1]-1 :
        direction = 'O'
    if case1[0] == case2[0] and case1[1] == case2[1]+1 :
        direction = 'E'
    if case1[0] == case2[0]-1 and case1[1] == case2[1] :
        direction = 'N'
    if case1[0] == case2[0]+1 and case1[1] == case2[1] :
        direction = 'S'
        
    return direction
    

def transformation(index_labyrinthe) :
    """
    Entrée :Une liste de tuple de coordonées (index_labyrinthe) et une liste de dictionnaires avec les directions et les booléens (direction_labyrinthe)
    Sortie : Un dictionnaire avec pour clé un tuple de coordonnées et pour valeurs associées à cette clé, les coordonnées des cases voisines directement reliées à la case en question
    Rôle : Tranformer la sortie des fonctions de génération de labyrinthe en un format lisible par l'interprétateur graphique 
    """
    lab_final_lisible = {}
    
    for i in range(len(index_labyrinthe)) :
        
        lab_final_lisible[index_labyrinthe[i]] =  voisins_case_toutes_directions(index_labyrinthe[i] , index_labyrinthe)
    
   
    return lab_final_lisible



    
def creer_lab_Aldous_frerot(n) :
    """
    Entrée : Un entier qui donne les dimensions du labyrinthe 
    Sortie : Une liste de dictionnaires avec les directions et les booléens (le tout forme un labyrinthe) 
    Rôle : Créer un labyrinthe avec l'algorithme d'aldous-Broder 
    """
    index_lab_final = []    # La liste des tuples de coordonées
    lab_final = []          # La liste des cases avec les dicos qui donnent les murs (ouverts/fermés) 
    cases_visitees = []     #la liste des cases visitees
    
    maze_completed = False
    
    
    for i in range(n) :                 # Axe des abscisses <---> 
        for j in range(n) :             # Axe des ordonnées (vers le haut)
            index_lab_final.append((i,j))  # On créer une liste de tuples qui sont les coordonnées des cases
            lab_final.append(creer_case()) # On crée une liste de dictionnaires 
            
    case_actuelle = random.choice(index_lab_final)    #La 1er case est une case au hasard dans le labyrinthe
    indice_case_actuelle = index_lab_final.index(case_actuelle)   #On récupère l'indice de la case
    cases_visitees.append(case_actuelle) #On considère la case de départ comme visitée
    
    while maze_completed == False :
        cases_voisines_case_actuelle = voisins_case_toutes_directions(case_actuelle, index_lab_final)  #On met dans une variable les cases voisines à la case actuelle
              
        case_voisine_choisie = random.choice(cases_voisines_case_actuelle)  # On prend une case au hasard parmis les cases voisines de la case actuelle  
        indice_voisin_case_actuelle = index_lab_final.index(case_voisine_choisie) # On prend aussi l'indice de la case voisine
        
        if case_voisine_choisie not in cases_visitees : # Si la case en question n'est pas encore reliés aux autres
            
         
            lab_final[indice_case_actuelle] = ouvrir_mur(lab_final[indice_case_actuelle], direction_fusions_2_cases(case_actuelle, case_voisine_choisie))    # On ouvre le mur entre les deux cases
            
            
            lab_final[indice_voisin_case_actuelle] = ouvrir_mur(lab_final[indice_voisin_case_actuelle], direction_inverse(direction_fusions_2_cases(case_actuelle, case_voisine_choisie)))  # On ouvre le mur dans l'autre sens 
        

        
        case_actuelle = case_voisine_choisie #On reprend une nouvelle case qui est la voisine que l'on a  fusionnée (ou pas)
        indice_case_actuelle = index_lab_final.index(case_actuelle)    #On récupère le nouvelle indice de cette case


        if case_voisine_choisie not in cases_visitees :
            cases_visitees.append(case_voisine_choisie) #On marque la case comme visité si on ne la pas déjà fait avant (pour qu'il n'y ait pas de doublons)
         
            
         
        if len(cases_visitees) == n**2 : # Quand on a visités toutes les cases c'est fini 
            maze_completed = True
    
    lab_final.reverse() # Sans le reverse, le premier termes était en bas à droite du labyrinthe
    
    
    
    return transformation(index_lab_final)  # Sors un format lisible pour l'interpreteur graphique 
        
       
        
       





        
       
print(creer_lab_Aldous_frerot(4))        
       
        
       
        
       
        
       
 
        
       
        
