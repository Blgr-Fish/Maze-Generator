#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 12:50:10 2022

@author: Maël Pierre Ziad
"""

import random


class Piles :

    def __init__(self) -> None:
        self.pile = []

    def est_vide (self) :
        return self.pile==[]

    def empiler (self, element) :
        self.pile.append(element)

    def depiler (self) :
        if not self.est_vide():
            del self.pile[-1]

    def sommet(self):
        if not self.est_vide():
            return self.pile[-1]
    
    def __repr__(self):               # méthode repr pour afficher le graphe
        return str(self.pile)


        

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
            self.ajouter_sommet(y)    # on vérifie que le noeud existe ou pas dans le graphe
            

        if x != y:                    # pour pas qu'on puisse faire une arrete avec le meme noeud
            if y not in self.A[x]:
                self.A[x].append(y)
           
            #if x not in self.A[y]:    # pour les graphes non orientés 
            #    self.A[y].append(x)   

    
    def creer_graphe_nxn(self,n):    # créer un graphe de n x n taille 
        #assert type(n) is int
        #assert n >= 1
        self.n = n
        for i in range(self.n):
            for j in range(self.n):
                self.ajouter_sommet((i,j))



    """def wilson(self):                  # algo wilson
        maze_completed = False
        self.first_cell = random.choice(list(self.A)) # créer la cellule initiale de manière aléatoire
        sommets_verifies = [self.first_cell]

        while not maze_completed:
            self.random_cell = random.choice(list(self.A))
            if self.random_cell not in  sommets_verifies:     # si la cellule choisie au hasard n'est pas dans les sommets verifies
                
                
                
                
                sommets_verifies.append(self.random_cell)     # on ajoute la random_cell dans les sommets visites
                
                # il faut faire en sorte de rejoindre random_cell et first_cell maintenant"""
    
    def fusion_aleatoire(self):
        maze_completed = False # Passe à True quand le labyrinthe est complet
        liste_valeurs = [] # Liste des valeurs attribuées à chaque noeud du graphe, de 0 à la longueur du graphe
        longueur = len(self.A) # Longueur du Graphe

        while len(liste_valeurs) < longueur : # On rempli tant que liste valeurs est inférieur la longueur du graphe
            valeur_temp = random.randint(0,longueur) # On rempli la liste de valeur au hasard...

            if valeur_temp not in liste_valeurs : 
                liste_valeurs.append(valeur_temp)  #... que si elles ne sont pas déjà présentes

        nombre_coups = 0 
        print("Liste valeur version initiale : ", liste_valeurs)

        while not maze_completed :
            random_cell = random.choice(list(self.A)) # un noeud random du graphe...
            random_index = list(self.A).index(random_cell) #... et son index
            cote_choisi = random.randint(1,4) # 1 = haut, 2 = bas, 3 = gauche et 4 = droite
             

            if cote_choisi == 1 and random_cell[0] != 0: # si ça va vers le haut et que c'est à l'index 0 on peut pas monter plus haut
                if liste_valeurs[random_cell[0]-1] != liste_valeurs[random_index]: # on vérifie que la valeur attribuée au noeud du dessus est différent de celle du noeud choisi

                    liste_valeurs[random_index] = liste_valeurs[random_cell[0]-1]  # si c'est le cas, le noeud choisi prend la valeur du noeud du dessus
                    self.ajouter_arete(random_cell,(random_cell[0]-1,random_cell[1])) # et on les joints par une arrête
                    nombre_coups +=1

            if cote_choisi == 2 and random_cell[0] != (self.n)-1 : # on peut pas descendre plus bas que n-1
                if liste_valeurs[random_cell[0]+1] != liste_valeurs[random_index]:
                    for ele in liste_valeurs :
                        if ele == liste_valeurs[random_index]:
                            ele = liste_valeurs[random_cell[0]+1]
                    liste_valeurs[random_index] = liste_valeurs[random_cell[0]+1]
                    self.ajouter_arete(random_cell,(random_cell[0]+1,random_cell[1])) 
                    nombre_coups +=1

            if cote_choisi == 3 and random_cell[1] != 0 : 
                if liste_valeurs[random_cell[1]-1] != liste_valeurs[random_index] :
                    for ele in liste_valeurs :
                        if ele == liste_valeurs[random_index]:
                            ele = liste_valeurs[random_cell[1]-1]        
                    liste_valeurs[random_index] = liste_valeurs[random_cell[1]-1]
                    self.ajouter_arete(random_cell,(random_cell[0],random_cell[1]-1))
                    nombre_coups +=1

            if cote_choisi == 4 and random_cell[1] != (self.n)-1 : 
                if liste_valeurs[random_cell[1]+1] != liste_valeurs[random_index] :
                    for ele in liste_valeurs :
                        if ele == liste_valeurs[random_index]:
                            ele = liste_valeurs[random_cell[1]+1]
                    liste_valeurs[random_index] = liste_valeurs[random_cell[1]+1]
                    self.ajouter_arete(random_cell,(random_cell[0],random_cell[1]+1))
                    nombre_coups +=1
            print(liste_valeurs)

            if liste_valeurs.count(liste_valeurs[0]) == len(liste_valeurs): # on vérifie que le nombre de valeurs égales à liste_valeurs[0] soit égal à la longueur de la liste
                maze_completed = True # si c'est le cas, ça veut dire que toutes les valeurs sont les mêmes et donc que le graphe est complet

            
        return "Labirynthe effectué en : " + str(nombre_coups) + " essais."

   
   
   
   
   
   
   
    def dfs_maze(self):
        pile = Piles()
        sommets_visites = []
        maze_completed = False
        nombre_coups = 0

        current_cell = random.choice(list(self.A)) # un noeud random du graphe...
        

        pile.empiler(current_cell)


        while not maze_completed :
            cote_choisi = random.randint(1,4) # 1 = haut, 2 = bas, 3 = gauche et 4 = droite
            sommets_visites.append(current_cell)
            print(sommets_visites)
             
           
            if cote_choisi == 1 and current_cell[0] != 0 and pile.sommet()[0] != 0 and pile.sommet()[0]-1 not in sommets_visites: # si ça va vers le haut et que c'est à l'index est à 0 on peut pas monter plus haut
                    
  
                self.ajouter_arete(current_cell,(pile.sommet()[0]-1,pile.sommet()[1]))
                current_cell = (pile.sommet()[0]-1,pile.sommet()[1])
                nombre_coups +=1


            elif cote_choisi == 2 and current_cell[0] != (self.n)-1 and pile.sommet()[0] != (self.n)-1 and pile.sommet()[0]+1 not in sommets_visites: # on peut pas descendre plus bas que 3

                self.ajouter_arete(current_cell,(pile.sommet()[0]+1,pile.sommet()[1]))
                current_cell = (pile.sommet()[0]+1,pile.sommet()[1])
                nombre_coups +=1

            elif cote_choisi == 3 and current_cell[1] != 0 and pile.sommet()[1] != 0 and pile.sommet()[1]-1 not in sommets_visites: 
    
                self.ajouter_arete(current_cell,(pile.sommet()[0],pile.sommet()[1]-1))
                current_cell = (pile.sommet()[0],pile.sommet()[1]-1)
                nombre_coups +=1

            elif cote_choisi == 4 and current_cell[1] != (self.n)-1 and pile.sommet()[1] != (self.n)-1 and pile.sommet()[1]+1 not in sommets_visites: 
               
                self.ajouter_arete(current_cell,(pile.sommet()[0],pile.sommet()[1]+1))
                current_cell = (pile.sommet()[0],pile.sommet()[1]+1)
                nombre_coups +=1

            else :

                if sommets_visites == len(self.A) :
                    maze_completed = True

                else : 

                    pile.depiler()
                    pile.__repr__()
                    print()
                    current_cell = pile.sommet()



        return "Labirynthe effectué en : " + str(nombre_coups) + " essais."

            
        
#TESTS

G = Graphe_dictionnaire()

G.creer_graphe_nxn(4)



print(G.fusion_aleatoire())

#print()
print(G.__repr__())


#     0  1  2  3
#  0  00 01 02 03
#  1  10 11 12 13
#  2  20 21 22 23
#  3  30 31 32 33