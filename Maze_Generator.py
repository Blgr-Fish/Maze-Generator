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
        if y not in self.A.keys():
            self.ajouter_sommet(y)    # on vérifie que le noeud y existe ou pas dans le graphe
            
        if x != y:                    # pour pas qu'on puisse faire une arrete avec le meme noeud
            self.A[x].append(y)
           
            if x not in self.A[y]:    # pour les graphes non orientés 
                self.A[y].append(x)


    def creer_graphe4x4(self):        # créer un labyrinthe un graphe en 4x4 avec 16 noeuds isolés
        for i in range(4):            # servira pour l'initialisation du labyrinthe
            for j in range(4):
                self.ajouter_sommet(str(i)+str(j))


    def wilson(self):
        maze_completed = False
        self.first_cell = random.choice(list(self.A)) # créer la cellule initiale de manière aléatoire
        sommets_verifies = [self.first_cell]

        while not maze_completed:
            self.random_cell = random.choice(list(self.A))
            if self.random_cell not in  sommets_verifies:     # si la cellule choisie au hasard n'est pas dans les sommets verifies
                sommets_verifies.append(self.random_cell)     # on ajoute la random_cell dans les sommets visites
                
                # il faut faire en sorte de rejoindre random_cell et first_cell maintenant
        
        





#TESTS

G = Graphe_dictionnaire()

"""G.ajouter_sommet('A')
G.ajouter_sommet('B')
G.ajouter_sommet('C')
G.ajouter_sommet('D')

G.ajouter_arete('A','B')
G.ajouter_arete('A','C')
G.ajouter_arete('A','D')
G.ajouter_arete('A','A') # ne marche pas car même valeur

print(G.voisins('A'))
print(G.voisins('D'))"""

G.creer_graphe4x4()

print(G.wilson())
print(G.__repr__())