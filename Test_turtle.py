from math import *
from Creation_lab_aldous import *
from turtle import *

def turtle_truc(n,m,G):
    """
    Entrée : 2 entiers, la longeur et la largeur du labyrinthe avec n la longeur et m la largeur, ainsi qu'un dictionnaire de coordonnées
    Sortie : un labyrinthe en turtle
    Rôle   : Créer un labyrinthe
    
    """
    setworldcoordinates(0, 0, n, m) # pour régler  l'affichage de la page turtle
    title("Maze Generator") 
    speed(6) 
    pensize(1)

    maze_completed = False
    
    etape = 0
    key_list = list(G.keys()) # la liste des clés du dictionnaire
    val_list = list(G.values()) # la liste des valeurs du dictionnaire
    largeur = n
    longueur = m

    while maze_completed == False:
        while etape == 0 : # on  définit les contours du labyrinthe
            pd()
            forward(longueur)
            left(90)
            forward(largeur)
            left(90)
            
  
        
        
            if abs(pos()) < 1 :
                etape +=1
                

        while etape == 1 : # on créé les parois intérieurs du labyrinthe
            for i in range(int(m)):
                setx(0)
                sety(0)
                setheading(0)
                forward(i)
                left(90)
                forward(m)
            for j in range (int(n)) :
                setx(0)
                sety(0)
                setheading(90)
                forward(j)
                right(90)
                forward(n)
            etape += 1
                   
               
        while etape == 2 :
            for i in range(len(G)): # la largeur
                for j in range(len(G)): # la longeur
                    if key_list[i] in val_list[j]:
                        pencolor('white')
                       
                        if key_list[i][0] == key_list[j][0] and key_list[i][1] != key_list[j][1]: # on vérifie que l'index 0 soit le même et que l'index 1 soit différent
                                                                                                  # On efface donc le trait de manière verticale
                            if key_list[i][0] == n-1 and n > 2 : # si on est tout en haut du labyrinthe
                               
                                pu()
                                setpos(max(key_list[i][1],key_list[j][1]),key_list[j][0]+1) # au lieu de tracer un trait vers le haut, on le fait aller vers le bas
                                setheading(270)
                                
                                forward(0.001)
                                pd()
                                forward(0.999) 
                                

                            else :
                            
                                pu()
                                setpos(max(key_list[i][1],key_list[j][1]),key_list[j][0])
                                setheading(90)
                               
                                forward(0.001)
                                pd()
                                forward(0.999)                    
                        
                        elif key_list[i][1] == key_list[j][1] and key_list[i][0] != key_list[j][0]: # Pareil qu'au desssus mais cette fois si c'est pour les index 1
                        
                            if key_list[i][1] == m-1 and m > 2 : # si on est trop à droite
                                                                 # on efface un trait vers la gauche au lieu de la droie
                                pu()
                                setpos(key_list[j][1]+1,max(key_list[i][0],key_list[j][0]))
                                setheading(180)
                                
                                
                                forward(0.001)
                                pd()
                                forward(0.999) 

                            else :
                           
                                pu()
                                setpos(key_list[j][1],max(key_list[i][0],key_list[j][0]))
                                setheading(0)
                                
                                
                                forward(0.001)
                                pd()
                                forward(0.999) 

                        
            pu()
            setpos(0,0) # quand tout est fini, on revient point de départ
            setheading(0)
            etape += 1

            while etape == 3 : # on remet bien les murs
                
                pencolor("black")
                pd()
                forward(longueur)
                left(90)
                forward(largeur)
                left(90)

                if abs(pos()) < 1 :
                    etape+=1

            while etape == 4 :
                print('Maze Completed')
                maze_completed = True
                break


        done()
            


cote4x4 ={(0, 0): [(1, 0)], (0, 1): [(1, 1), (0, 2)], (0, 2): [(0, 1)], (0, 3): [(1, 3)], (1, 0): [(0, 0), (1, 1)], (1, 1): [(1, 0), (0, 1), (1, 2)], (1, 2): [(1, 3), (2, 2), (1, 1)], (1, 3): [(1, 2), (2, 3), (0, 3)], (2, 0): [(3, 0), (2, 1)], (2, 1): [(3, 1), (2, 0)], (2, 2): [(3, 2), (1, 2)], (2, 3): [(1, 3), (3, 3)], (3, 0): [(2, 0), (3, 1)], (3, 1): [(3, 2), (2, 1), (3, 0)], (3, 2): [(3, 1), (2, 2), (3, 3)], (3, 3): [(3, 2), (2, 3)]}

cotetest = {(0, 0): [(0,1)], (0, 1): [(0,2)], (0, 2): [(0,3)],(0,3):[(1,3)], (1, 0): [(2,0)], (1, 1): [(1,2),(2,1)], (1, 2): [(2,2)],(1,3):[(2,3)], (2, 0): [(2,1),(3,0)], (2, 1): [(3,1)], (2, 2): [(2,3)],(2,3):[(3,3)], (3,0):[],(3,1):[(3,2)],(3,2):[],(3,3): [] }

cote3x3={(0, 0): [(1, 0), (0, 1)], (0, 1): [(1, 1)], (0, 2): [], (1, 0): [(2, 0), (1, 1)], (1, 1): [(0, 1)], (1, 2): [(1, 1)], (2, 0): [], (2, 1): [(1, 1)], (2, 2): [(2, 1)]}


cote45 ={(0, 0): [(1, 0)], (0, 1): [(1, 1)], (0, 2): [(0, 3), (1, 2)], (0, 3): [(1, 3)], (0, 4): [], (1, 0): [(2, 0)], (1, 1): [(1, 2), (0, 1)], (1, 2): [(1, 3), (1, 1)], (1, 3): [(1, 4)], (1, 4): [(1, 3)], (2, 0): [(2, 1), (3, 0)], (2, 1): [(2, 2), (2, 0), (1, 1)], (2, 2): [(2, 3), (2, 1)], (2, 3): [(2, 4), (2, 2)], (2, 4): [(2, 3)], (3, 0): [], (3, 1): [(3, 0)], (3, 2): [(3, 1), (2, 2)], (3, 3): [(3, 2), (2, 3)], (3, 4): [(2, 4)]}



a = int(input('Entrez la longeur du labyrinthe : '))
b = int(input('Entrez la largeur du labyrinthe : '))

graphe = creer_lab_Aldous_frerot(a,b)

print(turtle_truc(a,b,graphe))



