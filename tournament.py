#!/usr/bin/python3

class Player:
    def __init__(self, playerNo, name, cpu, cpuLevel,points):
        self.playerNo = playerNo
        self.name = name
        self.cpu = cpu
        self.cpuLevel = cpuLevel
        self.points = points
        aList = [playerNo,name,cpu,cpuLevel,points]
        self.info = aList
    def __getitem__(self,index):
        return self.info[index]
    def __repr__(self):
        return repr((self.playerNo,self.name, self.cpu, self.cpuLevel,self.points))
    def displayPlayer(self):
        print (str(self.playerNo)+".", "Name: ", self.name, ", CPU level: ", self.cpuLevel, "Points: ", self.points)
    def displayName(self):
        return self.name

def sortRoundRobinTable():
    list = []
    x = 0
    for player in players:
        list.append(players[x])
        x += 1
    list = sorted(list, key=lambda player: player.points, reverse=True)
    i = 1
    for x in list:
        print(str(i)+".",str(x[1]),str(x[4]),"points")
        i += 1

def newPlayerClass(num, mode):
    for x in range(0,num):
        playerNo = x
        name = input("Input name for player " + str(x) + ":")
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
            name = name + "(CPU)"
        players[x] = Player(playerNo,name,cpu,cpuLevel,points)

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
    if mode == 5:
        print("Elimination tournament selected")
        numberOfPlayers = inputPlayers()
        newPlayerClass(numberOfPlayers,mode)
    if mode == 6:
        #Just a test mode
        players[0] = Player(1,"test1",False,0,3)
        players[1] = Player(2,"test2",False,0,1)
        players[2] = Player(3,"test3",False,0,2)
        players[3] = Player(4,"test4",False,0,0)
        sortRoundRobinTable()
players = {}
startMenu()
