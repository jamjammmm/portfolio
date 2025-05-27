#Jamie Huang
#Magic 8 Ball
#1/24/25

#Init
import random
import time
magic_list = ["Yes", "Without a doubt", "Definitely", "Perhaps", "Most likely", "Sure", "Maybe", "Ask again later", "Unsure", "Cannot predict now", "No", "Not looking good", "Probably not", "My sources say no", "Better to give up now", "Your luck says no", "Your luck says yes", "Reply hazy", "Signs point to yes", "Signs point to no", "You may rely on it", "Depends on the situation", "Focus and ask again", "Ask someone else", "It's looking like a yes", "It's looking like a no"]

#Function
def magic8ball():

    #Introduction to the program
    print("Welcome to the Magic 8 Ball! Enter a question and receive an answer.")

    #Loop allows the user to continue playing without running program again
    while True:
        print(" ")
        print("Ask the Magic 8 Ball a yes or no question!")
        user = input("Ask the Magic 8 Ball a yes or no question!")
        x = user.endswith("?")

    #Checking to see if user input is valid
        if x:
            print(" ")
            print("Shake...")
            time.sleep(2)
            print(" ")
            print(random.choice(magic_list))
            print(" ")

        else:
            print(" ")
            print("ERROR: Please reenter the question and use a question mark (?).")
            print(" ")

    #Asking the user if they'd like to play again
        print("Would you like to ask another question?")
        user = input("Would you like to ask another question?")
        if user == "yes" or user == "y":
            print(" ")
            print("Waking Magic 8 Ball up...")
            print(" ")
        elif user == "no" or user == "n":
            print(" ")
            print("Thank you for playing!")
            print("Going to sleep...")
            break


#Main
magic8ball()
