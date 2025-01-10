#Jamie Huang
#Multiplication Quiz
#1/8/25

#Init
import random

#Functions

def multiplicationquiz():

    #Introduction to Program
    print("Welcome to the Multiplication Quiz!")
    print("How many questions would you like your quiz to be?")
    print(" ")

    #Customize Quiz Length
    questions = int(input("How many questions would you like your quiz to be?"))
    question = 0
    correct = 0

    #Loop
    for i in range(questions):
        question = question + 1
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        print("Question " + str(question) + " " + "out of " + str(questions))
        print("What is " + str(num1) + " times " + str(num2) + " ?")
        answer = int(input("What is " + str(num1) + " times " + str(num2) + " ?"))
    #Check Answer
        if answer == (num1 * num2):
            print("Correct!")
            print(" ")
            correct = correct + 1
        else:
            print("Incorrect!")
            print(" ")
    #End of Quiz
    print("You got " + str(correct) + " out of the " + str(questions) + " questions right!")
#Main
multiplicationquiz()
