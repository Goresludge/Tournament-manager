#!/usr/bin/python3

class Player:
    def __init__(self, playerNo, name, cpu, cpuLevel,points):
        self.playerNo = playerNo
        self.name = name
        self.cpu = cpu
        self.cpuLevel = cpuLevel
        self.points = points
    def displayPlayer(self):
        print (str(self.playerNo)+".", "Name: ", self.name, ", CPU level: ", self.cpuLevel, "Points: ", self.points)

def newPlayerClass(players, mode):
    for x in range(1,players+1):
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
        player[x] = Player(playerNo,name,cpu,cpuLevel,points)

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
    while selectedMode > 5 or selectedMode < 1:
        try:
            selectedMode = int(input("Input mode:"))
        except ValueError:
            print("Please type in a number")
            continue
    return selectedMode

def inputPlayers():
    numberOfPlayers = 0
    while numberOfPlayers > 8 or numberOfPlayers < 3:
        try:
            numberOfPlayers = int(input("How many players (between 3 and 8)? "))
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
        print(player[1].name)
        print(player[2].name)
    if mode == 2:
        print("Player vs CPU")
        newPlayerClass(2,mode)
        print(player[1].name)
        print(player[2].name, "Difficulty:",player[2].cpuLevel)
    if mode == 3:
        print("CPU vs CPU")
        newPlayerClass(2,mode)
        print(player[1].name, "Difficulty:",player[1].cpuLevel)
        print(player[2].name, "Difficulty:",player[2].cpuLevel)
    if mode == 4:
        print("Round robin tournament selected")
        players = inputPlayers()
        newPlayerClass(players,mode)
    if mode == 5:
        print("Elimination tournament selected")
        players = inputPlayers()
        newPlayerClass(players,mode)

player = {}
startMenu()
