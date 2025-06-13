#!/usr/bin/python3
#git commit TicTacToe.py
# créer le message de commit
#ctrl O (depend de nano, l'editeur de text du terminal)
# touche entrée ou qqchose comme ça
#ctrl x
#git push origin main
#
#ces commandes permettent de mettre a jour le github 

#-----------------------------------------------------Block init & variable-----------------------------------------------------
sumListeWin=[]
listeWin=[]
listesC=[]
listesL=[]
listeD_0=[]
listeD_1=[]
visuelF=[" "]
tour=0
pTour=2
alreadyPlayed=[]
wrongK=0
p1=-1
p2=+1
player=0

taille=int(input('donner la taille de votre morpion ?'))
colonne=[chr(i+65)for i in range(taille*2)]
colonne
ligne=colonne[int(taille):]
colonne = colonne[:int(taille)]
#print(colonne)                                         ##########              
#for i in ligne:                                        ##########
#   print(i)                                            ##########
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
#print(dico)                                            ##########
liste_cles=list(dico.keys())    #pour faire appelle aux valeurs du dico par index et non par clé



def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

#dico={"AD":0,                                          ##########
#      "BD":-1,                                         ##########
#      "CD":1,                                          ##########
#      "AE":-1,                                         ##########
#      "BE":1,                                          ##########
#      "CE":-1,                                         ##########
#      "AF":1,                                          ##########
#      "BF":0,                                          ##########
#      "CF":1                                           ##########
#      }                                                ##########
#print(dico)                                            ##########
#----------------------------------------------------------Block tour-----------------------------------------------------
def fTour():
    tour=tour+1
    if tour % 2 == 0:
        return 0
    if tour % 2 != 0:
        return 1
if fTour == 1:
    ptour=1
if fTour == 0:
    ptour=2

#---------------------------------------------------------Block affichage-----------------------------------------------------
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
#Affichage(dico)                                     ##########

#-----------------------------------------------------Block winCondition-----------------------------------------------------
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
#for i, listec in enumerate(listesC):                ##########
#    print(f"ListeC {i} : {listec}")                 ##########
#for i, listel in enumerate(listesL):                ##########
#    print(f"ListeL {i} : {listel}")                 ##########
#print("ListeD_0 :", listeD_0)                       ##########
#print("ListeD_1 :", listeD_1)                       ##########
for i in range(len(listesC)):
    listeWin.append(listesC[i])
for i in range(len(listesL)):
    listeWin.append(listesL[i])
listeWin.append(listeD_0)
listeWin.append(listeD_1)
#print(listeWin)                                     ##########
sumListeWin=[sum(sous_liste) for sous_liste in listeWin]
#print(sumListeWin)                                  ##########
def winCondition():
    #Draw
    if fTour == tailleSquare:
        print(f"Draw, {fTour} have been played")
        return 1
    #Win
    for i in range(len(sumListeWin)):
        if sumListeWin[i]==taille:
            print("Player 2 won")
            return 1
        if sumListeWin[i]==(-taille):
            print("Player 1 won")
            return 1
    return 0

#-----------------------------------------------------Block Playing-----------------------------------------------------
def playme(input:f"Player {pTour} chooses a play please"):
    Affichage
    if pTour==1:
        player=int(p1)
    if pTour==2:
        player=int(p2)
    if dico.get(input) == None:
        print("Wrong keys try something like AF")
        return wrongK==1
    if alreadyPlayed.get(input):
        print("Already played this combinaison, try again")
        return wrongK==1
    if wrongK==0:
        alreadyPlayed.append(input)
        winCondition
        fTour
        dico[input]=player

def run1():
    while winCondition==0:
        playme
        wrongK==0
run1
# jouez : fonctionnement "demander au joueur x de jouer /// if wrong input => message error ET joueur x rejoue /// implémenter l'index jouer par joueur X avec -1 ET passez au joueur O
#               demander a joueur O de jouer /// error message too /// impl l'index jouer par joueur O avec +1 ET passe au joueur suivant" Tant que windcond =/= 0

# demandez "voulez vous rejouer" (if wincond == 1 => ...)
