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
colonne=[chr(i+65)for i in range(taille*2)]
colonne
ligne=colonne[int(taille):]
colonne = colonne[:int(taille)]
#print(colonne)         ##################
#for i in ligne:
#   print(i)

tailleSquare=taille**2
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
#print(dico)         ##################

visuelF=[" "]

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

########TEST############
dico={"AD":0,
      "BD":-1,
      "CD":3,
      "AE":-2,
      "BE":5,
      "CE":-6,
      "AF":9,
      "BF":155,
      "CF":2
      }
print(dico)
#############TEST############

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



liste_cles=list(dico.keys())    #pour faire appelle aux valeurs du dico par index et non par clé


listesC=[]
listesL=[]
listeD_0=[]
listeD_1=[]
for i in range(taille):
    listesC.append([])   #on ajoute une nouvelle liste vide à chaque itération
    for y in range(i, taille*(taille-1)+i+1, taille):
        listesC[i].append(dico[liste_cles[y]])

for i in range(taille):
    listesL.append([])
    for y in range(taille*i, taille*(i+1), 1):
        listesL[i].append(dico[liste_cles[y]])

for y in range(taille):
    listeD_0.append(dico[liste_cles[(y+1)*(taille-1)]])
for y in range(taille):
    listeD_1.append(dico[liste_cles[y*(taille+1)]])

for i, listec in enumerate(listesC):                ##########
    print(f"ListeC {i} : {listec}")
for i, listel in enumerate(listesL):                ##########
    print(f"ListeL {i} : {listel}")
print(listeD_0)
print(listeD_1)

# winCondition : fonctionnement "3 en ligne, 3 en column, ou 3 en diagonal => win /// if not => draw"


# toursSysteme : fonctionnement "on commence a un tour et on repette jusqu'a ce que winCondition reagisse, si winCondition == true => fin du compteur de tour,
#                   reinitialisation du compteur de tour, de dico, de visuel, visuelF et de wincond, ET demandez "voulez vous rejouer"

# jouez : fonctionnement "demander au joueur x de jouer /// if wrong input => message error ET joueur x rejoue /// implémenter l'index jouer par joueur X avec -1 ET passez au joueur O
#               demander a joueur O de jouer /// error message too /// impl l'index jouer par joueur O avec +1 ET passe au joueur suivant" Tant que windcond =/= 0

# Et c'est fini



#fruits = ['pomme', 'banane', 'orange']
#for index, fruit in enumerate(fruits):
#    print(index, fruit)