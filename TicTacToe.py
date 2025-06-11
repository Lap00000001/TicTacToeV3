#!/usr/bin/python3
#git commit TicTacToe.py
# créer le message de commit
#ctrl O (depend de nano, l'editeur de text du terminal)
# touche entrée ou qqchose comme ça
#ctrl x
#git push origin main
#
#ces commandes permettent de mettre a jour le github 


# on aimerais pouvoir a termes avoir le tictactoe avec 4X4 ou 5X5 ou 6X6 ect, voir 5X6
# Donc il va falloir penser en amont a comment on fabrique le dictionnaire a partir de 2 liste, il faudrait automatiser la création du dico,
#  et du rendu, et du fonctionnement "3 en ligne, 3 en column, ou 3 en diagonal => win"

#petit essaie de thomas pour automatiser une partie du systeme ligne colonne:
#taille=6
#colonne=[chr(i+65)for i in range(taille)]
#colonne= ['A','B','C', 'D', 'E', 'F']
#ligne=colonne[:3]  #on slice du début à trois
#ligne #['A', 'B', 'C']
#colonne= colonne [3:]  #on slice de 3 jusqu'à la fin
#colonne #['D', 'E', 'F']
#colign = [chr(i+65) for i in range (taille)]
#ligne = colonne [:int(len(colign)/2)]  #int pour etre sur que c'est un entier, len(colign) c'est la taille de colign
#colonne = colonne[int(len(colign)/2):]
#print(ligne)
#for i in colonne:
#   print(i)



#visuel qui est la partie visuel de notre morpion, ici on l'initialise.
visuel = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#dico qui est le fond de notre morpion, j'ai utiliser un systéme de coordonné en ABC, qui ne parait pas trés claire ... 
#probablement a modifier (par exemple en 1A, 2C, 3B ect, et en faisant en sort que 1A et A1 soient 2 réponse acceptable pour utiliser la premiere case)
dico =	{
  "AA":0,
  "AB":0,
  "AC":0,
  "BA":-1,
  "BB":-1,
  "BC":1,
  "CA":1,
  "CB":0,
  "CC":0
  }

#dico2 est une tentative de comprendre et d'utiliser les ** dans un dictionnaire et les tupples 
#dico2 =	(**{"AA":0, "AB":-1, "AC":0}, **{"BA":1, "BB":0, "BC":0}, **{"CA":0, "CB":0, "CC":0})

#la fonction ligne me sert pour faire mes coordonées, il faudras recrée une fonction colomn, et éditer les fonction suivantes (et precedente) afain qu'il y aie des coordonnées en 1A ou en A1 , est que les 2 matrice soit liéé
line = ("A","B","C")

#ici on imprime notre morpion, pour le moment la partie graphique n'est pas présente, une fois faites, ce print disparaitras dans les limbes
print(" ", line[0], line[1], line[2])
print(line[0], dico['AA'], dico['AB'], dico['AC'])
print(line[1], dico['BA'], dico['BB'], dico['BC'])
print(line[2], dico['CA'], dico['CB'], dico['CC'])
#d'ailleur les premieres case de chaque print deviendront respectivement : " ";column[0];column[1];column[2];
#une fois que la fonction dico auras des 123 dans ses coordonnées, le premiers print seras le meme mais tous les "dico['AA'] deviendront "dico['_column[X]__line[Y]']


def Affichage(dico):
    for index,fruit in enumerate(dico.values()):
            if fruit==0:
                visuel[index]=" "
            if fruit<0:
                visuel[index]="X"
            if fruit>0:
                visuel[index]="O"
    print(" ", line[0], line[1], line[2])
    print(line[0], visuel[0], visuel[1], visuel[2])
    print(line[1], visuel[3], visuel[4], visuel[5])
    print(line[2], visuel[6], visuel[7], visuel[8])

Affichage(dico)



#Exemples de fonctions
#date = input('Entrez votre date de naissance : ')
#age = (2018 - int(date))
#print('Vous avez  ', age, 'ans')

#print("\n",case['AA'])

#fruits = ['pomme', 'banane', 'orange']
#for index, fruit in enumerate(fruits):
#    print(index, fruit)

# utiliser un modulot pour rajouter un "\n" dans les printX4 pour automatiser le truc (le modulo depends de la taille du plateau, demander la taille du plateau au debut)

fruits = ['pomme', 'banane', 'orange']
for index, fruit in enumerate(fruits):
    print(index, fruit)