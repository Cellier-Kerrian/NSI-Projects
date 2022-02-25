import random

lettre_base_ADN = ['A', 'C', 'G', 'T']
lettre_base_ARN = ['A', 'C', 'G', 'U']
lettre_ADN = {'U': 'A', 'G': 'C', 'C': 'G', 'A': 'T'}
lettre_ARN = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
complementaire = {'A': 'C', 'C': 'A', 'G': 'T', 'T': 'G'}
dicogene = {'UUU': 'F', 'UUC': 'F',
            'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
            'AUG': 'M',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU':  'S', 'AGC': 'S',
            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'UAU': 'Y', 'UAC': 'Y',
            'UAA': '*', 'UAG': '*', 'UGA': '*',
            'CAU': 'H', 'CAC': 'H',
            'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N',
            'AAA': 'K', 'AAG': 'K',
            'GAU': 'D', 'GAC': 'D',
            'GAA': 'E', 'GAG': 'E',
            'UGU': 'C', 'UGC': 'C',
            'UGG': 'W',
            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA':' R', 'AGG': 'R',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

#-----------------------------------------------------------------------------

def trouver(sequence): 
    '''Permet de trouver si la séquence est ARN ou ADN ou rien du tout
    Parmètres : sequence (str)
    Sortie : 'ADN' (str), 'ARN' (str), None (bool)'''
    if ADN(sequence) == True:
        return 'ADN'
    elif ARN(sequence) == True:
        return 'ARN'
    else:
        return None

def ADN(chaine):
    '''Permet de trouver si la séquence est ADN
    Paramètres : chaine (str)
    Sortie : True (bool), False (bool)'''
    for lettre in chaine:
        if not(lettre in lettre_base_ADN):
            return False
    return True

def ARN(chaine):
    '''Permet de trouver si la séquence est ARN
    Paramètres : chaine (str)
    Sortie : True (bool), False (bool)'''
    for lettre in chaine:
        if not(lettre in lettre_base_ARN):
            return False
    return True

def genereADN(n=1):
    '''Renvoie une séquence ADN générée aléatoirement et dont la taille
    n est passée en paramètre
    Paramètres : n (int)
    Sortie : chaineADN (str)'''
    chaineADN = ''
    for i in range(n):
        chaineADN += random.choice(lettre_base_ADN)
    return chaineADN

def genereARN(n=1):
    '''Renvoie une séquence ARN générée aléatoirement et dont la taille
    n est passée en paramètre
    Paramètres : n (int)
    Sortie : True (bool), False (bool)'''
    chaineARN = ''
    for i in range(n):
        chaineARN += random.choice(lettre_base_ARN)
    return chaineARN

def baseComplementaire(base, type):
    '''Renvoie la base complémentaire de la base
    "base" passée en paramètre, selon le type type de séquence 
    demandé en sortie qui peut être soit ’ADN’ soit ’ARN’
    Paramètres : base (str), type (str)
    Sortie : True (bool), False (bool)'''
    base_modif = ''
    if type == 'ADN': #transforme en ARN
        for lettre in base:
            if not(lettre in lettre_ARN):
                print('error')
                return True
            base_modif += lettre_ARN[lettre]
        return base_modif
    elif type == 'ARN': #transforme en ADN
        for lettre in base:
            if not(lettre in lettre_ADN):
                print('error')
                return True
            base_modif += lettre_ADN[lettre]
        return base_modif
    else:
        print('Le type n\'est pas correcte.')
        return False

def transcrit(sequence, debut, fin):
    '''Renvoie la séquence d’ARN messager construit
    à partir de la sous-séquence d’ADN comprise entre les deux positions 
    debut et fin passées en paramètre, incluses
    Paramètres : sequence (str), debut (str), fin (str)
    Sortie : sequence_modif (str)'''
    sequence_modif = ''
    for i in range(debut, fin):
        sequence_modif += sequence[i]
    return sequence_modif

def transcrit_bis(sequence, debut, fin):
    '''Renvoie la séquence d’ARN messager construit
    à partir de la sous-séquence d’ADN comprise entre les deux positions 
    debut et fin passées en paramètre, incluses
    Paramètres : sequence (str), debut (str), fin (str)
    Sortie : baseComplementaire (str)'''
    sequence_modif = ''
    for i in range(debut, fin):
        sequence_modif += sequence[i]
    type_sequence = trouver(sequence_modif)
    return baseComplementaire(sequence_modif, type_sequence)

def replique(sequence):
    '''Construit la séquence ADN complémentaire et inversée de
    celle passée en paramètre
    Paramètres : sequence (str)
    Sortie : None (bool)'''
    sequence_comp = ''
    type_sequence = trouver(sequence)
    if type_sequence == 'ARN':
        return None
    else:
        for lettre in sequence:
            sequence_comp += complementaire[lettre]
        return sequence_comp

def codeGenetique(genetique):
    '''Renvoie l’acide aminé (sous la forme
    du nom abrégé en une lettre) correspondant au codon passé en paramètre, ou * pour les codons Stop
    Paramètres : genetique (str)
    Sortie : dicogene[genetique] (str), 'error' (str)'''
    if genetique in dicogene:
        return dicogene[genetique]
    return 'error'

# def transformerCodons(sequence):
    '''Coupe la séquence en groupe de 3
    Paramètres : sequence (str)
    Sortie : True (bool), False (bool)'''
#     print(sequence)
#     liste = []
#     temp = ''
#     for i in sequence:
#         temp += i
#         if len(temp) == 3:
#             liste.append(temp)
#             temp = ''
#     return liste

def transformerCodons(chaine, debut=0):
    '''Permet de transformer la chaine d’ARN messager chaine
    (de longueur supposée multiple de 3) en une liste de 
    codons (séquences de 3 nucléotides successifs)
    Paramètres : chaine (str), debut (int)
    Sortie : liste (str)'''
    liste = []
    temp = ''
    for i in range(len(chaine)):
        if i >= debut:
            temp += chaine[i]
            if len(temp) == 3:
                liste.append(temp)
                temp = ''
    return liste

def transformerCodons_bis(chaine, debut=0, fin=0):
    '''Permet de transformer la chaine d’ARN messager chaine
    (de longueur supposée multiple de 3) en une liste de 
    codons (séquences de 3 nucléotides successifs)
    Paramètres : chaine (str) , debut (int), fin (int)
    Sortie : liste (str)'''
    liste = []
    temp = ''
    if fin == 0:
        fin = len(chaine)
    for i in range(debut, fin):
        temp += chaine[i]
        if len(temp) == 3:
            liste.append(temp)
            temp = ''
    return liste
      
def traduit(chaine):
    '''Construit la séquence protéique obtenue par la traduction de
    la séquence d’ARN messager chaine passée en paramètre
    Paramètres : chaine (str)
    Sortie : None (bool), complementaire (str)'''
    complementaire = ''
    if not(len(chaine)%3 == 0):
        print('La séquence ne peut pas être couper par 3, car celle-ci n\'est pas multiple de 3.')
        return None
    else:
        codon_cut = transformerCodons(chaine)
        for i in range(len(codon_cut)):
            complementaire += codeGenetique(codon_cut[i])
        return complementaire

def traduit_bis(chaine):
    '''Construit la séquence protéique obtenue par la traduction de
    la séquence d’ARN messager chaine passée en paramètre
    Paramètres : chaine (str)
    Sortie : None (bool), codons (str)'''
    debut = debutTraduction(chaine)
    if debut == None:
        print('La séquence doit être de type ARN.')
        return None
    fin = finTraduction(chaine, debut)
    if fin == None:
        return None
    codons = transformerCodons_bis(chaine, debut, fin)
    return codons
    
    
def traduit_codon(chaine):
    '''Renvoie les codons correspondant à la chaine
    Paramètres : chaine (str)
    Sortie : None (bool), complementaire (str)'''
    complementaire = ''
    debut = debutTraduction(chaine)
    if debut == None:
        return 'debut_None'
    fin = finTraduction(chaine, debut)
    if fin == None:
        return 'fin_None'
    transformation = transformerCodons_bis(chaine, debut, fin)
    for i in range(len(transformation)):
        complementaire += codeGenetique(transformation[i])
    return complementaire

def debutTraduction(chaine):
    '''Indique le rang du premier nucléotide qui suit
    immédiatement la première séquence de nucléotides 
    AUG (codon START) de la chaine d’ARN messager chaine
    passée en paramètre
    Paramètres : chaine (str)
    Sortie : None (bool), i (str)'''
    if chaine == '' or not('AUG' in chaine):
        print('La séquence ne comporte pas de Codon Start (\'AUG\')')
        return None
    else:
        for i in range(len(chaine)):
            if chaine[i] == 'A' and chaine[i+1] == 'U' and chaine[i+2] == 'G':
                return i+3

def finTraduction(chaine, debut):
    '''Construit la séquence protéique obtenue par la traduction de
    la séquence d’ARN messager chaine passée en paramètre
    Paramètres : chaine (str), debut (str)
    Sortie : None (bool), i (str)'''
    if chaine == '' or not('UAA' in chaine) and not('UAG' in chaine) and not('UGA' in chaine):
        print('La séquence ne contient pas de Codon Stop.')
        return None
    else:
        for i in range(len(chaine)):
            if i >= debut:
                if chaine[i] == 'U' and chaine[i+1] == 'A' and chaine[i+2] == 'A':
                    return i
                elif chaine[i] == 'U' and chaine[i+1] == 'A' and chaine[i+2] == 'G':
                    return i
                elif chaine[i] == 'U' and chaine[i+1] == 'G' and chaine[i+2] == 'A':
                    return i

#-----------------------------------------------------------------------------

option_menu = {'Trouver': 'permet de trouver si la séquence fournie est de type ADN ou ARN.',
               'Complémentaire': 'permet de généré l\'opposé de la séquence d\'ADN fournie.',
               'Généré ADN': 'permet de généré une séquence d\'ADN.',
               'Généré ARN': 'permet de généré une séquence d\'ARN.',
               'Traduit ADN': 'permet de traduire une séquence d\'ADN en ARN.',
               'Traduit ARN': 'permet de traduire une séquence d\'ARN en ADN.',
               'Codon (x1)': 'permet de trouver le Codon du fragment de la séquence fournie.',
               'Codon': 'permet de fournir tout les Codons de la séquence fournie.',
               'Séquence ADN': 'permet de découper la séquence fornie en fontion d\'un Codon Start et d\'un Codon Stop.',
               'Acides Aminnées': 'permet de donner les Acides Aminées de la séquence d\'ADN fournie.'}

def menu():
    '''Affiche le menu interactif qui permet d’utiliser 
    l’ensemble des fonctions programmées au choix de l’utilisateur
    '''
    drapeau = False
    print('\n~~~~~ Menu ~~~~~\n')
    option()
    demande = input('\nQue voulez-vous faire ?\n')
    while drapeau == False:
        if demande == '/help':
            print('\n')
            help()
            demande = input('\nQue voulez-vous faire ?\n')
            drapeau = False
        elif demande in liste_option_setup():
            
            if demande == '1':
                demande1()
            
            elif demande == '2':
                demande2()
                
            elif demande == '3':
                demande3()
                
            elif demande == '4':
                demande4()
                
            elif demande == '5':
                demande5()
                
            elif demande == '6':
                demande6()
                
            elif demande == '7':
                demande7()
                
            elif demande == '8':
                demande8()
                
            elif demande == '9':
                demande9()
                
            elif demande == '10':
                demande10()
                
        else:
            drapeau = False
            print('\nVeillez renseigner le nombre qui se trouve devant l\'option que vous désirez.')
            demande = input('\nQue voulez-vous faire ?\n')
        
def option():
    '''Affiche les options de sélection du menu'''
    nbr = 1
    for i in option_menu:
        print(nbr, i)
        nbr += 1
    print('PS: Pour plus de renseignement → \"/help\"')
    
    
def help():
    '''Affiche une aide dans le menu'''
    nbr = 1
    for i in option_menu:
        print(nbr, i)
        print('  →', option_menu[i])
        nbr += 1
    print('\nA tout moment vous pouvez fair \"cancel\" afin de revenir au Menu de séléction.')
    
def liste_option_setup():
    '''Permet de connaitre le nombre d'option du dico "option_menu"
    Sortie : liste (str)'''
    liste = []
    for i in range(len(option_menu)):
        liste.append(str(i+1))
    return liste

def demande1():
    '''Informe l'utilisateur si la séquence est ADN ou ARN'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence :\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence :\n')
            mini_drapeau = False
        else:
            print('\nLa séquence fourrnie est du type:', trouver(sequence))
            mini_drapeau = True
            restart()
            
def demande2():
    '''Affiche le complément d'une séquence ADN'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ADN:\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.\n')
            sequence = input('\nMentionne une séquence d\'ADN:\n')
            mini_drapeau = False
        elif type == 'ARN':
            print('\nLa séquence que vous venez de fournir est de type ARN et pas ADN.\n')
            sequence = input('\nMentionne une séquence d\'ADN:\n')
            mini_drapeau = False
        else:
            print('\nLa séquence complémentaire de la séquence fournie est:', replique(sequence))
            mini_drapeau = True
            restart()
            
def demande3():
    '''Génère une séquence ADN'''
    n = input('\nMentionne le nombre base que la séquence d\'ADN doit avoir:\n')
    if n == 'cancel':
        print('\n')
        menu()
    else:
        ADN_genere = genereADN(int(n))
        print('\nVoici une séquence d\'ADN composer de', n, 'base(s):')
        print(ADN_genere)
        restart()
            
def demande4():
    '''Génère une séquence ARN'''
    n = input('\nMentionne le nombre base que la séquence d\'ARN doit avoir:\n')
    if n == 'cancel':
        print('\n')
        menu()
    else:
        ARN_genere = genereARN(int(n))
        print('\nVoici une séquence d\'ADN composer de', n, 'base(s):')
        print(ARN_genere)
        restart()    
        
def demande5():
    '''Convertit une séquence ADN en ARN'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ADN:\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence d\'ADN:\n')
            mini_drapeau = False
        elif type == 'ARN':
            print('\nLa séquence que vous venez de fournir est de type ARN et pas ADN.')
            sequence = input('\nMentionne une séquence d\'ADN:\n')
            mini_drapeau = False
        else:
            mini_drapeau = True
            sequence_modif = baseComplementaire(sequence, type)
            print('\nL\'équivalent de la séquence d\'ADN fournie en ARN est:')
            print(sequence_modif)
            restart()
            
def demande6():
    '''Convertit une séquence ARN en ADN'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ARN:\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        elif type == 'ADN':
            print('\nLa séquence que vous venez de fournir est de type ADN et pas ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        else:
            mini_drapeau = True
            sequence_modif = baseComplementaire(sequence, type)
            print('\nL\'équivalent de la séquence d\'ARN fournie en ADN est:')
            print(sequence_modif)
            restart()
            
def demande7():
    '''Traduit un codon (simple)'''
    mini_drapeau = False
    petit_drapeau = False
    sequence = input('\nMentionne un fragment de séquence d\'ARN (3 allèles):\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while petit_drapeau == False:
        if len(sequence) < 3 or len(sequence) > 3:
            print('\nUn fragement de séquence doit être sous la forme \'XXX\'')
            sequence = input('\nMentionne un fragment de séquence d\'ARN (3 allèles):\n')
            petit_drapeau = False
        elif len(sequence) == 3:
            petit_drapeau = True
            while mini_drapeau == False:
                type = trouver(sequence)
                if type == None:
                    print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
                    sequence = input('\nMentionne un fragment de séquence d\'ARN (3 allèles):\n')
                    mini_drapeau = False
                elif type == 'ADN':
                    print('\nLa séquence que vous venez de fournir est de type ADN et pas ARN.')
                    sequence = input('\nMentionne un fragment de séquence d\'ARN (3 allèles):\n')
                    mini_drapeau = False
                else:
                    mini_drapeau = True
                    traduction = traduit(sequence)
                    print('\nLe Codon du fragment de la séquence d\'ARN fournie est:')
                    print(traduction)
                    restart()
            
def demande8():
    '''Traduit un codon (multiple)'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ARN (multiple de 3):\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence d\'ARN (multiple de 3):\n')
            mini_drapeau = False
        elif type == 'ADN':
            print('\nLa séquence que vous venez de fournir est de type ADN et pas ARN.')
            sequence = input('\nMentionne une séquence d\'ARN (multiple de 3):\n')
            mini_drapeau = False
        else:
            traduction = traduit(sequence)
            if traduction == None:
                sequence = input('\nMentionne une séquence d\'ARN (multiple de 3):\n')
                mini_drapeau = False
            else:
                mini_drapeau = True
                print('\nLes Codons de la séquence d\'ARN fournie sont:')
                print(traduction)
                restart()
    
def demande9():
    '''Découoage d'un séquence à partir d'un codon start jusqu'à un codon stop'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ARN:\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        elif type == 'ADN':
            print('\nLa séquence que vous venez de fournir est de type ADN et pas ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        else:
            mini_drapeau = True
            codons = traduit_bis(sequence)
            print('\nVoici les Codons présent entre le Codon Start et le Codon Stop:')
            print(codons)
            restart()

def demande10():
    '''Génère l'acide aminé d'une suite ADN'''
    mini_drapeau = False
    sequence = input('\nMentionne une séquence d\'ARN:\n')
    if sequence == 'cancel':
        print('\n')
        menu()
    while mini_drapeau == False:
        type = trouver(sequence)
        if type == None:
            print('\nCe que vous venez de donner n\'est ni de type ADN ni de type ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        elif type == 'ADN':
            print('\nLa séquence que vous venez de fournir est de type ADN et pas ARN.')
            sequence = input('\nMentionne une séquence d\'ARN:\n')
            mini_drapeau = False
        else:
            codons = traduit_codon(sequence)
            if codons == 'debut_None' or codons == 'fin_None':
                sequence = input('\nMentionne une séquence d\'ARN:\n')
                mini_drapeau = False
            else:
                mini_drapeau = True
                print('\nVoici les Acides Aminées pour la séquence fournie:')
                print(codons)
                restart()

def restart():
    '''Relance le menu'''
    menu()
    
#-----------------------------------------------------------------------------
menu()