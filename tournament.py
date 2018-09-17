#!/usr/bin/python3

class Player:
    def __init__(self, playerNo, name, gamesPlayed, cpu, cpuLevel,points):
        self.playerNo = playerNo
        self.name = name
        self.gamesPlayed = gamesPlayed
        self.cpu = cpu
        self.cpuLevel = cpuLevel
        self.points = points
        self.info = [playerNo,name,gamesPlayed,cpu,cpuLevel,points]
    def __getitem__(self,index):
        return self.info[index]
    def __repr__(self):
        return repr((self.playerNo,self.name,self.gamesPlayed, self.cpu, self.cpuLevel,self.points))
    def displayPlayer(self):
        print (str(self.playerNo)+".", "Name: ", self.name,", Games played",self.gamesPlayed, ", CPU level: ", self.cpuLevel, "Points: ", self.points)
    def updatePlayer(self,point):
        self.points += point
        self.gamesPlayed += 1
        self.info[2] = self.gamesPlayed
        self.info[5] = self.points

def sortRoundRobinTable():
    list = sorted(players, key=lambda player: player.points, reverse=True)
    return list

def printRoundRobinTable():
    list = sortRoundRobinTable()
    i = 1
    width = 0
    maxWidth = 4
    for x in list:
        print(x)
        width = len(str(x[1]))
        if(maxWidth<width):
            maxWidth = width
    print("  ","Name".ljust(maxWidth),"| Played | Points")
    for x in list:
        print(str(i)+".",str(x[1]).ljust(maxWidth),"|  ",str(x[2]),"   |  ",str(x[5]))
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
        if(mode == 2 and x == 2):
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
        print("2.",players[1].name, "Difficulty:",player[1].cpuLevel)
    if mode == 3:
        print("CPU vs CPU")
        newPlayerClass(2,mode)
        print("1.",players[0].name, "Difficulty:",player[0].cpuLevel)
        print("2,",players[1].name, "Difficulty:",player[1].cpuLevel)
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
        new_player = Player(1,"test1",0,False,0,3)
        players.append(new_player)
        new_player = Player(2,"test2",0,False,0,5)
        players.append(new_player)
        new_player = Player(3,"test3",0,False,0,1)
        players.append(new_player)
        printRoundRobinTable()
players = []
startMenu()
