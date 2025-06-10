#!/usr/bin/python3






#dicoV qui est la partie visuel de notre morpion, ici on l'initialise.
dicoV = (0, 0, 0, 0, 0, 0, 0, 0, 0)
#dico qui est le fond de notre morpion, j'ai utiliser un systéme de coordonné en ABC, qui ne parait pas trés claire ... 
#probablement a modifier (par exemple en 1A, 2C, 3B ect, et en faisant en sort que 1A et A1 soient 2 réponse acceptable pour utiliser la premiere case)
dico =	{
  "AA":0,
  "AB":0,
  "AC":0,
  "BA":1,
  "BB":0,
  "BC":0,
  "CA":0,
  "CB":0,
  "CC":0
  }

#dico2 est une tentative de comprendre et d'utiliser les ** dans un dictionnaire et les tumples 
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
    for i in dico:
        if i==0:
            dicoV[i]=" "
        elif i<0:
            dicoV[i]="X"
        elif i>0:
            dicoV[i]="O"
    print(" ", line[0], line[1], line[2])
print(line[0], dicoV[0], dicoV[1], dicoV[2])
print(line[1], dicoV[3], dicoV[4], dicoV[5])
print(line[2], dicoV[6], dicoV[7], dicoV[8])

# A FINIR Affichage(dico)



#Exemples de fonctions
#date = input('Entrez votre date de naissance : ')
#age = (2018 - int(date))
#print('Vous avez  ', age, 'ans')

#print("\n",case['AA'])
