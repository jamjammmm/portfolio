#Jamie Huang
#Slot Machine
#1/28/25


#Init
import random
import time
symbols = ["7", "♥", "♦", "☆"]
credits = 500


#Functions

def intro():
    print("--------------------------------------------------------------------")
    print("Welcome to the 3-Slot Machine! Spin to win big!!!")
    print("Enter 'S' to spin and 'Q' to quit!")
    print("--------------------------------------------------------------------")


def userchoice():
    global credits, slot1, slot2, slot3
    while True:
        print("How much would you like to bet?")
        bet = 0
        bet = int(input("How much would you like to bet?"))
        if bet > credits:
            print("Insufficient credits.")
            bet = int(input("Please don't bet more than your balance. How much would you like to bet?"))
        elif bet < credits:
            user = input("Would you like to spin? (S/Q)")
        #User spins
            if user == "S":
                if credits <= 0:
                    print(" ")
                    print("Insufficient Credits.")
                    print("Would you like to buy more credits?")
                    choice = input("Would you like to buy more credits? (Y/N)")
                    if choice == "Y" or choice == "y":
                        print(" ")
                        print("Scanning card...")
                        time.sleep(2)
                        print(" ")
                        print("Successful transaction! -$200")
                        print("+300 credits added to your balance.")
                        credits += 1000
                    elif choice == "N" or choice == "n":
                        print("Insufficient credits. Please refill card and come back!")
                        break
                    else:
                        print("==============ERROR==============")
                        print("Invalid input. Please try again.")

            credits = credits - bet
            slot1 = random.choices(symbols, weights = [1, 3, 2, 4])[0]
            slot2 = random.choices(symbols, weights = [1, 3, 2, 4])[0]
            slot3 = random.choices(symbols, weights = [1, 3, 2, 4])[0]
            print(" ")
            print(" ")
            print("Remaining credits: " + str(credits))
            print(" ")
            print("Spinning...")
            time.sleep(2)
            print(" ")
            print(str("===|"), slot1, str(" "), slot2, str(" "), slot3, str("|==="))
            print(" ")
            outcomes()

        #User quits
        elif user == "Q":
            print(" ")
            print("Thank you for playing!")
            print("Shutting down...")
            print("Total credits: " + str(credits))
            break
        else:
            print(" ")
            print("============== ERROR ==============")
            print("Invalid input. Please try again.")

def outcomes():
    global credits, slot1, slot2, slot3
    if slot1 == "7" and slot2 == "7" and slot3 == "7":
        credits = credits + bet*5
        print("CONGRATULATIONS, YOU HIT THE JACKPOT !!!!!!!!!!!!!!!!!")
        print("+ " + credits  + " credits!")
        print(" ")
        print(" ")
    elif slot1 == "♥" and slot2 == "♥" and slot3 == "♥":
        credits = credits + bet*1.5
        print("You won!")
        print("+ " + credits  + " credits!")
        print(" ")
        print(" ")
    elif slot1 == "♦" and slot2 == "♦" and slot3 == "♦":
        credits == credits + bet*1.2
        print("You won!")
        print("+ " + credits  + " credits!")
        print(" ")
        print(" ")
    elif slot1 == "☆" and slot2 == "☆" and slot3 == "☆":
        credits == credits + bet*2
        print("You won!")
        print("+ " + credits  + " credits!")
        print(" ")
        print(" ")
    else:
        print("No match!")
        print(" ")
        print(" ")

def slotmachine():
    intro()
    userchoice()


#Main
slotmachine()
