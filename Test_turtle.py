# -*- coding: utf-8 -*-
from Maze_Generator import *
from math import *


from turtle import *

def turtle_truc(n,G):
    setworldcoordinates(0, 0, n, n)
    speed(5) 
    maze_completed = False
    
    etape = 0
    key_list = list(G.keys())
    val_list = list(G.values())
    longueur = n
    list_coord = []
    while True:
        while etape == 0 : # on  définit les contours du labyrinthe
            pd()
            forward(longueur)
            left(90)
            pu()
  
        
        
            if abs(pos()) < 1 :
                etape +=1
                
             
                

            while etape == 1 : # on créé les parois intérieurs du labyrinthe
               
               for i in range(len(G)):
                   for j in range(len(G)):
                       if key_list[i] in val_list[j]: # on vérifie si un noeud est présent dans les voisins du noeud à côté
                           print(key_list[i] ,"est relié à ",key_list[j])
                           
                           
                       else :
                           if key_list[i] != key_list[j]:
                               if key_list[i][0] == key_list[j][0] : # on vérifie que les y sont les mêmes
                                   if key_list[i][1] - key_list[j][1] == abs(1) : # et on s'assure que x - x soit = 1
                                     print(key_list[i] ,"est  pas relié à ",key_list[j])
                                     pencolor("green")
                               
                                     setx(key_list[i][1])
                                     pd()
                                     if key_list[i][1] == n-1 :
                                        sety(key_list[i][0])
                                        
                                     else : 
                                        sety(key_list[i+1][0])
                                     pu()

                                   
                                   
                               elif key_list[i][1] == key_list[j][1]: # si les y sont differents
                                   if key_list[i][0] - key_list[j][0] == abs(1) :
                                   
                                     print(key_list[i] ,"est  pas relié à ",key_list[j])
                                     pencolor("red")
                                     
                                     sety(key_list[i][0])
                                    
                                     pd()
                                     if key_list[i][1] == n-1 :
                                         setx(key_list[i-1][1])
                                     else:
                                         setx(key_list[i+1][1])
                                     pu()

                                   
            
                      

                   
                   
                  
                  
                   """for j in range(len(G)):

                       if key_list[i] in val_list[j]:
                           print(key_list[i] ,"est relié à ",key_list[j])
                         
                           
                       else :
                           if key_list[i] != key_list[j]:
                               if key_list[i][0] == key_list[j][0] :
                                   print(key_list[i] ,"est  pas relié à ",key_list[j])
                                   print('ok')
                                   
                                   
                                   setpos((10*n)),(0)
                                   setpos((10*n),(j*20))
                               elif key_list[i][1] == key_list[j][1]:
                                   print(key_list[i] ,"est  pas relié à ",key_list[j])

                                   print('o')"""
                           
            
                       
                
                
                
                
                
               etape +=1
               pass

                        
        break
    done()
            
# =============================================================================
#         
#             for i in range (n):
#                 setx(0)
#                 sety(0)
#                 setheading(0)
#                 forward(20*i)
#                 right(90)
#                 forward(20*n)
#             for j in range (n) :
#                 setx(0)
#                 sety(0)
#                 setheading(270)
#                 forward(20*j)
#                 left(90)
#                 forward(20*n)
#             etape += 1
# =============================================================================

G = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 2)], (0, 2): [(0, 3), (0, 1), (0, 3)], (0, 3): [], (1, 0): [(2, 0)], (1, 1): [(0, 1), (1, 2), (1, 0), (1, 2), (0, 1), (2, 1)], (1, 2): [(2, 2), (0, 2), (1, 1), (1, 3), (0, 2), (2, 2), (0, 2), 
(0, 2)], (1, 3): [(0, 3), (1, 2)], (2, 0): [(3, 0)], (2, 1): [(2, 2), (2, 0), (3, 1)], (2, 2): [(1, 2), (2, 3)], (2, 3): [(2, 2), (1, 3), (2, 2), (2, 2), (1, 3)], (3, 0): [(3, 1), (3, 1)], (3, 1): [(2, 1)], (3, 2): [(3, 3), (3, 1), 
(3, 3)], (3, 3): [(2, 3), (2, 3)]}
F = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1)], (1, 0): [(0, 0)], (1, 1): [(0, 1)]}           


E = {(0, 0): [(0, 1)], (0, 1): [(0, 2), (0, 0), (1, 1)], (0, 2): [(1, 2), (0, 1), (0, 1)], (1, 0): [(2, 0), (2, 0)], (1, 1): [(0, 1), (1, 2), (1, 2)], (1, 2): [(0, 2), (2, 2), (1, 1), (0, 2)], (2, 0): [(2, 1), (2, 1), (1, 0)], (2, 1): [(2, 0), (2, 2)], (2, 2): [(2, 1), (1, 2), (1, 2)]}

print(turtle_truc(sqrt(len(G)),G))

A = Graphe_dictionnaire()
A.creer_graphe_nxn(2)

"""print(A.fusion_aleatoire())
print()
print(A.__repr__)"""

    


#key_list = list(G.keys())
#val_list = list(F.values())

    
    