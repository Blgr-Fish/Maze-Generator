from math import *
from Creation_lab_aldous import *
from turtle import *

def turtle_lab(n,m,G):
    """
    Entrée : 2 entiers, la longeur et la largeur du labyrinthe avec n la largeur et m la longueur, ainsi qu'un dictionnaire de coordonnées
    Sortie : un labyrinthe en turtle
    Rôle   : Créer un labyrinthe
    
    """
    setworldcoordinates(-0.5, -0.5, m+0.5, n+0.5) # pour régler  l'affichage de la page turtle
    title("Maze Generator") 
    speed(10) 
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
                

        while etape == 1 : # on crée les parois intérieurs du labyrinthe
            for i in range(int(m)):
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
                forward(m)
            etape += 1
                   
               
        while etape == 2 :
            for i in range(len(G)): 
                print(i)
                for j in range(len(G)):
                    if key_list[i] in val_list[j]:
                        pencolor('white') # on efface pas le trait, mais on le repasse en blanc
                       
                        if key_list[i][0] == key_list[j][0] and key_list[i][1] != key_list[j][1]: # on vérifie que l'index 0 soit le même et que l'index 1 soit différent
                                                                                                  # On efface donc le trait de manière verticale
                            if key_list[i][0] == m-1 and m > 2 : # si on est tout en haut du labyrinthe
                               
                                pu()
                                setpos(max(key_list[i][1],key_list[j][1]),key_list[j][0]+1) # au lieu de tracer un trait vers le haut, on le fait aller vers le bas
                                setheading(270)
                                
                                forward(0.001) # on s'avance un petit peu pour pas dessiner en blance sur les trait non effacés
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
                        
                            if key_list[i][1] == n-1 and n > 2 : # si on est trop à droite
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
            

cote54 = {(0,0):[(1,0)],(0,1):[(0,2)],(0,2):[(0,1),(0,3)],(0,3):[(0,2),(1,3),(0,4)],(0,4):[(0,3),(1,4)],
          (1,0):[(0,0),(1,1)],(1,1):[(1,0),(1,2)],(1,2):[(1,1),(2,2),(1,3)],(1,3):[(1,2),(0,3)],(1,4):[(0,4),(2,4)],
          (2,0):[(3,0),(2,1)],(2,1):[(2,0),(2,2)],(2,2):[(2,1),(1,2),(3,2)],(2,3):[(2,4)],(2,4):[(1,4),(3,4)],
          (3,0):[(2,0),(3,1)],(3,1):[(3,0)],(3,2):[(2,2),(3,3)],(3,3):[(3,2)],(3,4):[(2,4)]}

long = int(input('Entrez la longeur du labyrinthe : '))
larg = int(input('Entrez la largeur du labyrinthe : '))

graphe = creer_lab_Aldous_frerot(long,larg)

print(turtle_lab(long,larg,graphe))



