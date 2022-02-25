import random

nbr_joueur = int(input("Combient de Joueur êtes-vous ? \n1, ou 2 ?\n"))

# system → Anti-Error
error_nbr_joueur = True
error1 = True
error2 = True

while error_nbr_joueur == True:
#----------------------------------------------------BcJ----------------------------------------------------
  if nbr_joueur == 1:
      # system → niveau de difficulté
      demande = int(input("Niveau 1:\nL'intervalle est compris entre 1 et 100.\nNiveau 2:\nL'intervalle est compris entre 1 et 1000.\nNiveau 3:\nL'intervalle est compris entre 1 et 10000.\n\nQuel niveau de difficulté voulez-vous : \n1, 2, ou 3 ?\n"))
      while error1 == True:
        if demande == 1:
          affichage=random.randint(1,100)
          error1 = False
        if demande == 2:
          affichage=random.randint(1,1000)
          error = False
        if demande == 3:
          affichage=random.randint(1,10000)
          error1 = False
        if demande > 3:
          demande = int(input("Quel niveau de difficulté voulez-vous : \n1, 2, ou 3 ?\n"))
          error1 = True 

      reponse = int(input("Votre nombre ?\n"))

      # system → devinette BcJ
      nombre_coup = 0

      while reponse != affichage:
        if reponse < affichage:
          print("Le nombre à deviner est plus grand")
          nombre_coup = nombre_coup + 1
          reponse = int(input("Votre nombre ?\n"))
        if reponse > affichage:
          print("Le nombre à deviner est plus petit")
          nombre_coup = nombre_coup + 1
          reponse = int(input("Votre nombre ?\n"))
        if reponse == affichage:
          print("Bravo ! Vous avez deviné le nombre en", nombre_coup + 1, "coups.")
        error_nbr_joueur = False
#----------------------------------------------------JcJ----------------------------------------------------
  if nbr_joueur == 2:
      j1 = int(input("Joueur 1, choisissez un nombre compris entre 1 et 1000 (inclus), à faire devinez.\n"))
      nbr_j1 = 0

      # system → choix nombre de départ par le Joueur 1
      while error2 == True:
        if j1 <= 1000:
          nbr_j1 = j1
          error2 = False
        if j1 >=1001:
          j = int(input("Choisie un nombre compris entre 1 et 1000, à faire devinez.\n"))
          error2 = True

      reponse = int(input("Joueur 2, quel est votre nombre ?\n"))

      nombre_coup = 0

      # system → devinette JcJ
      while reponse != nbr_j1:
        if reponse < nbr_j1:
          print("Le nombre à deviner est plus grand")
          nombre_coup = nombre_coup + 1
          reponse = int(input("Joueur 2, quel est votre nombre ?\n"))
        if reponse > nbr_j1:
          print("Le nombre à deviner est plus petit")
          nombre_coup = nombre_coup + 1
          reponse = int(input("Joueur 2, quel est votre nombre ?\n"))
        if reponse == nbr_j1:
          print("Bravo ! Vous avez deviné le nombre en", nombre_coup + 1, "coups.")
          error_nbr_joueur = False
#----------------------------------------retry question → nbr_joueur----------------------------------------
  if nbr_joueur > 2:
      nbr_joueur = int(input("Combient de Joueur êtes-vous ? \n1, ou 2 ?\n"))
      error_nbr_joueur = True