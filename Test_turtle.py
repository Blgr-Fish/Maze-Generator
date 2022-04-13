from math import *
#from Maze_Generator import *

from turtle import *

def turtle_truc(n,G):
    setworldcoordinates(0, 0, n, n)
    title("Maze Generator")
    speed(15) 
    pensize(10)
    maze_completed = False
    
    etape = 0
    key_list = list(G.keys())
    val_list = list(G.values())
    print(len(key_list))
    print(val_list)
    longueur = n

    while maze_completed == False:
        while etape == 0 : # on  définit les contours du labyrinthe
            pd()
            forward(longueur)
            left(90)
            
  
        
        
            if abs(pos()) < 1 :
                etape +=1
                

        while etape == 1 : # on créé les parois intérieurs du labyrinthe
            for i in range(int(n)):
                setx(0)
                sety(0)
                setheading(0)
                forward(i)
                left(90)
                forward(n)
            for j in range (int(n)) :
                setx(0)
                sety(0)
                setheading(90)
                forward(j)
                right(90)
                forward(n)
            etape += 1
                   
               
        while etape == 2 :
            print('b')    
            print(key_list)
            print("b")
            print(val_list)
            for i in range(len(G)):
                for j in range(len(G)):
                    if key_list[i] in val_list[j]:
                        pencolor('white')
                       
                        if key_list[i][0] == key_list[j][0] and key_list[i][1] != key_list[j][1]: # on vérifie que l'index 0 soit le même et que l'index 1 soit différent
                                                                                                  # On efface donc le trait de manière verticale
                            if key_list[i][0] == n-1 and n > 2 : # si on est tout en haut du labyrinthe
                               
                                pu()
                                setpos(max(key_list[i][1],key_list[j][1]),key_list[j][0]+1) # au lieu de tracer un trait vers le haut, on le fait aller vers le bas
                                setheading(270)
                                
              
                                pd()
                                forward(1)
                                

                            else :
                            
                                pu()
                                setpos(max(key_list[i][1],key_list[j][1]),key_list[j][0])
                                setheading(90)
                               
                                pd()
                                forward(1)                       
                        
                        elif key_list[i][1] == key_list[j][1] and key_list[i][0] != key_list[j][0]: # Pareil qu'au desssus mais cette fois si c'est pour les index 1
                        
                            if key_list[i][1] == n-1 and n > 2 : # si on est trop à droite
                                                                 # on efface un trait vers la gauche au lieu de la droie
                                pu()
                                setpos(key_list[j][1]+1,max(key_list[i][0],key_list[j][0]))
                                setheading(180)
                                
                                
                                pd()
                                forward(1) 

                            else :
                           
                                pu()
                                setpos(key_list[j][1],max(key_list[i][0],key_list[j][0]))
                                setheading(0)
                                
                                
                                pd()
                                forward(1) 

                        print(key_list[i],"est relié à ", key_list[j])
                        
            pu()
            setpos(0,0) # quand tout est fini, on revient point de départ
            setheading(0)
            etape += 1

            while etape == 3 : # on remet bien les murs
                
                pencolor("black")
                pd()
                forward(longueur)
                left(90)

                if abs(pos()) < 1 :
                    etape+=1

            while etape == 4 :
                print('Maze Completed')
                maze_completed = True
                break


        done()
            


cote2 = {(0, 0): [(1, 0)], (0, 1): [(1, 1)], (1, 0): [(1, 1), (0, 0)], (1, 1): [(1, 0), (0, 1)]}          

cote4 = {(0, 0): [(1, 0), (0, 1)], (0, 1): [(0, 0), (1, 1), (0, 2)], (0, 2): [(0, 1), (1, 2), (0, 3)], (0, 3): [(0, 2), (1, 
3)], (1, 0): [(0, 0), (2, 0), (1, 1)], (1, 1): [(1, 0), (2, 1), (1, 2), (0, 1)], (1, 2): [(0, 2), (1, 1), (1, 3), (2, 2)], (1, 3): [(2, 3), (0, 3), (1, 2)], (2, 0): [(3, 0), (2, 1), (1, 0)], (2, 1): [(1, 1), (2, 0), (2, 2), (3, 1)], (2, 2): [(1, 2), (2, 3), (2, 1), (3, 2)], (2, 3): [(2, 2), (1, 3), (3, 3)], (3, 0): [(3, 1), (2, 0)], (3, 1): [(3, 
2), (2, 1), (3, 0)], (3, 2): [(2, 2), (3, 1), (3, 3)], (3, 3): [(2, 3), (3, 2)]}


cote4x4 ={(0, 0): [(1, 0)], (0, 1): [], (0, 2): [(1, 2)], (0, 3): [(0, 2)], (1, 0): [(2, 0), (1, 1), (0, 0)], (1, 1): [(0, 1)], (1, 2): [(0, 2), (1, 1)], (1, 3): [(2, 3), (1, 2)], (2, 0): [(1, 0)], (2, 1): [(2, 2)], (2, 2): [(2, 3)], (2, 3): [(3, 3), (1, 3)], (3, 0): [(2, 0)], (3, 1): [(3, 0), (2, 1)], (3, 2): [(3, 3)], (3, 3): [(3, 2)]}

cote3 = {(0, 0): [], (0, 1): [], (0, 2): [], (1, 0): [], (1, 1): [(1,2)], (1, 2): [], (2, 0): [], (2, 1): [], (2, 2): []}

cotetest = {(0, 0): [(0,1)], (0, 1): [(0,2)], (0, 2): [(0,3)],(0,3):[(1,3)], (1, 0): [(2,0)], (1, 1): [(1,2),(2,1)], (1, 2): [(2,2)],(1,3):[(2,3)], (2, 0): [(2,1),(3,0)], (2, 1): [(3,1)], (2, 2): [(2,3)],(2,3):[(3,3)], (3,0):[],(3,1):[(3,2)],(3,2):[],(3,3): [] }




"""A = Graphe_dictionnaire()
A.creer_graphe_nxn(10)
A.fusion_aleatoire()"""

E = {(0, 0): [(0, 1)], (0, 1): [(0, 2), (0, 0), (1, 1)], (0, 2): [(1, 2), (0, 1), (0, 1)], (1, 0): [(2, 0), (2, 0)], (1, 1): [(0, 1), (1, 2), (1, 2)], (1, 2): [(0, 2), (2, 2), (1, 1), (0, 2)], (2, 0): [(2, 1), (2, 1), (1, 0)], (2, 1): [(2, 0), (2, 2)], (2, 2): [(2, 1), (1, 2), (1, 2)]}
print(turtle_truc(sqrt(len(cote4)),cote4))
#print(turtle_truc(sqrt(a),a))