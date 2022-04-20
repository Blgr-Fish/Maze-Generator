from math import *
from Creation_lab_aldous import *
from Creation_lab_prim import *
from turtle import *

def turtle_lab(n,m,G):
    """
    Entrée : 2 entiers, la longeur et la largeur du labyrinthe avec n la largeur et m la longueur, ainsi qu'un dictionnaire de coordonnées
    Sortie : un labyrinthe en turtle
    Rôle   : Créer un labyrinthe
    
    """
    setworldcoordinates(-0.5, -0.5, m+0.5, n+0.5) # pour régler  l'affichage de la page turtle
    title("Maze Generator") 
    speed(15) # Modifier pour que ça aille plus ou moins vite 
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
            setpos(0,0) # quand tout est fini, on revient au point de départ
            setheading(0)
            etape += 1

            while etape == 3 : # on refait bien les contours
                
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
                hideturtle()
                maze_completed = True
                break


        done()



def transfo_aldous(G,longe,large):
    """
    Entrée : Une liste de directions NSOE, une valeur longueur et une valeur largeur
    Sortie : Un dictionnaire sous forme {(cellule):[(cellule_reliée)]}
    Rôle   : Transformer une liste de directions venant de l'algorithme d'Aldous en un dictionnaire interprétable par la partie graphique   
    """
    g = {} 
    l = len(G)
    for i in range(max(large,longe)): # Création des cellules
        for j in range(min(large,longe)):
            g.update({(i,j):[]})
    
    for i in range(l):        # Si N est égal à True, cela signifie que la cellule est reliée en haut
        if G[i]['N'] == True :
            ajouter_arete(g,list(g)[i],((list(g)[i][0]+1,list(g)[i][1])))
        
        if G[i]['S'] == True :  # Si S est égal à True, cela signifie que la cellule est reliée en bas
            ajouter_arete(g,list(g)[i],((list(g)[i][0]-1,list(g)[i][1])))

        if G[i]['O'] == True :   # Si O est égal à True, cela signifie que la cellule est reliée à gauche
            ajouter_arete(g,list(g)[i],((list(g)[i][0],list(g)[i][1]-1)))

        if G[i]['E'] == True :   # Si E est égal à True, cela signifie que la cellule est reliée à droite
            ajouter_arete(g,list(g)[i],((list(g)[i][0],list(g)[i][1]+1)))

    return g



def transfo_prim(G,longe,large):
    """
    Entrée : Une liste de directions NSOE, une valeur longueur et une valeur largeur
    Sortie : Un dictionnaire sous forme {(cellule):[(cellule_reliée)]}
    Rôle   : Transformer une liste de directions venant de l'algorithme d'Aldous en un dictionnaire interprétable par la partie graphique   
    """
    g = {}
    l = len(G)
    for i in range(max(large,longe)): # Création des cellules
        for j in range(min(large,longe)):
            g.update({(i,j):[]})
    
    for i in range(l): 
        if G[i]['N'] == True :   # Si N est égal à True, cela signifie que la cellule est reliée en bas, car le point (0,0) se situe en haut à droite, du coup il faut inverser le labyrintge
            ajouter_arete(g,list(g)[i],((list(g)[i][0]-1,list(g)[i][1])))
        
        if G[i]['S'] == True :  # Si S est égal à True, cela signifie que la cellule est reliée en haut
            ajouter_arete(g,list(g)[i],((list(g)[i][0]+1,list(g)[i][1])))

        if G[i]['O'] == True : # Si O est égal à True, cela signifie que la cellule est reliée à gauche
            ajouter_arete(g,list(g)[i],((list(g)[i][0],list(g)[i][1]-1)))

        if G[i]['E'] == True : # Si E est égal à True, cela signifie que la cellule est reliée à droite
            ajouter_arete(g,list(g)[i],((list(g)[i][0],list(g)[i][1]+1)))

    return g
    

def ajouter_arete(G,x, y):     # ajoute une arrête entre 2 noeuds
        if x != y:                    # pour pas qu'on puisse faire une arrete avec le meme noeud
            if y not in G[x]:
                G[x].append(y)
           
#######################################################################################################

def mainprog():

    long = int(input('Entrez la longeur du labyrinthe (METTRE LA PLUS GRANDE VALEUR): '))
    assert long > 1, "Un labyrinthe ne peut pas être créé avec une longueur de 1"

    larg = int(input('Entrez la largeur du labyrinthe (METTRE LA PLUS PETITE VALEUR): '))
    assert larg > 1,  "Un labyrinthe ne peut pas être créé avec une largeur de 1"

    assert long < larg, "La longueur doit être supérieure ou égale à la largeur"
    question = input("Prim ou Aldous ? ")

    if question.upper() == "ALDOUS" :
        graphe =creer_lab_Aldous_frerot(long,larg)
        graphe2 = transfo_aldous(graphe,larg,long)
        print(turtle_lab(long,larg,graphe2))
    elif question.upper() == "PRIM" :
        graphe = creer_lab_prim(long,larg)
        graphe2 = transfo_prim(graphe,larg,long)
        print(turtle_lab(long,larg,graphe2))
    else : 
        print('Erreur, relancez le programme.(Vérifiez la syntaxe des algorithmes)')


mainprog()

