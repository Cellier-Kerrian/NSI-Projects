class Sac:
    '''
    class = creer un sac (soius forme d'une liste).
    '''
    def __init__(self, collection=[]):
        '''
        constructeur = creer un sac.
        '''
        if type(collection) == list:
            raise ValueError("Une liste doit être renseigner.")
        
        self.contenu = collection
    
    def __len__(self):
        '''

        Returns
        -------
        int
            le nombre d'element que contient le sac.

        '''
        conteur = 0
        tmp = []
        for i in self.contenu:
            tmp.append(i)
            conteur += 1
        return conteur

    def __eq__(self, other):
        '''

        Parameters
        ----------
        other : Sac
            une autre instance de la class Sac.

        Returns
        -------
        bool
            True = les deux sacs contiennent les meme elements.
            False = les deux sacs ne contiennent pas les meme elements.

        '''
        if self.longueur() == other.longueur(): # if len(self) == len(other):
            for i in self.contenu:
                if i not in other.contenu:
                    return False
            return True
        return False
    
    def __repr__(self):
        '''

        Returns
        -------
        str
            affiche le sac.

        '''
        return f"{self.contenu}"
    
    def __str__(self):
        '''

        Returns
        -------
        str
            affiche le contenue du sac.

        '''
        return f"{self.contenu}"
    
    def est_vide(self):
        '''

        Returns
        -------
        bool
            True = si le sac est vide.
            False = si le sac n'est pas vide.

        '''
        return self.contenu == []
    
    def ajoute(self, n):
        '''

        Parameters
        ----------
        n : int/float
            un element a ajouter au sac.

        Returns
        -------
        bool
            True = element ajouter au sac.
            False = element deja present dans le sac, donc non ajouter.

        '''
        if n not in self.contenu:
            self.contenu = self.contenu + [n]
            return True
        return False
    
    def fusion(self, other):
        '''

        Parameters
        ----------
        other : Sac
            une autre instance de la class Sac.

        Returns
        -------
        None.
        
        Description
        -------
            fusionne le deuxieme sac dans le premier.

        '''
        if other.est_vide() == False:
            for i in other.contenu:
                self.ajoute(i)