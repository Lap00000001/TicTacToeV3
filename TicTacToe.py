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
alreadyPlayed=[]

taille=int(input('donner la taille de votre morpion ?'))
colonne=[chr(i+65)for i in range(taille*2)]
colonne
ligne=colonne[int(taille):]
colonne = colonne[:int(taille)]
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

liste_cles=list(dico.keys())                    ########## a revoir (dico.keys() est deja liste

def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

#---------------------------------------------------------Block affichage-----------------------------------------------------
def Affichage(dico):
    visuelF=[" "]
    for index,fruit in enumerate(dico.values()):
        if fruit==0:
            visuel[index]=" "
        elif fruit<0:
            visuel[index]="X"
        elif fruit>0:
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
#-----------------------------------------------------Block winCondition-----------------------------------------------------

def winCondition(t):
    sumListeWin=[]
    listeWin=[]
    listesC=[]
    listesL=[]
    listeD_0=[]
    listeD_1=[]
    for i in range(taille):
        listesC.append([])
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
    for i in range(len(listesC)):
        listeWin.append(listesC[i])
    for i in range(len(listesL)):
        listeWin.append(listesL[i])
    listeWin.append(listeD_0)
    listeWin.append(listeD_1)
    sumListeWin=[sum(sous_liste) for sous_liste in listeWin]
    #Draw
    if t >= tailleSquare:
        print(f"Draw, {t} have been played")
        return 1
    #Win
    for i in range(len(sumListeWin)):
        print(sumListeWin[i])
        if sumListeWin[i]==taille:
            print("Player 2 won")
            return 1
        if sumListeWin[i]==(-taille):
            print("Player 1 won")
            return 1
    return 0
#------------------------------------------------input_play-----------------------------------
def choice(p,listp):
    liste_players=list(listp.keys())
    for key in liste_players:
        if listp[key]==p:
            p2display=key
    maReponse = input(f"Player {p2display} chooses a play, please:  ")
    isRepInDic=(dico.get(maReponse) == None)
    isAlreadyPlay=(maReponse in alreadyPlayed)
    while (isRepInDic or isAlreadyPlay):
        if isRepInDic:
            print("Wrong keys try something like AF")
        if isAlreadyPlay:
            print(f"{maReponse} is already played, try again")
        maReponse = input(f"Player {p2display} chooses a play, please:  ")
        isRepInDic=(dico.get(maReponse) == None)
        isAlreadyPlay=(maReponse  in alreadyPlayed)
    return maReponse
#-----------------------------------------------------Block Playing-----------------------------------------------------
def playme(reponse,nPlayer):
        alreadyPlayed.append(reponse)
        dico[reponse]=nPlayer

def run1():
    tour=0
    win=False
    players={'player 1' :-1, 'player 2' :+1}
    player=players['player 2']
    while win==False:
        Affichage(dico)
        fTour= 1 if tour%2==0 else 0
        maReponse=choice(player, players)
        playme(maReponse,player)
        tour+=1     #compteur de tour (tour=tour+1)
        winCondition(tour)
        win=winCondition(tour)
        if fTour == 1:
            player=players['player 1']
        if fTour == 0:
            player=players['player 2']        
run1()


# demandez  (if wincond == 1 => )"voulez vous rejouer" et réinitialiser