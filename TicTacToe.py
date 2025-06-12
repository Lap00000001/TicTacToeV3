#!/usr/bin/python3
#git commit TicTacToe.py
# créer le message de commit
#ctrl O (depend de nano, l'editeur de text du terminal)
# touche entrée ou qqchose comme ça
#ctrl x
#git push origin main
#
#ces commandes permettent de mettre a jour le github 

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
    for i in range(1, (taille*2), 2):
        print(visuelF[(taille+i):(taille+i+2)],"\n")
Affichage(dico)


# winCondition : fonctionnement "3 en ligne, 3 en column, ou 3 en diagonal => win /// if not => draw"

# toursSysteme : fonctionnement "on commence a un tour et on repette jusqu'a ce que winCondition reagisse, si winCondition [0] == true => fin du compteur de tour,
#                   reinitialisation du compteur de tour, de dico, de visuel, visuelF et de wincond, ET demandez "voulez vous rejouer"

# jouez : fonctionnement "demander au joueur x de jouer /// if wrong input => message error ET joueur x rejoue /// implémenter l'index jouer par joueur X avec -1 ET passez au joueur O
#               demander a joueur O de jouer /// error message too /// impl l'index jouer par joueur O avec +1 ET passe au joueur suivant" Tant que windcond[1] =/= 0

# Et c'est fini



#fruits = ['pomme', 'banane', 'orange']
#for index, fruit in enumerate(fruits):
#    print(index, fruit)