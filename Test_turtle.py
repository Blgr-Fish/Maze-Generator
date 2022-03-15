# -*- coding: utf-8 -*-
#from Maze_generator_fusion_aleatoireV1 import *
from math import *


from turtle import *

def turtle_truc(n,G):
    speed(2) 
    maze_completed = False
    
    etape = 0
    key_list = list(G.keys())
    val_list = list(G.values())
    while True:
        while etape == 0 : # on  définit les contours du labyrinthe
            forward(20*n)
            right(90)
        
        
            if abs(pos()) < 1 :
                etape +=1
                
             
                

            while etape == 1 : # on créé les parois intérieurs du labyrinthe
               for i in range(len(G)): # a modifier
                   for j in range(len(G)):

                       if key_list[i] in val_list[j]:
                           print(key_list[i] ,"est relié à ",key_list[j])
                           
                       else :
                           if key_list[i] != key_list[j] and abs(i-j) == 1 :
                               print(key_list[i] ,"est  pas relié à ",key_list[j])
                               
                               setpos((i*20),(j*20))
                        
                           
            
                       
                
                
                
                
                
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

G = {(0, 0): [(0, 1), (1, 0)], (0, 1): [(0, 0), (1, 1), (0, 2)], (0, 2): [(0, 3), (1, 2), (0, 1)], (0, 3): [(0, 2), (1, 3), (1, 3)], (1, 0): [(0, 0), (1, 1)], (1, 1): [(0, 1), (2, 1), (1, 2), (1, 0)], (1, 2): [(0, 2), (2, 2), (1, 3), (1, 1), (1, 1)], (1, 3): [(0, 3), (1, 2), (2, 3), (1, 2)], (2, 0): [(3, 0), (3, 0), (2, 1)], (2, 1): [(1, 1), (2, 0), (2, 2), (2, 0)], (2, 2): [(3, 2), (1, 2), (2, 1), (2, 3)], (2, 3): [(1, 3), (2, 2), (3, 3)], (3, 0): [(3, 1), (2, 0), (3, 1)], (3, 1): [(3, 0), (3, 2), (3, 0)], (3, 2): [(3, 3), (2, 2), (3, 1), (2, 2), (2, 2)], (3, 3): [(3, 2), (2, 3)]}
F = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1)], (1, 0): [(0, 0)], (1, 1): [(0, 1)]}           
            
print(turtle_truc(10,F))


    


#key_list = list(G.keys())
#val_list = list(F.values())

    
    