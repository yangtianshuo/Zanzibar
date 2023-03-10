'''
Zanzibar

Game rules:
Player and computer each starts with 20 chips. On player's turn, they roll three six-sided dice. The first player of a round may choose to reroll up to two additional times, taking the 
best roll. Subsequent player may only roll as many times as the first. The best roll is a 4-5-6. Then three of a kind. The next best roll is 1-2-3. Other hands are scored by the sum of 
the scores of each die with the following scale:
1 = 100 points
6 = 60 points
2 = 2 points
3 = 3 points
4 = 4 points
5 = 5 points
The player with the lowest score loses, and takes chips from the other player based on the winning roll: 1 chip normally, 2 chips if winning roll was 1-2-3, 3 chips if winning roll was 
three of a kind, and 4 chips if winning roll was 4-5-6. The winner goes first for the next round. The first player to run out of chips wins.
'''

import random as r

def determine_turn():
    while True:
        try:
            n = int(input("Enter a positive integer for player first, 0 or negative for computer first: "))
        except ValueError:
            print("Not an integer")
        else:
            if n > 0:
                return True
            else:
                return False

#Roll 3 dices
#Return the roll
def roll_func():
    roll = []
    dice1 = r.randint(1,6)
    dice2 = r.randint(1,6)
    dice3 = r.randint(1,6)
    roll.extend([dice1,dice2,dice3])
    roll.sort()
    return roll

#Assign a type to each roll
#Return roll type
def roll_type_func(roll):
    if roll == [4,5,6]:
        roll_type = 4
    elif roll.count(roll[0]) == len(roll):
        roll_type = 3
    elif roll == [1,2,3]:
        roll_type = 2
    else:
        roll_type = 1
    return roll_type

#Assign points based on roll
#Return the number of points
def roll_type1(roll):
    points = 0
    for i in range(len(roll)):
        if roll[i] == 1:
            points += 100
        elif roll[i] == 6:
            points += 60
        elif roll[i] == 2:
            points += 2
        elif roll[i] == 3:
            points += 3
        elif roll[i] == 4:
            points += 4
        else:
            points += 5
    return points

#Play one round of the game
#Return the results of one round
def one_round(turn):
    player_roll_types = []
    computer_roll_types = []
    player_points = []
    computer_points = []
    if turn == True:
        num_rolls = 0
        for i in range(3):
            roll = roll_func()
            print("Player roll " + str(i+1) + ":",roll)
            roll_type = roll_type_func(roll)
            if roll_type == 1:
                points = roll_type1(roll)
                player_points.append(points)
            player_roll_types.append(roll_type)
            num_rolls += 1
            if num_rolls < 3:
                while True:
                    try:
                        n = int(input("Enter a positive integer to continue rolling, any other integer to stop: "))
                        break
                    except ValueError:
                        print("Not an integer")
            if n <= 0:
                break
        for i in range(num_rolls):
            roll = roll_func()
            print("Computer roll " + str(i+1) + ":",roll)
            roll_type = roll_type_func(roll)
            if roll_type == 1:
                points = roll_type1(roll)
                computer_points.append(points)
            computer_roll_types.append(roll_type)
    else:
        num_rolls = 0
        for i in range(3):
            roll = roll_func()
            print("Computer roll " + str(i+1) + ":",roll)
            roll_type = roll_type_func(roll)
            if roll_type == 1:
                points = roll_type1(roll)
                computer_points.append(points)
            computer_roll_types.append(roll_type)
            num_rolls += 1
            if roll_type == 4 or roll_type == 3 or roll_type == 2:
                break
        for i in range(num_rolls):
            roll = roll_func()
            print("Player roll " + str(i+1) + ":",roll)
            roll_type = roll_type_func(roll)
            if roll_type == 1:
                points = roll_type1(roll)
                player_points.append(points)
            player_roll_types.append(roll_type)
    return player_roll_types,computer_roll_types,player_points,computer_points

def game_func():
    round_num = 1
    player_chips = 20
    computer_chips = 20
    turn = determine_turn()
    print()
    while player_chips > 0 and computer_chips > 0:
        print("Round",round_num,"---")
        result = one_round(turn)
        max_player = max(result[0])
        max_computer = max(result[1])
        if max_player > max_computer:
            for i in range(2,5):
                if max_player == i:
                    player_chips += i
                    computer_chips -= i
            turn = True
        elif max_computer > max_player:
            for i in range(2,5):
                if max_computer == i:
                    player_chips -= i
                    computer_chips += i
            turn = False
        else:
            if max_player == 1:
                max_player = max(result[2])
                max_computer = max(result[3])
                if max_player > max_computer:
                    player_chips += 1
                    computer_chips -= 1
                    turn = True
                elif max_computer > max_player:
                    player_chips -= 1
                    computer_chips += 1
                    turn = False
        print("Player chips:",player_chips)
        print("Computer chips:",computer_chips)
        round_num += 1
        print()
    print()
    if player_chips <= 0:
        print("Computer wins")
    if computer_chips <= 0:
        print("Player wins")

game_func()