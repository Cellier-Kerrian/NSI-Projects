import random
import math
import matplotlib.pyplot as plt
fig = plt.figure()


def alea(a, b):
    '''

    Parameters
    ----------
    a : int
        la valeur minimum du nombre choisi aléatoirement.
    b : int
        la valeur maximum du nombre choisi aléatoirement.

    Returns
    -------
    X, Y : tuple
        un nombre choisi aléatoirement.
    
    Description
    -------
        Choisir des valeurs X et Y alétoirement entre deux deux valeurs donner 
        en parametre.

    '''
    
    X = random.randint(a, b)
    Y = random.randint(a, b)
    return X, Y

def centreExam(a,b,n=1):
    '''

    Parameters
    ----------
    a : int
        la valeur minimum du nombre choisi aléatoirement.
    b : int
        la valeur maximum du nombre choisi aléatoirement.
    n : int, optional
        le nombre de tuple dans la liste. The default is 1.

    Returns
    -------
    liste : list
        une liste contenant n tuple(s).
    
    Description
    -------
        creer une liste de n tuple(s) qui sont choisie aléatoirement.

    '''
    
    liste = []
    for i in range(n):
        nombres = alea(a, b)
        liste.append(nombres)
    return liste

def distance(a, b):
    '''

    Parameters
    ----------
    a : tuple(int)
        deux valeur, X et Y, contenue dans un tuple.
    b : tuple(int)
        deux valeur, X et Y, contenue dans un tuple.

    Returns
    -------
    calcule : int
        calcule une distance entre deux positions.
        
    Description
    -------
        calcul la distance entre deux points.

    '''
    
    calcule = math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    return calcule

def centre_plus_proche(mesCoord, listeCentres):
    '''

    Parameters
    ----------
    mesCoord : tuple(int)
        Coordonnées du point qui se situ au centre du cercle.
    listeCentres : list
        la liste contenant les tuples.

    Returns
    -------
    coord_centre : tuple(int)
        les coordonnées du tuples le qui a la distance la plus petite en 
        fonction de mesCoord.
    
    Description
    -------
        trouve le point le plus proche dupoint qui est le centre du cercle.

    '''
    
    distance_plus_proche = distance(mesCoord, listeCentres[0])
    coord_centre = listeCentres[0]
    for i in range(len(listeCentres)):
        test_distance = distance(mesCoord, listeCentres[i])
        if distance_plus_proche > test_distance:
            distance_plus_proche = test_distance
            coord_centre = listeCentres[i]
    return coord_centre

def convertir(mesCoord, listeCentres):
    '''

    Parameters
    ----------
    mesCoord : tuple(int)
        Coordonnées du point qui se situ au centre du cercle.
    listeCentres :list
        la liste contenant les tuples.

    Returns
    -------
    liste : list
        revois une liste qui contiendes tuples de X et Y ainsi que le distance 
        espective par rapport au centre du cercle.
        
    Description
    -------
        affiche une lsite qui mon regroupe les coordonner des point ainsi que 
        les distances qu'ils ont par rapport au centre du cercle.

    '''
    
    liste = []
    for i in range(len(listeCentres)):
        nbr = distance(mesCoord, listeCentres[i])
        liste.append(nbr)
    return liste

def tri_selection(liste, listeCentres):
    '''

    Parameters
    ----------
    liste : list
        liste qui contient les distance en fonction du centre du cercle (non 
        trier).
    listeCentres : list
        liste contenant les coordonnées de chaque point (non trier).

    Returns
    -------
    tab : list
        liste de terme trier.
        
    Description
    -------
        tri une liste de terme à l'aide d'une aute liste de terme (les deux 
        listes concordent).

    '''
    
    N = len(liste)
    for i in range(0, N-1):
        pos = recherche_pos_min(liste, i)
        echange_element(liste, i, pos, listeCentres)
    return listeCentres

def recherche_pos_min(liste, i):
    '''

    Parameters
    ----------
    tab : list
        liste de terme.
    i : int
        nombre qui represente un index de tab.

    Returns
    -------
    index_min : int
        l'index minimum de tab.
        
    Description
    -------
        renvois l'index de la valeur la plus petite parmis tab.

    '''
    
    valeur_min = liste[i]
    index_min = i
    for j in range(i, len(liste)):
        if liste[j] < valeur_min:
            index_min = j
            valeur_min = liste[j]
    return index_min

def echange_element(liste, i, pos, listeCentres):
    '''

    Parameters
    ----------
    tab : list
        liste de terme.
    i : int
        nombre qui represente un index de tab.
    pos : int
        nombre qui represente un index de tab.
    listeCentres : list
        liste contenant les coordonnées de chaque point (non trier).

    Returns
    -------
    None.
    
    Description
    -------
        échange l'élément pos à la place de l'élément i.
    
    '''
    
    temp1 = liste[i]
    temp2 = listeCentres[i]
    liste[i] = liste[pos]
    listeCentres[i] = listeCentres[pos]
    liste[pos] = temp1
    listeCentres[pos] = temp2

def graph(a, b, n=5):
    '''

    Parameters
    ----------
    a : int
        la valeur la plus petite (pour utilise la fonction alea).
    b : int
        la valeur la plus grande (pour utilise la fonction alea).
    n : int, optional
        le nombre de points en plus du centre du cercle. The default is 5.

    Returns
    -------
    None.
    
    Description
    -------
        permet de créer un graph visuel, afin de voirle point le plus proche du 
        centre du cercle.

    '''
    '''Paramètres : a → la valeur la plus petite pour utilise la fonction alea.
                    b → la valeur la plus grande pour utilise la fonction alea.
                    n → le nombre de tuple dans la liste (par default 5).
    Retour : Un graphique qui permet de visualisé tout les point, et le point 
    le pris proche du point qui se situ au centre du cercle.'''
    
    mesCoord = alea(a, b)
    listeCentres = centreExam(a, b, n)
    listeCentresModif = convertir(mesCoord, listeCentres)
    listeCentresCroissant = tri_selection(listeCentresModif, listeCentres)
    coord_centre = centre_plus_proche(mesCoord, listeCentresCroissant)
    rayon = distance(mesCoord, coord_centre)
    
    vx = []
    vy = []
    for i in range(len(listeCentres)):
        x = listeCentres[i][0]
        vx.append(x)
        y = listeCentres[i][1]
        vy.append(y)
    
    xa = mesCoord[0]
    ya = mesCoord[1]
    xb = coord_centre[0]
    yb = coord_centre[1]
    
    cercle = plt.Circle((mesCoord[0], mesCoord[1]), radius = rayon, color = 'green', fill = False )
    
    ax= plt.gca()
    ax.add_patch(cercle)
    plt.plot([xa, xb], [ya, yb], '--', color = 'green')
    plt.plot(vx, vy, '.', color = 'blue')
    plt.plot(xa, ya, '.', color = 'red')
    plt.text(listeCentres[2][0] , listeCentres[2][1], rayon, horizontalalignment = 'center', verticalalignment = 'center')
    ax.add_patch(cercle)
    plt.axis('scaled')
    plt.title("Le point le plus proche du centre du Cercle")
    plt.xlabel('Axe X')
    plt.ylabel('Axe Y')
    fig.savefig('graph.png')
    plt.show ()


#Executer :
a = int(input("nombre minimum du centre du cercle :\n"))
b = int(input("nombre maximum du centre du cercle :\n"))
n = int(input("nombre de points :\n"))

graph(a, b, n)