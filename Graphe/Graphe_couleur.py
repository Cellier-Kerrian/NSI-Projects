import math
import tkinter

def choix_couleur(graph :dict):
    '''

    Parameters
    ----------
    graph : dict
        un dictionnaire qui contient tout les sommets en cle et les sommets 
        voisins dans une lsite en valeur.

    Returns
    -------
    dico : dict
        un ditionnaire qui contient les sommets du dictionnaire donner en 
        paremetre en cle et en valeur la couleur qui leur est attribuer.
        
    Description
    -------
        attribut une couleur pour tout les sommets du graphe qui est donner en 
        paramtre, tout cela dans une disctionnaire qui est renvoyer.

    '''
    dico = {k: 0 for k in graph}
    for key in graph:
        n = 0
        n_invalide = True
        while n_invalide:
            n += 1
            n_invalide = False
            for other_key in graph[key]:
                if dico[other_key] == n:
                    n_invalide = True
        dico[key] = n
    return dico

def graph(graph :dict, color=True, colors=['blue', 'red', 'green', 'black']):
    '''

    Parameters
    ----------
    graph : dict
        un dictionnaire qui contient tout les sommets en cle et les sommets 
        voisins dans une lsite en valeur.
    color : bool, optional
        True = colorer les sommets du graphe. The default is True.
        False = ne pas colorer les sommets du graphe.
    colors : list, optional
        une liste de couleur. The default is ['blue', 'red', 'green', 'black'].

    Returns
    -------
        None
        
    Description
    -------
        affiche un graphe visual a l'aide de Tkinter à l'aide d'un graphe.

    '''
    #creation fenetre
    fen = tkinter.Tk()
    fen.title("Projet : Graphe Couleur")
    
    rayon = 300
    npoints = len(graph)
    
    taillepoint = rayon/npoints/5
    xcentre = rayon+taillepoint
    ycentre = xcentre 
    
    #creation coordonneess points
    x=[ycentre+rayon*math.sin(math.pi*2*i/npoints) for i in range(npoints)]
    y=[ycentre+rayon*math.cos(math.pi*2*i/npoints) for i in range(npoints)]
    
    index = 0
    coordonnees = {}
    sommet_color = (choix_couleur(graph) if color != False else None)
    for key in graph:
        try :
            coordonnees[key] = (x[index], y[index], (colors[sommet_color[key]] if color != False else None))
        except:
            return "ERREUR - La liste de couleur doit contenir plus de couleur."
        index += 1
    
    #creation de la zone de dessin
    w = tkinter.Canvas(fen, width=2*(rayon+taillepoint), height=2*(rayon+taillepoint)+50, bd=0, highlightthickness=0, bg="white")
    w.pack()
    
    #trace cercle principale
    w.create_oval(xcentre-rayon, ycentre-rayon, xcentre+rayon, ycentre+rayon, outline= 'white')
    
    #trace aretes
    for key in coordonnees:
        for other_key in graph[key]:
            w.create_line(coordonnees[key][0], coordonnees[key][1], coordonnees[other_key][0%npoints], coordonnees[other_key][1%npoints], fill="black")
    
    #tracer sommets
    for key in coordonnees:
        w.create_oval(coordonnees[key][0]-taillepoint, coordonnees[key][1]-taillepoint, coordonnees[key][0]+taillepoint, coordonnees[key][1]+taillepoint, fill=(coordonnees[key][2] if color != False else 'white'))     
        w.create_text(coordonnees[key][0], coordonnees[key][1], text=key, fill=('black' if coordonnees[key][2] != 'black' else 'white'))
    
    #Bouton Quitter
    bou = tkinter.Button(fen, text="Quitter", command=fen.destroy)
    bou.pack()
    
    #fin fenetre
    fen.mainloop()