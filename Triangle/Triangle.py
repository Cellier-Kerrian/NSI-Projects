# import de bibliotheque
import math

class Triangle:
    '''
    class = Triangle, creation d'un triangle.
    '''
    def __init__(self, l1 :float, l2:float, l3:float):
        '''
        constructeur = creer un triangle.
        '''
        self.cote_a = l1
        self.cote_b = l2
        self.cote_c = l3
    
    def est_rectangle(self):
        '''

        Returns
        -------
        bool
            True = c'est un triangle rectangle.
            False = ce n'est pas un triangle rectangle.
            
        Description
        -------
            informe si le triangle est rectange ou non.
        '''
        a = self.cote_a
        b = self.cote_b
        c = self.cote_c
        return ((a*a+b*b == c*c) or (b*b+c*c == a*a) or (a*a+c*c == b*b))
        
    def aire(self):
        '''

        Returns
        -------
        float/int
            la valeur du perimetre du triangle.
            
        Description
        -------
            renvois la valeur qui correspond au perimetre du triangle.

        '''
        a = self.cote_a
        b = self.cote_b
        c = self.cote_c
        p = (a+b+c)/2
        return math.sqrt(p*(p-a)*(p-b)*(p-c))
    
    def est_plus_grand(self, other):
        '''

        Parameters
        ----------
        other : Triangle
            une instance de la class Triangle.

        Returns
        -------
        bool
            True = le perimetre de self est superieur a celui de other.
            False = le perimetre de self est inferieur a celui de other.

        '''
        perimetre_self = self.cote_a + self.cote_b + self.cote_c
        perimetre_other = other.cote_a + other.cote_b + other.cote_c
        return perimetre_self > perimetre_other