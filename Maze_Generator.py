#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:50:10 2022

@author: Maël Pierre Ziad
"""

import random

class Graphe_dictionnaire:

    def __init__(self):               # On initialise un dictionnaire vide
        self.A = {}


    def __repr__(self):               # méthode repr pour afficher le graphe
        return str(self.A)


    def voisins(self, x):             # montre les voisins d'un noeud
        return self.A[x]


    def ajouter_sommet(self,x):       # ajoute un noeud 
         self.A.update({x:[]})
    

    def ajouter_arete(self,x, y):     # ajoute une arrête entre 2 noeuds
        if x != y:                    # pour pas qu'on puisse faire une arrete avec le meme noeud
            if y not in self.A[x]:
                self.A[x].append(y)
           
                if x not in self.A[y]:    # pour les graphes non orientés 
                    self.A[y].append(x)   

    
    def creer_graphe_nxn(self,n):    # créer un graphe de n x n taille 
        assert type(n) == int
        assert n >= 1
        self.n = n
        for i in range(self.n):
            for j in range(self.n):
                self.ajouter_sommet((i,j))


   
    def fusion_aleatoire(self):
        maze_completed = False # Passe à True quand le labyrinthe est complet
        liste_valeurs = [] # Liste des valeurs attribuées à chaque noeud du graphe, de 0 à la longueur du graphe
        longueur = len(self.A) # Longueur du Graphe


        for i in range (longueur):
            liste_valeurs.append(i) # on assigne une valeur unique à une cellule, de 0 à len du graphe


        self.nombre_coups = 0 # compteur d'étapes pour la réalisation du labyrinthe

        while not maze_completed :
            random_cell = random.choice(list(self.A)) # un noeud random du graphe...
            random_index = list(self.A).index(random_cell) #... et son index
            cote_choisi = random.randint(1,4) # 1 = bas, 2 = haut, 3 = gauche et 4 = droite
            #print(liste_valeurs)

            if cote_choisi == 1 and random_cell[0] != 0: # si ça va vers le bas et que c'est à l'index 0 on peut pas descendre plus bas
                random_index_1 = list(self.A).index((random_cell[0]-1,random_cell[1])) # l'index de la cellule du dessous
                
                if liste_valeurs[random_index_1] != liste_valeurs[random_index]: # on vérifie que la valeur attribuée au noeud du dessous est différent de celle du noeud choisi
                    self.ajouter_arete(random_cell,(random_cell[0]-1,random_cell[1])) # et on les joints par une arrête

                    for i in range(longueur) : 
                        
                        if liste_valeurs[i] == liste_valeurs[random_index_1]: # on s'assure que toutes les autres cellules ayant la même valeur soient modifiées
                            liste_valeurs[i] = liste_valeurs[random_index]
                    
                    self.nombre_coups +=1

           
            elif cote_choisi == 2 and random_cell[0] != (self.n)-1 : # pour le haut
                random_index_2 = list(self.A).index((random_cell[0]+1,random_cell[1]))
                
                if liste_valeurs[random_index_2] != liste_valeurs[random_index]:
                    self.ajouter_arete(random_cell,(random_cell[0]+1,random_cell[1]))
                    
                    for i in range(longueur) :

                        if liste_valeurs[i] == liste_valeurs[random_index_2]:
                            liste_valeurs[i] = liste_valeurs[random_index]
                    
                    self.nombre_coups +=1

            
            elif cote_choisi == 3 and random_cell[1] != 0 : # pour la gauche
                random_index_3 = list(self.A).index((random_cell[0],random_cell[1]-1))

                if liste_valeurs[random_index_3] != liste_valeurs[random_index] :
                    self.ajouter_arete(random_cell,(random_cell[0],random_cell[1]-1))

                    for i in range(longueur) :

                        if liste_valeurs[i] == liste_valeurs[random_index_3]:
                            liste_valeurs[i] = liste_valeurs[random_index]        
                
                    self.nombre_coups +=1

            
            elif cote_choisi == 4 and random_cell[1] != (self.n)-1 : # pour la droite
                random_index_4 = list(self.A).index((random_cell[0],random_cell[1]+1)) 

                if liste_valeurs[random_index_4] != liste_valeurs[random_index] :
                    self.ajouter_arete(random_cell,(random_cell[0],random_cell[1]+1))

                    for i in range(longueur) :

                        if liste_valeurs[i] == liste_valeurs[random_index_4]:
                            liste_valeurs[i] = liste_valeurs[random_index]
                   
                    self.nombre_coups +=1
          
            

            if all(element == liste_valeurs[0] for element in liste_valeurs): # on vérifie que le nombre de valeurs égales à liste_valeurs[0] soit égal à la longueur de la liste
                maze_completed = True # si c'est le cas, ça veut dire que toutes les valeurs sont les mêmes et donc que le labyrinthe est terminé

        #return "Labirynthe effectué en : " + str(self.nombre_coups) + " essais."


#TESTS
a=1
while True:
    G = Graphe_dictionnaire()
    G.creer_graphe_nxn(5)
    G.fusion_aleatoire()
    
    print("labyrinthe n°" + str(a))
    if G.nombre_coups == ((G.n)**2)+1:
        print(G.__repr__())
        print(G.nombre_coups)
        break
    a+=1


#     0  1  2  3
#  0  00 01 02 03
#  1  10 11 12 13
#  2  20 21 22 23
#  3  30 31 32 33