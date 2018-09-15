#!/usr/bin/python3

class Player:
    def __init__(self, playerNo, name, cpu, cpuLevel,points):
        self.playerNo = playerNo
        self.name = name
        self.cpu = cpu
        self.cpuLevel = cpuLevel
        self.points = points
    def displayPlayer(self):
        print ("Name: ", self.name, ", CPU controlled: ", self.cpu, ", CPU level: ", self.cpuLevel, "Points: ", self.points)


def newPlayerClass(players):
    player = {}
    for x in range(1,players+1):
        playerNo = x
        name = input("Input name for player " + str(x) + ":")
        cpu = selectCpu()
        print(cpu)
        if cpu == True:
            cpuLevel = selectCpuLevel()
        else:
            cpuLevel = 0
        points = 0
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
    if mode == 2:
        print("Player vs CPU")
    if mode == 3:
        print("CPU vs CPU")
    if mode == 4:
        print("Round robin tournament selected")
        players = inputPlayers()
        newPlayerClass(players)
    if mode == 5:
        print("Elimination tournament selected")
        players = inputPlayers()
        newPlayerClass(players)

startMenu()
