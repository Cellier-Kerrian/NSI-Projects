from random import choice

ERREURS_POSSIBLES = 10
SYMBOLE_MYSTERE = "-"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LONGUEUR_MINIMALE = 4


def charge_dictionnaire ():
    '''

    Returns
    -------
    liste_mots : list
        une liste qui contient des mots (str).
        
    Description
    ------
        permet de creer une liste de mots present dans un fichier .txt (un 
        fichier externe) afin qu'il puisse etre exploiter par le programme.

    '''
    liste_mots = []
    with open("dictionnaire-francais.txt", "r") as f:
        for mot in f. readlines ():
            mot = mot. strip (). upper ()
            if len (mot ) >= LONGUEUR_MINIMALE :
                liste_mots.append (mot)
    return liste_mots


def genere_motifs(secret,propositions):
    '''

    Parameters
    ----------
    mot_mystere : str
        le mot mystere que le joueur doit trouver.
    propositions : list
        liste de lettre proposee par le joueur.

    Returns
    -------
    motif : str
        un mot qui contient un symbole pour les lettres qu'il n'a pas trouve 
        et les lettres clairement affichees pour celle qu'il a trouve.
        
    Description
    -------
        genere une chaine de caractere qui represente les lettres que le 
        joueur n'a pas encore trouvees.

    '''
    motif = ""
    for i in range (0,len(secret)):
        if secret[i] in propositions:
            motif = motif+secret[i]
        else:
            motif = motif + SYMBOLE_MYSTERE
    return motif
    

def partie_simple():
    '''

    Returns
    -------
    TYPE
    bool
        True = Partie Gagner.
        False = Partie Perdu.
    
    Description
    -------
        lancement de la partie.

    '''
    liste_mots = charge_dictionnaire()
    mot = choice(liste_mots)
    lettres_proposées = []
    motif = genere_motifs(mot,lettres_proposées)
    erreur = 0
    while True:
        if mot == motif:
            print("Tu a GAGNER !")
            return True
        elif erreur <= ERREURS_POSSIBLES-1:
            while motif != mot and erreur <= ERREURS_POSSIBLES-1:
                lettre = input("Quelle est la lettre que tu veux insérer ?\n")
                if lettre in lettres_proposées:
                    print("La lettre a déja été proposé.")
                    print("Le mot :",motif)
                elif lettre in mot:
                    lettres_proposées.append(lettre)
                    motif = genere_motifs(mot,lettres_proposées)
                    print("Le mot :",motif) 
                else:
                    erreur += 1
                    print("Erreur encore possible :",ERREURS_POSSIBLES-erreur)
                    print("Le mot :",motif) 
        else:
            print("Tu a PERDU !")
            print("le mot était:",mot)
            return False


#Executable :
partie_simple()
