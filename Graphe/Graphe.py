import math
import tkinter

class Sommet:
    '''
    class = Sommet, creer un Sommet.
    '''
    
    def __init__(self, nom :str, val :str):
        '''
        constructeur : creation d'un sommet.
        '''
        self.nom = nom
        self.donnee = val
    
    def get_donnee(self):
        '''

        Returns
        -------
        str
            la valeur de self.
            
        Description
        ------
            revois la valeur compris dans self.

        '''
        return self.donnee
    
    def set_donnee(self, val :str):
        '''

        Parameters
        ----------
        val : str
            une nouvel valeur.

        Returns
        -------
        None.
        
        Description
        ------
            remplace la veleur compris dans self.

        '''
        self.donnee = val
        
    def __repr__(self):
        '''

        Returns
        -------
        str
            affiche self.
            
        Description
        ------
            affiche self.

        '''
        return str(self.nom)
        
class Arete:
    '''
    
    Description
    ------
        création d'une class Arete.
        
    '''
    def __init__(self, coef :int, sommets :set, origine :Sommet=None, extremite :Sommet=None):
        '''
        
        Description
        -------
            constructeur : creation des instances de la class.

        '''
        self.coefficient = coef
        self.sommets = sommets
        self.origine = origine if origine != None else None
        self.extremite = extremite if extremite != None else None
        
    def get_coefficient(self):
        '''

        Returns
        -------
        int
            coeficient de self.
            
        Description
        ------
            renvois le coeficient que comporte self.

        '''
        return self.coefficient
    
    def set_coefficient(self, coef :int):
        '''

        Parameters
        ----------
        coef : int
            une nouvel valeur.

        Returns
        -------
        None.
        
        Description
        ------
            remplace le coeficient compris dans self.

        '''
        self.coefficient = coef
    
    def __repr__(self):
        '''

        Returns
        -------
        str
            affiche self.
            
        Description
        ------
            affiche self.

        '''
        return str((self.coefficient, self.sommet))
        
class Graphe:
    '''
    
    Description
    ------
        création d'une class Graphe.
        
    '''
    def __init__(self, sommets :list, aretes :list, oriente :bool, pondere :bool):
        '''
        
        Description
        -------
            constructeur : creation des instances de la class.

        '''
        self.sommets = sommets
        self.aretes = aretes
        self.oriente = oriente
        self.pondere = pondere
        
    def __len__(self):
        nbr = 0
        for i in self.sommets:
            nbr =+ 1
        return nbr
        
    def est_pondere(self):
        '''

        Returns
        -------
        None.
        
        Description
        ------
            cela ne fait rien si toute les aretes sont pondere, en cas 
            contraire, toute les aretes sont pondere à 1.

        '''
        if self.pondere == False:
            for i in self.aretes:
                i.set_coefficient(1)
        
    def get_aretes(self):
        '''

        Returns
        -------
        list
            une liste contenant des instances de la class Arete.
            
        Description
        ------
            renvois la liste des aretes present dans self.

        '''
        return self.aretes
    
    def ajoute_arete(self, arete :Arete):
        '''

        Parameters
        ----------
        arete : Arete
            une arete de la class Arete.

        Returns
        -------
        None.
        
        Description
        ------
            ajoute a la liste d'aretes une arete de la class Arete.

        '''
        self.aretes.append(arete)
    
    def get_sommets(self):
        '''

        Returns
        -------
        list
            une liste contenant des instances de la class Sommet.
            
        Description
        ------
            renvois la liste des sommets present dans self.

        '''
        return self.sommets
    
    def ajoute_sommet(self, sommet :Sommet):
        '''

        Parameters
        ----------
        sommet : Sommet
            un sommet de la class Sommet.

        Returns
        -------
        None.
        
        Description
        ------
            ajoute a la liste de sommet un sommet de la class Sommet.

        '''
        self.sommets.append(sommet)
        
    def est_complet(self):
        '''

        Returns
        -------
        bool
            True = Le graphe est complet.
            False = le graphe n'est pas complet.
            
        Description
        ------
            informe sur le fait que le grahe est complet ou non.

        '''
        return ((len(self.sommets)*(len(self.sommets)-1)/2) == len(self.aretes))
    
    def get_graph_dict(self):
        dico = {}
        for i in self.sommets:
            dico[i] = ([] if i not in dico else None)
            for j in self.aretes:
                if i in j.sommets:
                    for k in j.sommets:
                        if k != i and k not in dico[i]:
                            dico[i].append(k)
        return dico
    
    def get_graph(self):
        '''

        Returns
        -------
        None.
        
        Description
        ------
            Affiche le graphe à l'aide Tkinter.

        '''
        #creation fenetre
        fen = tkinter.Tk()
        fen.title("Graphe")
        
        rayon = 300
        graph = self.get_graph_dict()
        npoints = len(graph)
        
        taillepoint = rayon/npoints/5
        xcentre = rayon+taillepoint
        ycentre = xcentre 
        
        #creation coordonneess points
        x=[ycentre+rayon*math.sin(math.pi*2*i/npoints) for i in range(npoints)]
        y=[ycentre+rayon*math.cos(math.pi*2*i/npoints) for i in range(npoints)]
        
        index = 0
        coordonnees = {}
        for key in graph:
            coordonnees[key] = (x[index], y[index])
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
            w.create_oval(coordonnees[key][0]-taillepoint, coordonnees[key][1]-taillepoint, coordonnees[key][0]+taillepoint, coordonnees[key][1]+taillepoint, fill='white')     
            w.create_text(coordonnees[key][0], coordonnees[key][1], text=key, fill='black')
        
        #Bouton Quitter
        bou = tkinter.Button(fen, text="Quitter", command=fen.destroy)
        bou.pack()
        
        #fin fenetre
        fen.mainloop()