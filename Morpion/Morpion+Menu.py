from random import randint

def creation_grille(taille=3):
    """
    Fonction qui permet de créer une grille de morpion vide.

    Paramètres:
        taille -> int

    Renvoie:
        list <- grille de morpion.
    """
    grille = [['.']*taille for _ in range(taille)]
    return grille

def affichage(grille):
    """
    Fonction qui permet d'afficher une grille de morpion.

    Paramètres:
        grille -> list

    Renvoie:
        Rien.
    """
    taille = len(grille)
    print('  '+''.join([str(i) for i in range(taille)]))
    for y in range(taille):
        if y != 0:
            print('\n',sep='',end='')
        print(y,'',end='')
        for x in range(taille):
            print(grille[y][x],end='')
    print('')

def libre(grille, x, y):
    """
    Fonction qui permet de vérifier si une case est libre.

    Paramètres :
        grille -> list
        x -> int
        y -> int

    Renvoie :
        bool <- Vrai si l'emplacement sur la grille est libre.
    """
    if grille[x][y] == '.':
        return True
    else:
        print('Place déjà prise.')
        return False

def demander(grille):
    """
    Fonction qui permet de demander des coordonnées au joueur.

    Paramètres:
        grille -> list

    Renvoie:
        tuple <- Coordonées du point que le joueur a choisi.
    """
    taille = len(grille)
    while True:
        try:
            n_ligne = int(input("Numéro de ligne : "))
            n_colonne = int(input("Numéro de colonne : "))
        except ValueError:
            n_ligne = taille + 1 # Affiche nécessairement 'Réponse invalide.'

        if n_ligne >= taille or n_colonne >= taille:
            print("Réponse invalide.")
        elif libre(grille,n_ligne,n_colonne):
            return n_ligne,n_colonne

def placer(grille, x, y, symbole):
    """
    Fonction qui permet de placer le symbole aux coordonnées x, y.

    Paramètres:
        grille -> list
        x -> int
        y -> int
        symbole -> str

    Renvoie:
        Rien.
    """
    grille[x][y] = symbole

def tester_ligne(grille, x):
    """
    Fonction qui permet de tester la ligne x pour voir si elle possède le même
    symbole sur toute la ligne.

    Paramètres:
        grille -> list
        x -> int

    Renvoie:
        bool <- Vrai si la ligne est complète et gagnante.
    """

    for j in range(len(grille)):
        if grille[x][j] != '.':
            symbole = grille[x][j]
        else:
            symbole = ''

        for i in grille[x]:
            if i != symbole:
                return False
    return True

def tester_colonne(grille, x):
    """
    Fonction qui permet de tester la colonne x pour voir si elle possède le
    même symbole sur toute la colonne.

    Paramètres:
        grille -> list
        x -> int

    Renvoie:
        bool <- Vrai si la colonne est complète et gagnante.
    """
    for j in range(len(grille)):
        if grille[j][x] != '.':
            symbole = grille[j][x]
            break
        else:
            symbole = ''

    for i in range(len(grille)):
        if grille[i][x] != symbole:
            return False
    return True

def tester_diagonales(grille):
    """
    Fonction qui permet de tester les diagonales pour voir si au moins une des
    diagonales est composé d'un seul symbole.

    Paramètres:
        grille -> list
        x -> int

    Renvoie:
        bool <- Vrai si au moins une des diagonales est complète et gagnante.
    """
    symb_bool1 = True
    symb_bool2 = True
    symbole1 = ''
    symbole2 = ''
    for i in range(len(grille)):
        if grille[i][i] != '.' and symb_bool1:
            symbole1 = grille[i][i]
            symb_bool1 = False

        if grille[i][(len(grille)-1)-i] != '.' and symb_bool2:
            symbole2 = grille[i][(len(grille)-1)-i]
            symb_bool2 = False

    for j in range(len(grille)):
        if grille[j][j] != symbole1 and not symb_bool1:
            symb_bool1 = True
        if grille[j][(len(grille)-1)-j] != symbole2 and not symb_bool2:
            symb_bool2 = True

    return (not symb_bool1) or (not symb_bool2)

def tester(grille, x, y):
    """
    Fonction qui teste entièrement la grille avec toutes les fonctions écrites
    précédemment pour voir si le jeu est fini.

    Paramètres:
        grille -> list
        x -> int
        y -> int

    Renvoie:
        bool <- Vrai s'il y a au moins un des tests qui renvoie Vrai.
    """
    list_rep = [0]*3
    list_rep[0] = tester_diagonales(grille)
    list_rep[1] = tester_ligne(grille, x)
    list_rep[2] = tester_colonne(grille, y)
    return (True in list_rep)

def partie(taille=3,joueur=1):
    """
    Fonction qui débute une partie simple (deux joueurs).

    Paramètres:
        taille -> int
        joueur -> int

    Renvoie:
        str <- Symbole du gagnant. (Ou rien, si personne ne gagne.)
    """
    a = creation_grille(taille)
    symb_fin = '_' * 40
    for i in range(taille**2):
        if not (joueur-1):
            symbole = 'X'
        else:
            symbole = 'O'
        print('\n**********\nAu tour du joueur %s (%s)\n**********' % (joueur, symbole))
        joueur = 3 - joueur # f(x) = 3 - x
        affichage(a)
        x, y = demander(a)
        placer(a, x, y, symbole)
        affichage(a)
        if tester(a, x, y):
            if symbole == 'X':
                print('\nBravo au joueur 1 (%s) !' % symbole)
                print(symb_fin)
                return symbole # Pour la première amélio. de l'étape 5
            else:
                print('\nBravo au joueur 2 (%s) !' % symbole)
                print(symb_fin)
                return symbole # //
    print('\nPartie nul (égalité)')
    print(symb_fin)

def parties_multiple(taille=3, nbr_partie=3, ia=False):
    """
    Fonction qui permet de commencer plusieurs parties en gardant le score des
    parties précédentes.

    Paramètres:
        taille -> int
        nb_partie -> int
        ia -> bool

    Renvoie:
        Rien.
    """
    resultat_X = 0
    resultat_O = 0
    joueur = 1
    for i in range(nbr_partie):
        print('Partie', i+1)
        if ia:
            jeux = partie_ordi(taille, joueur)
        else:
            jeux = partie(taille, joueur)
        if jeux == 'X':
            joueur = 2
            resultat_X += 1
        elif jeux == 'O':
            joueur = 1
            resultat_O += 1
    if resultat_O > resultat_X:
        gagnant = "Le joueur 2"
    elif resultat_X > resultat_O:
        gagnant = "Le joueur 1"
    else:
        gagnant = "Le joueur 1 et 2 (égalité)"
    print('le joueur 1 à gagner : %s fois.\nLe joueur 2 à gagner : %s fois. \
        \nLe gagnant est : %s' % (resultat_X, resultat_O, gagnant))

def ia_ordi(grille):
    """
    Fonction qui indique à l'ordinateur où il doit jouer lors d'une partie contre
    l'ordinateur.

    Paramètres:
        grille -> list

    Renvoie:
        tuple <- Coordonées du point que l'ordinateur va jouer.
    """
    taille = len(grille)
    x, y = None, None
    for i in range(taille):
        for k in range(taille):
            if grille[i][k] != '.':
                continue
            grille_test = [x[:] for x in grille]
            grille_test[i][k] = 'X'
            if tester(grille_test, i, k):
                x, y = i, k
            grille_test[i][k] = 'O'
            if tester(grille_test, i, k):
                return i, k
    if x == None:
        x = randint(0, taille-1)
        y = randint(0, taille-1)
        while not (grille[x][y] == '.'):
            x = randint(0, taille-1)
            y = randint(0, taille-1)
    return x, y

def partie_ordi(taille=3, joueur=1):
    """
    Fonction qui lance une partie simple mais contre l'ordinateur et non contre
    un autre joueur.

    Paramètres:
        taille -> int
        joueur -> int

    Renvoie:
        str <- Le symbole du gagnant.
    """
    a = creation_grille(taille)
    symb_fin = '_' * 40
    for i in range(taille**2):
        if joueur == 1:
            symbole = 'X'
        else:
            symbole = 'O'
        print('\n**********\nAu tour du joueur %s (%s)\n**********' % (joueur, symbole))
        if joueur == 2: # Si le joueur est l'ordinateur
            x, y = ia_ordi(a)
            print("-"*3)
        else:
            affichage(a)
            x, y = demander(a)
        placer(a, x, y, symbole)
        affichage(a)
        joueur = 3 - joueur # f(x) = 3 - x
        if tester(a, x, y):
            if symbole == 'X':
                print('\nBravo au joueur 1 (%s) !' % symbole)
                print(symb_fin)
                return symbole # Pour la première amélio. de l'étape 5
            else:
                print('\nBravo au joueur 2 (%s) !' % symbole)
                print(symb_fin)
                return symbole # //
    print('\nPartie nul (égalité)')
    print(symb_fin)

def run():
    verif = False
    while not(verif):
        reponse = input('A quel mode de jeux voulez-vous jouer ? (1, 2, 3, 4 ou \'/info\' pour avoir des informations à propos des différents mode de jeux)\n• 1 → 1VS1\n• 2 → Compétition 1VS1\n• 3 → 1VS ordi\n• 4 → Compétition 1VS ordi\nRéponse : ')
        if reponse == '1':
            verif = True
            taille = int(input('\nQuel taille voulez-vous que la grille face ? (une partie normal = 3)\nRéponse : '))
            partie(taille)
        elif reponse == '2':
            verif = True
            print('\n')
            taille = int(input('\nQuel taille voulez-vous que la grille face ? (une partie normal = 3)\nRéponse : '))
            parties_multiple(taille)
        elif reponse == '3':
            verif = True
            print('\n')
            partie_ordi()
        elif reponse == '4':
            verif = True
            taille = int(input('\nQuel taille voulez-vous que la grille face ? (une partie normal = 3)\nRéponse : '))
            nbr_partie = int(input('\nNombre de partie ? (une partie normal = 3)\nRéponse : '))
            print('\n')
            parties_multiple(taille, nbr_partie, True)
        elif reponse == '/info':
            verif = False
            print('\n-----Information :-----\n• 1VS1 → un joueur joue contre une autre personne.\n• Compétition 1VS1 → un joueur joue un nombre de partie contre une autre personne, à la fin il y a les résultats.\n• 1VS ordi → un joueur joue contre l\'ordinateur.\n• Compétition 1VS ordi → un joueur joue un nombre de partie contre l\'ordinateur, à la fin il y a les résultats.\n')
        else:
            verif = False
            print('\nCe que vous avez rentrer est incorrecte.')
    choix = input("Voulez vous continuer ?\nRéponse : ")
    if choix in ('o', 'oui'):
        run()
    else:
        pass

# Lanceur
run()