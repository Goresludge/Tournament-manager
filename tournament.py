#!/usr/bin/python3

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
if mode == 5:
    print("Elimination tournament selected")
    players = inputPlayers()
