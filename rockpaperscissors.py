#Jamie Huang
#Rock Paper Scissors
#1/6/25

#Init
import random

#Functions

def rockpaperscissors():
    player_score = 0
    computer_score = 0
    tie = 0
    print("Welcome to Rock, Paper, Scissors")
    while True:

        #Player's choice
        print("Please select one of the three options by inputting a number: ")
        player = input("""Selection:
        1. Rock
        2. Paper
        3. Scissors""")
        if player == "1":
            player = "rock"
        elif player == "2":
            player = "paper"
        elif player == "3":
            player = "scissors"
        else:
            print("Please enter a number.")

        #Computer's choice
        computer = random.randint(1, 3)
        if computer == 1:
            computer = "rock"
            print("Computer chose rock")
        elif computer == 2:
            computer = "paper"
            print("Computer chose paper")
        elif computer == 3:
            computer = "scissors"
            print("Computer chose scissors")

        #Outcome
        if player == "rock" and computer == "rock":
            print("Tie!")
            tie = tie + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "paper" and computer == "paper":
            print("Tie!")
            tie = tie + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "scissors" and computer == "scissors":
            print("Tie!")
            tie = tie + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "rock" and computer == "paper":
            print("Computer wins!")
            computer_score = computer_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "rock" and computer == "scissors":
            print("Player wins!")
            player_score = player_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "paper" and computer == "rock":
            print("Player wins!")
            player_score = player_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "paper" and computer == "scissors":
            print("Computer wins!")
            computer_score = computer_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "scissors" and computer == "rock":
            print("Computer wins!")
            computer_score = computer_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
        elif player == "scissors" and computer == "paper":
            print("Player wins!")
            player_score = player_score + 1
            print("Player score: " + str(player_score))
            print("Computer score: " + str(computer_score))
            print("Ties: " + str(tie))
            
        playagain = input("Would you like to play again?")
        if playagain == "yes":
            print(" ")
            print("Restarting...")
            print(" ")
        if playagain == "no":
            print("Thank you for playing!")
            break
#Main
rockpaperscissors()
