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
    print(visuelF[:(taille+1)],"\n")
    for i in range(1, (taille-1)):
        print(visuelF[(taille+i):(taille+i+2)],"\n")
        print(taille+i)
        print(taille+i+2)
Affichage(dico)

# ligne 60, 61, 62, 63 n'apparaisse pas ??
# ligne 62 et 63 sont la pour voir ce qui cloche

#fruits = ['pomme', 'banane', 'orange']
#for index, fruit in enumerate(fruits):
#    print(index, fruit)