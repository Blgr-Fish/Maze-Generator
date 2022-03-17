from math import *
from Maze_Generator import *

from turtle import *

def turtle_truc(n,G):
    setworldcoordinates(0, 0, n, n)
    speed(10) 
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

                                     if n == 2 :
                                        sety(key_list[i][0])
                                     elif key_list[i][0] == n-1 and n>2 :
                                        sety(key_list[i][0])
                                        
                                     else : 
                                        sety(key_list[i][0]+1)
                                     pu()

                                   
                                   
                               elif key_list[i][1] == key_list[j][1]: # si les y sont differents
                                   if key_list[i][0] - key_list[j][0] == abs(1) :
                                   
                                     print(key_list[i] ,"est  pas relié à ",key_list[j])
                                     pencolor("red")
                                     
                                     sety(key_list[i][0])
                                    
                                     pd()
                                     if key_list[i][1] == n-1 :
                                         setx(key_list[i][1])
                                     else:
                                         setx(key_list[i][1]+1)
                                     pu()

               etape +=1
               pass

                        
        break
    done()
            

G = {(0, 0): [(1, 0)], (0, 1): [(0, 2), (0, 0)], (0, 2): [(0, 1), (0, 3), (1, 2)], (0, 3): [(0, 2), (1, 3)], (1, 0): [(2, 0)], (1, 1): [(0, 1), (1, 2), (2, 1)], (1, 2): [(1, 3), (1, 1), (2, 2)], (1, 3): [(1, 2)], (2, 0): [(2, 1), (3, 0)], (2, 1): [(2, 0), (1, 1)], (2, 2): [(1, 2), (3, 2), (2, 1), (2, 3)], (2, 3): [(2, 2), (3, 3), (1, 3)], (3, 0): [(3, 1)], (3, 1): [(3, 2), (2, 1), (3, 0)], (3, 2): [(3, 3), (2, 2)], (3, 3): [(2, 3), (3, 2)]}

F = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1)], (1, 0): [(0, 0)], (1, 1): [(0, 1)]}           

E = {(0, 0): [(0, 1)], (0, 1): [(0, 2), (0, 0), (1, 1)], (0, 2): [(1, 2), (0, 1), (0, 1)], (1, 0): [(2, 0), (2, 0)], (1, 1): [(0, 1), (1, 2), (1, 2)], (1, 2): [(0, 2), (2, 2), (1, 1), (0, 2)], (2, 0): [(2, 1), (2, 1), (1, 0)], (2, 1): [(2, 0), (2, 2)], (2, 2): [(2, 1), (1, 2), (1, 2)]}

B = {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(0, 3)], (0, 3): [(0, 4)], (0, 4): [(1, 4), (0, 3)], (1, 0): [(2, 0)], (1, 1): [(1, 0), (2, 1), (1, 2), (0, 1)], (1, 2): [(2, 2), (0, 2)], (1, 3): [(2, 3), (1, 4), (0, 3)], (1, 4): [(2, 4), (1, 3), (0, 4)], (2, 0): [(1, 0), (3, 0), (2, 1)], (2, 1): [(2, 0), (3, 1), (2, 2)], (2, 2): [(1, 2), (2, 3), (3, 2)], (2, 3): [(3, 3)], (2, 4): [(2, 3), (1, 4)], (3, 0): [(4, 0), (3, 1), (2, 0)], (3, 1): [(4, 1), (3, 2), (3, 0), (2, 1)], (3, 2): [(3, 1), (4, 2)], (3, 3): [(4, 3), (2, 3), (3, 4)], (3, 4): [(2, 4), (3, 3), (4, 4)], (4, 0): [(4, 1), (3, 0)], (4, 1): [(4, 2), (3, 1), (4, 0)], (4, 2): [(4, 3)], (4, 3): [(4, 2), (3, 3)], (4, 4): [(4, 3)]}

print(turtle_truc(sqrt(len(B)),B))

"""A = Graphe_dictionnaire()
A.creer_graphe_nxn(10)
A.fusion_aleatoire()"""


#print(turtle_truc(sqrt(a),a))


    

    