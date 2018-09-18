#!/usr/bin/python3
from random import shuffle

class Player:
    def __init__(self, playerNo, name, gamesPlayed, cpu, cpuLevel,points):
        self.playerNo = playerNo
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.cpu = cpu
        self.cpuLevel = cpuLevel
        self.points = points
        self.info = [playerNo, name, gamesPlayed, cpu, cpuLevel,points]
    def __getitem__(self,index):
        return self.info[index]
    def __repr__(self):
        return repr((self.playerNo,self.name,self.gamesPlayed, self.cpu, self.cpuLevel,self.points))
    def displayPlayer(self):
        print (str(self.playerNo)+".", "Name: ", self.name,", Games played",self.gamesPlayed, ", CPU level: ", self.cpuLevel, "Points: ", self.points)
    def updatePlayer(self,point):
        self.points += point
        self.gamesPlayed += 1

def simulateGame(player1,player2):

    list = [player1,player2]
    shuffle(list)
    winner = list[0][0]
    loser = list[1][0]
    players[winner].updatePlayer(3)
    players[loser].updatePlayer(0)

def nextGameRoundRobin(num):
    printRoundRobinTable()
    totalGames = (num*((1+num)/2))-num
    for x in range(0,int(totalGames)):
        list = sorted(players, key=lambda player: player.gamesPlayed)
        simulateGame(list[0],list[1])
        printRoundRobinTable()
        shuffle(list)

def sortRoundRobinTable():
    list = sorted(players, key=lambda player: player.points, reverse=True)
    return list

def printRoundRobinTable():
    list = sortRoundRobinTable()
    i = 1
    width = 0
    maxWidth = 4
    for elem in list:
        x = elem[0]
        width = len(players[x].name)
        if(maxWidth<width):
            maxWidth = width
    print("  ","Name".ljust(maxWidth),"| Played | Points")
    for elem in list:
        x = elem[0]
        print(str(i)+".",players[x].name.ljust(maxWidth),"|  ",str(players[x].gamesPlayed),"   |  ",str(players[x].points))
        i += 1

def inputName(x,nameList):
    validName = False
    while validName == False:
        name = input("Input name for player " + str(x+1) + ":")
        validName = True
        if (len(name) > 20):
            print("Please input a shorter name (less than 20 characters)")
            validName = False
        if (len(name) < 1):
            validName = False
        if name in nameList:
            print("Someone already picked",name,"as their name")
            validName = False
    nameList.append(name)
    return name

def newPlayerClass(num, mode):
    list = []
    for x in range(0,num):
        playerNo = x
        name = inputName(x,list)
        gamesPlayed = 0
        cpu = False
        cpuLevel = 0
        points = 0
        if(mode == 2 and x == 1):
            cpu = True
            cpuLevel = selectCpuLevel()
        if(mode == 3):
            cpu = True
            cpuLevel = selectCpuLevel()
        if(mode == 4 or mode == 5):
            cpu = selectCpu()
            if cpu == True:
                cpuLevel = selectCpuLevel()
        if(cpu == True):
            name = name + "(CPU"+ str(cpuLevel)+")"
        new_player = Player(playerNo,name,gamesPlayed,cpu,cpuLevel,points)
        players.append(new_player)

    return players

def selectCpu():
    selection = ""
    while (selection != "y" and selection != "Y" and selection != "n" and selection != "N"):
        selection = input("CPU controlled(y or n)?")
        if (selection == "y" or selection == "Y"):
            cpu = True
        if (selection == "n" or selection == "N"):
            cpu = False
    return cpu

def selectCpuLevel():
    cpuLevel = 0
    while cpuLevel > 3 or cpuLevel < 1:
        try:
            cpuLevel = int(input("Input CPU difficulty (1-3):"))
        except ValueError:
            print("Please type in a number")
            continue

    return cpuLevel

def selectGameType():
    selectedMode = 0
    while selectedMode > 6 or selectedMode < 1:
        try:
            selectedMode = int(input("Input mode:"))
            if(selectedMode > 5 or selectedMode < 1):
                print("Input a number between 1 and 5")
        except ValueError:
            print("Please type in a number")
            continue
    return selectedMode

def inputPlayers():
    numberOfPlayers = 0
    while numberOfPlayers > 8 or numberOfPlayers < 3:
        try:
            numberOfPlayers = int(input("How many players (between 3 and 8)? "))
            if(numberOfPlayers > 5 or numberOfPlayers < 1):
                print("Input a number between 3 and 8")
        except ValueError:
            print("Please type in a number")
            continue
    return numberOfPlayers

def startMenu():

    print("Welcome to <insert game name>!")
    print("Please input a game mode")
    print("1. Player vs Player")
    print("2. Player vs CPU")
    print("3. CPU vs CPU")
    print("4. Round robin tournament")
    print("5. Elimination tournament")

    mode = selectGameType()

    if mode == 1:
        print("Player vs player")
        newPlayerClass(2,mode)
        print("1.",players[0].name)
        print("2.",players[1].name)
    if mode == 2:
        print("Player vs CPU")
        newPlayerClass(2,mode)
        print("1.",players[0].name)
        print("2.",players[1].name)
    if mode == 3:
        print("CPU vs CPU")
        newPlayerClass(2,mode)
        print("1.",players[0].name)
        print("2,",players[1].name)
    if mode == 4:
        print("Round robin tournament selected")
        numberOfPlayers = inputPlayers()
        newPlayerClass(numberOfPlayers,mode)
        printRoundRobinTable()
    if mode == 5:
        print("Elimination tournament selected")
        numberOfPlayers = inputPlayers()
        newPlayerClass(numberOfPlayers,mode)
    if mode == 6:
        #Just a test mode
        new_player = Player(0,"test1",0,False,0,0)
        players.append(new_player)
        new_player = Player(1,"test2",0,False,0,0)
        players.append(new_player)
        new_player = Player(2,"test3",0,False,0,0)
        players.append(new_player)
        new_player = Player(3,"test4",0,False,0,0)
        players.append(new_player)
        nextGameRoundRobin(4)
players = []
startMenu()
