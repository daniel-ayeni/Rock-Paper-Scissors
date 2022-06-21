# import random from Python built-in modules
import random

# choices variable is created to hold a list of values which are "Rock", "Paper", "Scissors" for the game
choices = ["Rock", "Paper", "Scissors"]
# Computer variable is created and given a value at random from choices
computer = random.choice(choices)
# Player variable is created and assigned a boolean value of False
player = False
# Computer Score variable is created and assigned a value of zero
cpu_score = 0
# Player Score variable is created and assigned a value of zero
player_score = 0
# While loop starts and continues to run the code within its indentation till the conditions become false or break
while True:
    # Receives input from user and capitalizes it then stores in player variable
    player = input("Rock, Paper or  Scissors?  >_").capitalize()

    # Conditions for the game
    # If both the player and computer select the same , It is a TIE
    if player == computer:
        # TIE is displayed
        print("TIE!")
        # Computer variable is given a value at random from choices again
        computer = random.choice(choices)
    # If Player chooses ROCK and Computer randomly chooses PAPER, Player Loses
    elif player == "Rock":
        if computer == "Paper":
            # YOU LOSE!, Paper covers Rock is displayed
            print("YOU LOSE!", computer, "covers", player)
            # 1 is added to the current score of computer
            cpu_score += 1
            # Computer variable is given a value at random from choices again
            computer = random.choice(choices)
        # If Player chooses ROCK and Computer randomly chooses SCISSORS, Computer Loses
        else:
            # YOU WIN!, Rock smashes paper is displayed
            print("YOU WIN!", player, "smashes", computer)
            # 1 is added to the current score of Player
            player_score += 1
    # If Player chooses PAPER and Computer randomly chooses SCISSORS, Player Loses
    elif player == "Paper":
        if computer == "Scissors":
            #  YOU LOSE!, Scissors cut paper is displayed
            print("YOU LOSE!", computer, "cut", player)
            # 1 is added to the current score of computer
            cpu_score += 1
            # Computer variable is given a value at random from choices again
            computer = random.choice(choices)
        # If Player chooses Paper and Computer randomly chooses Rock, Computer Loses
        else:
            # YOU WIN!, Paper covers Rock is displayed
            print("YOU WIN!", player, "covers", computer)
            # 1 is added to the current score of Player
            player_score += 1
            # Computer variable is given a value at random from choices again
            computer = random.choice(choices)
    # If Player chooses SCISSORS and Computer randomly chooses ROCK, Player Loses
    elif player == "Scissors":
        if computer == "Rock":
            # YOU LOSE!, Rock smashes Scissors is displayed
            print("YOU LOSE!", computer, "smashes", player)
            # 1 is added to the current score of computer
            cpu_score += 1
            # Computer variable is given a value at random from choices again
            computer = random.choice(choices)
        # If Player chooses SCISSORS and Computer randomly chooses PAPER, Computer Loses
        else:
            #  YOU WIN!, Scissors cut paper is displayed
            print("YOU WIN!", player, "cut", computer)
            # 1 is added to the current score of Player
            player_score += 1
            # Computer variable is given a value at random from choices again
            computer = random.choice(choices)
    # If Player chooses Enters/ inputs "Stop" or "End" or "Quit" or "Q", The game ends and the results are displayed
    elif player == "Stop" or "End" or "Quit" or "Q":
        print("Final Scores:")
        #  Computer Score is displayed using format style 1
        print("CPU:{}".format(cpu_score))
        #  Player Score is displayed using format style 2
        print(f"Player:{player_score}")
        # This terminates the while loop
        break
