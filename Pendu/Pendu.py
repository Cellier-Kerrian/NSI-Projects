from random import choice

ERREURS_POSSIBLES = 10
SYMBOLE_MYSTERE = "-"
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "
LONGUEUR_MINIMALE = 4


def charge_dictionnaire ():
    liste_mots = []
    with open("dictionnaire-francais.txt", "r") as f:
        for mot in f. readlines ():
            mot = mot. strip (). upper ()
            if len (mot ) >= LONGUEUR_MINIMALE :
                liste_mots.append (mot)
    return liste_mots


def genere_motifs(secret,propositions):
    '''Cette Fonction permet de regarder si les lettres lettres rentrer par 
    l'utilisateur sont dans le mot à trouver
    Elle prend enparametre le mot à trouver, ainsi que les lettres que 
    l'utilisateur à renseigner'''
    motif = ""
    for i in range (0,len(secret)):
        if secret[i] in propositions:
            motif = motif+secret[i]
        else:
            motif = motif + SYMBOLE_MYSTERE
    return motif
    

def partie_simple():
    '''Cette Fonction, permet de jouer au Pendu. Elle dispose d'un system de 
    Win/Lose celon si vous trouvr le mot ou non avant que le pendu meur
    Elle utilise la fonction crée precedament, 
    "genere_motif(secret,propositions)"'''
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