#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:50:10 2022

@author: Maël Pierre Ziad
"""
class Graphe_dictionnaire:
    """ """
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
            self.ajouter_sommet(y)
            
        
        if x != y:                    # pour pas qu'on puisse faire une arrete avec le meme noeud
            self.A[x].append(y)

            if x not in self.A[y]:    # pour les graphes non orientés 
                self.A[y].append(x)



#TESTS

G = Graphe_dictionnaire()
G.ajouter_sommet('A')
G.ajouter_sommet('B')
G.ajouter_sommet('C')
G.ajouter_sommet('D')

G.ajouter_arete('A','B')
G.ajouter_arete('A','C')
G.ajouter_arete('A','D')
G.ajouter_arete('A','A') # ne marche pas car même valeur

print(G.__repr__())