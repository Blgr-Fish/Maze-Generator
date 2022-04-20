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



def get_voisins_case_directions(case, direction) :

    """
    Entrée : Une cases
    Sortie : Une case représentée par un tuple de coordonnées
    Rôle : Indique les coordonnées de la case voisine à la case actuelle dans une direction précise
    """

    temp = None
    if direction == 'O' :
        temp = (case[0]-1,case[1])
        
    if direction == 'E' :
        temp = (case[0]+1, case[1])
        
    if direction == 'N' :
        temp = (case[0] , case[1]-1)
        
    if direction == 'S' :
        temp = (case[0] , case[1]+1)
        
        
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
    

def transformation(test_index , test_card) :
    """
    Entrée :Une liste de tuple de coordonées (index_labyrinthe) et une liste de dictionnaires avec les directions et les booléens (direction_labyrinthe)
    Sortie : Un dictionnaire avec pour clé un tuple de coordonnées et pour valeurs associées à cette clé, les coordonnées des cases voisines directement reliées à la case en question
    Rôle : Tranformer la sortie des fonctions de génération de labyrinthe en un format lisible par l'interprétateur graphique 
    """ 
    relai_direction = ['N','E','S','O']
    
    produit_final = {}
    
    temp = []
    
    for i in range(len(test_card)) :
        for ele in relai_direction :  #On regarde les 4 directions
            if mur_ouvert(test_card[i], ele) == True :  #Si il y a une ouverture dans la direction de la case
                if get_voisins_case_directions(test_index[i], ele) in test_index :
                    temp.append(get_voisins_case_directions(test_index[i], ele))
        produit_final[test_index[i]] =  temp
        temp = []


    return produit_final


def affiche_lab(lab_card,n,m) : # On rentre la liste de citionnaire
    """
    Entrée : Une liste de dictionnaires avec les directions et les booléens (direction_labyrinthe) et les dimensions du labyrinthe
    Sortie : Une chaine de caractères qui représente le labyrinthe
    Rôle : Donne une forme visuellement interpretable du labyrinthe
    """
     
    coins = [" ", "═", "║", "╚", "═", "═", "╝", "╩", "║", "╔", "║", "╠", "╗", "╦", "╣", "╬"]  #On a associé des valeurs binaires pour les directions 
                                                                                              #  Est = 1 ; Nord = 2 ; Ouest = 4 ; Sud = 8
                                                                                              
  
    visual_lab = "\n"
    
    saut_ligne = "\n"
    
    valeur_index = 0
    
    compteur_pour_saut_de_ligne = 0
    
    for i in range(m*n) :  # Les dimension du labyrinthe 
        if lab_card[i]['E'] == True :
            valeur_index += 1
                
        if lab_card[i]['N'] == True :
            valeur_index += 2
                
        if lab_card[i]['O'] == True :
            valeur_index += 4 
    
        if lab_card[i]['S'] == True :
            valeur_index += 8
            
        visual_lab = visual_lab + coins[valeur_index]

        valeur_index = 0 # On réinitialise la valeur à 0
        compteur_pour_saut_de_ligne +=1
        
        if compteur_pour_saut_de_ligne == m : 
            
            visual_lab = visual_lab + saut_ligne    # On saute de ligne
            compteur_pour_saut_de_ligne = 0

    return visual_lab
    

    
def creer_lab_prim(n,m) :  # n est la longueur ( <---> ) et m la largeur   

    index_lab_final = []
    lab_final = []


    for i in range(n) :                 # Axe des abscisses <---> 
        for j in range(n) :             # Axe des ordonnées (vers le haut)
            index_lab_final.append((i,j))
            lab_final.append(creer_case())





    case_actuelle = random.choice(index_lab_final)

    indice_case_actuelle = index_lab_final.index(case_actuelle)

    cases_frontieres = []

    cases_fusionnees = [case_actuelle]

    list_bon_voisin = []  
    
    maze_completed = False
    
    while maze_completed == False :
        for i in range(len(voisins_case_toutes_directions(case_actuelle, index_lab_final))) :
                if voisins_case_toutes_directions(case_actuelle, index_lab_final)[i] not in cases_frontieres :        # Si certains voisins ont déjà marqués commes des cases frontières on ne les ajoutent pas  
                    if voisins_case_toutes_directions(case_actuelle, index_lab_final)[i] not in cases_fusionnees :    # Si les voisins sont déjà reliés (directement ou pas) à la case actuelle, on les ignore 
                        cases_frontieres.append(voisins_case_toutes_directions(case_actuelle, index_lab_final)[i])
    

        if cases_frontieres != [] :  
        
            case_qui_fusionne = random.choice(cases_frontieres) 
        
            indice_case_qui_fusionne =  index_lab_final.index(case_qui_fusionne) #On récupère l'indice de la case qui va fusionner

        
            list_bon_voisin = []
        
            for j in range(len(voisins_case_toutes_directions(case_qui_fusionne , index_lab_final))) :
            
                if voisins_case_toutes_directions(case_qui_fusionne , index_lab_final)[j] in cases_fusionnees :
        
                    list_bon_voisin.append(voisins_case_toutes_directions(case_qui_fusionne , index_lab_final)[j]) #Il peut y avoir plusieurs voisins de la case qui sont déjà fusionné avec tout le monde
                
            case_actuelle = random.choice(list_bon_voisin)
            
            indice_case_actuelle = index_lab_final.index(case_actuelle)
        
            cases_frontieres.remove(case_qui_fusionne)   #On enlève la case dans la liste des voisins

            lab_final[indice_case_actuelle] = ouvrir_mur(lab_final[indice_case_actuelle], direction_fusions_2_cases(case_actuelle, case_qui_fusionne))    # On ouvre le mur entre les deux cases
            
            lab_final[indice_case_qui_fusionne] = ouvrir_mur(lab_final[indice_case_qui_fusionne], direction_inverse(direction_fusions_2_cases(case_actuelle, case_qui_fusionne)))  # On ouvre le mur dans l'autre sens 

            cases_fusionnees.append(case_qui_fusionne)  
        
            case_actuelle = case_qui_fusionne # On change cette case dans la variable pour obtenir ses voisins
        
            indice_case_actuelle = index_lab_final.index(case_actuelle)   #On récupère l'indice de la case
        
    
    

  


        if len(cases_fusionnees) == n*m :  # Quand toutes les cases du labyrinthe ont été fusionnées 
            maze_completed = True
                        
    lab_final.reverse() # Sans le reverse, le premier termes était en bas à droite du labyrinthe
    
    return lab_final
    #return affiche_lab(lab_final , n, m) #--> pour affichage semi-graphique
        
      
#print(creer_lab_prim(3,2))        
       
        
       
        

       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
 
        
       
        
