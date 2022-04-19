from math import *
#from Maze_Generator import *

from turtle import *

def turtle_truc(n,G):
    #setworldcoordinates(0,-n,n,0)
    setworldcoordinates(-5,-5,5,5)
    title("Maze Generator")
    speed(6) 
    pensize(1)

    maze_completed = False
    
    etape = 0
    """G = list(G.keys()) # les cellules du graphe
    val_list = list(G.values()) # les valeurs des cellules
    print(len(G))
    print(val_list)"""
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
            for i in range(3):
                for j in range(3) :
                    if G[i]['N'] == True :
                        
                        pencolor('white')
                        pu()
                        setpos(j,i)
                        setheading(180)     
                        forward(0.001)
                        pd()
                        forward(0.999)                    

                    elif G[i]['S'] == True :
                        pencolor('white')
                        pu()
                        setpos(j,i+1)
                        setheading(180)     
                        forward(0.001)
                        pd()
                        forward(0.999)

                    elif G[i]['E'] == True :
                        pencolor('white')
                        pu()
                        setpos(j+1,i)
                        setheading(90)     
                        forward(0.001)
                        pd()
                        forward(0.999)
                
                    elif G[i]['O'] == True :
                        pencolor('white')
                        pu()
                        setpos(j-1,i)
                        setheading(90)     
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

            if abs(pos()) < 1 :
                etape+=1

        while etape == 4 :
            print('Maze Completed')
            maze_completed = True
            break


    done()

                

cote3= [{'N': False, 'E': True, 'S': False, 'O': False}, {'N': False, 'E': False, 'S': True, 'O': True},  {'N': False, 'E': False, 'S': True, 'O': False},
        {'N': False, 'E': True, 'S': True, 'O': False},  {'N': True, 'E': True, 'S': False, 'O': True},   {'N': True, 'E': False, 'S': True, 'O': True}, 
        {'N': True, 'E': False, 'S': False, 'O': False}, {'N': False, 'E': True, 'S': False, 'O': False}, {'N': True, 'E': False, 'S': False, 'O': True}]


print(cote3[0]['N']) # Renvoie True

print(turtle_truc(sqrt(len(cote3)),cote3))