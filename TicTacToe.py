#!/usr/bin/python3
#git commit TicTacToe.py
# créer le message de commit
#ctrl O (depend de nano, l'editeur de text du terminal)
# touche entrée ou qqchose comme ça
#ctrl x
#git push origin main
#
#ces commandes permettent de mettre a jour le github 

# et du rendu, et du fonctionnement "3 en ligne, 3 en column, ou 3 en diagonal => win"

taille=int(input('donner la taille de votre morpion ?'))
taille2=taille*2
colonne=[chr(i+65)for i in range(taille2)]
colonne
ligne=colonne[int(taille):]
colonne = colonne[:int(taille)]
print(colonne)
for i in ligne:
   print(i)

tailleSquare=taille2**2
visuel=[0 for i in range(tailleSquare)]
dico={}
listeindex=[]
for i in range(taille):
    for y in range(taille):
        listeindex.append(colonne[y]+ligne[i])
def creadico():
    for i in range(len(listeindex)):
        dico[listeindex[i]]=0
creadico()
print(dico)

visuelF=[" "]

#on refait la fonction ci dessus en un print:
#on va créer une liste (visuelF) qui nous serviras a print seulement la notre rendu final grace a visuel qui est une liste un peu plus graphique de l'etat de notre dico

#pas sur d'avoir compris thaumaturge ce que je viens de copier dans les 2 lignes du dessous
def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def Affichage(dico):
    for index,fruit in enumerate(dico.values()):
        if fruit==0:
            visuel[index]=" "
        if fruit<0:
            visuel[index]="X"
        if fruit>0:
            visuel[index]="O"
    chunks = split_list(visuel, taille)
    for i in range(taille):
        visuelF.append(colonne[i])
    for i in range(taille):
        visuelF.append(ligne[i])
        visuelF.append(chunks[i])
    chunks2 = split_list(visuelF, (taille+1))
    for i in range(0, (taille+1)):
        print(chunks2[i],"\n")
Affichage(dico)

#print(" ", line[0], line[1], line[2])
#    print(line[0], visuel[0], visuel[1], visuel[2])
#    print(line[1], visuel[3], visuel[4], visuel[5])
#    print(line[2], visuel[6], visuel[7], visuel[8])

#print("\n",case['AA'])
#fruits = ['pomme', 'banane', 'orange']
#for index, fruit in enumerate(fruits):
#    print(index, fruit)
# utiliser un modulot pour rajouter un "\n" dans les printX4 pour automatiser le truc (le modulo depends de la taille du plateau, demander la taille du plateau au debut)