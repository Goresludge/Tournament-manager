#!/usr/bin/python3
from operator import itemgetter, attrgetter
from random import shuffle
import random


class Player:
    def __init__(self, player_no, name, games_played, cpu, cpu_level, points):
        self.player_no = player_no
        self.name = name
        self.games_played = games_played
        self.cpu = cpu
        self.cpu_level = cpu_level
        self.points = points
        self.data = [player_no, name, games_played, cpu, cpu_level, points]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr((self.player_no, self.name, self.games_played, self.cpu, self.cpu_level, self.points))

    def display_player(self):
        print(str(self.player_no) + ".", "Name: ", self.name, ", Games played", self.games_played,
              ", CPU level: ", self.cpu_level, "Points: ", self.points)

    def update_player(self, point):
        self.points += point
        self.games_played += 1


def simulate_game(list_input):

    if random.randint(0, 10) == 7:
        # gives player_no
        a = list_input[0][0]
        b = list_input[1][0]
        print("It's a draw between", players[a].name, "and", players[b].name+"!")
        players[a].update_player(1)
        players[b].update_player(1)
    else:
        shuffle(list_input)
        winner = list_input[0][0]
        loser = list_input[1][0]
        players[winner].update_player(3)
        players[loser].update_player(0)
        print(players[winner].name, "won!")


# Next Game Round Robin
def next_game_rr(num):
    # m_list = []
    all_games = []
    print_rr_table()
    total_games = int((num*((1+num)/2))-num)
    i = 1
    for x in range(0, num-1):
        for y in range(i, num):
            m_list = [players[x], players[y]]
            all_games.append(m_list)
        i += 1
    shuffle(all_games)
    sorted_list = sort_played(all_games)
    for x in range(0, total_games):
        print("Round", x+1)
        updated_list = update_list(sorted_list)
        sorted_list = sort_played(sorted_list)
        simulate_game(sorted_list[0])
        del sorted_list[0]
        print_rr_table()


# Generate Elimination Tournament
def elim_tourney(num):
    total_games = 0
    player_list = players
    while total_games < num-1:
        player_list, total_games = play_next_round(player_list, total_games)
    return player_list


def play_next_round(player_list, total_games):
    i = 0
    next_round = []
    while i < len(player_list):

        try:
            m_list = [players[i], players[i+1]]
            simulate_game(m_list)
            total_games = total_games + 1
            if players[i][5] > players[i+1][5]:
                next_round.append(players[i])
            else:
                next_round.append(players[i+1])

        except:
            next_round.append(players[i])
        i = i+2
    return next_round, total_games

def print_t_table(list_input):
    max_width = name_width(players) + 3
    for x in range(0,list_input):
        if(x % 2 != 0):
            print("-VS-".ljust(max_width),"Winner"+"\n"+players[x].name)
        else:
            if(x+1 == list_input):
                len(players[x].name)
                print("\n\n"+players[x].name.ljust(max_width),"Winner")
            else:
                print("\n"+players[x].name)

def update_list(list_input):
    for x in range(0,len(list_input)):
        list_input[x][0][2] = players[list_input[x][0][0]].games_played
        list_input[x][1][2] = players[list_input[x][1][0]].games_played
    return list_input

def sort_played(list_input):
    sorted_list = sorted(list_input, key=lambda x: (x[0][2], x[1][2]))
    return sorted_list


def name_width(list_input):
    max_width = 4
    for elem in list_input:
        x = elem[0]
        width = len(players[x].name)
        if max_width < width:
            max_width = width
    return max_width


def print_rr_table():
    m_list = sorted(players, key=lambda player: player.points, reverse=True)
    i = 1
    max_width = name_width(m_list)
    print("  ", "Name".ljust(max_width), "| Played | Points")
    for elem in m_list:
        x = elem[0]
        print(str(i) + ".", players[x].name.ljust(max_width), "|  ",
              str(players[x].games_played), "   |  ", str(players[x].points))
        i += 1


def input_name(x, name_list):
    valid_name = False
    while valid_name == False:
        name = input("Input name for player " + str(x+1) + ":")
        valid_name = True
        if len(name) > 20:
            print("Please input a shorter name (less than 20 characters)")
            valid_name = False
        if len(name) < 1:
            valid_name = False
        if name in name_list:
            print("Someone already picked", name, "as their name")
            valid_name = False
    name_list.append(name)
    return name


def new_player_class(num, mode):
    name_list = []
    for x in range(0, num):
        player_no = x
        name = input_name(x, name_list)
        games_played = 0
        cpu = False
        cpu_level = 0
        points = 0

        if mode == 2 and x == 1:
            cpu = True
            cpu_level = select_cpu_level()

        if mode == 3:
            cpu = True
            cpu_level = select_cpu_level()

        if mode == 4 or mode == 5:
            cpu = select_cpu()
            if cpu == True:
                cpu_level = select_cpu_level()

        if cpu == True:
            name = name + "(CPU" + str(cpu_level) + ")"

        new_player = Player(player_no, name, games_played, cpu, cpu_level, points)
        players.append(new_player)

    return players


def select_cpu():
    selection = ""
    while selection != "y" and selection != "Y" and selection != "n" and selection != "N":
        selection = input("CPU controlled(y or n)?")
        if selection == "y" or selection == "Y":
            cpu = True

        if selection == "n" or selection == "N":
            cpu = False
    return cpu


def select_cpu_level():
    cpu_level = 0
    while cpu_level > 3 or cpu_level < 1:
        try:
            cpu_level = int(input("Input CPU difficulty (1-3):"))
        except ValueError:
            print("Please type in a number")
            continue

    return cpu_level


def select_game_type():
    selected_mode = 0
    while selected_mode > 6 or selected_mode < 1:
        try:
            selected_mode = int(input("Input mode:"))
            if selected_mode > 5 or selected_mode < 1:
                print("Input a number between 1 and 5")
        except ValueError:
            print("Please type in a number")
            continue
    return selected_mode


def input_players():
    no_of_players = 0
    while no_of_players > 8 or no_of_players < 3:
        try:
            no_of_players = int(input("How many players (between 3 and 8)? "))
            if no_of_players > 5 or no_of_players < 1:
                print("Input a number between 3 and 8")
        except ValueError:
            print("Please type in a number")
            continue
    return no_of_players


def start_menu():

    print("Welcome to <insert game name>!")
    print("Please input a game mode")
    print("1. Player vs Player")
    print("2. Player vs CPU")
    print("3. CPU vs CPU")
    print("4. Round robin tournament")
    print("5. Elimination tournament")

    mode = select_game_type()

    if mode == 1:
        print("Player vs player")
        new_player_class(2, mode)
        simulate_game(players)
        print("1.", players[0].name)
        print("2.", players[1].name)

    if mode == 2:
        print("Player vs CPU")
        new_player_class(2, mode)
        simulate_game(players)
        print("1.", players[0].name)
        print("2.", players[1].name)

    if mode == 3:
        print("CPU vs CPU")
        new_player_class(2, mode)
        print("1.", players[0].name)
        print("2,", players[1].name)

    if mode == 4:
        print("Round robin tournament selected")
        no_of_players = input_players()
        new_player_class(no_of_players, mode)
        next_game_rr(no_of_players)

    if mode == 5:
        print("Elimination tournament selected")
        no_of_players = input_players()
        new_player_class(no_of_players, mode)
        winner = elim_tourney(no_of_players)
        print(winner[0][1], "won the tournament!")
    if mode == 6:
        # Just a test mode
        new_player = Player(0, "a", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(1, "b", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(2, "c", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(3, "d", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(4, "e", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(5, "test6", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(6, "test7", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(7, "test8", 0, False, 0, 0)
        players.append(new_player)
        print_t_table(5)


players = []
start_menu()
