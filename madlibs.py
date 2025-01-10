#Jamie Huang
#Madlibs Game
#12/10/24

#Init

#Function
def madlibs():
    print("Hello, welcome to MadLibs! Please input an answer to generate your story. Have fun!")
    adjective = input("Please enter an adjective: ")
    noun = input("Please enter a person (princess, cop, CEO, etc.): ")
    place = input("Please enter any place in the world: ")
    ppronoun = input("Please enter a pronoun (he/she/they): ")
    sound = input("Please enter a sound (boom, bang, pop, etc.): ")
    animal = input("Please enter an animal: ")
    object = input("Please enter an object: ")
    location = input("Please enter the name of any room in a house: ")
    verb = input("Please enter a verb in past tense: ")
    number = input("Please enter a number: ")
    print("Once upon a time, there was a" + " " + str(adjective) + " " + str(noun) + " " + "who lived in" + " " + str(place) + ".")
    print("One day," + " " + str(ppronoun) + " " + "heard a loud" + " " + str(sound) + ".")
    print("Turns out, the loud sound" + " " + str(ppronoun) + " " + "heard was made by a" + " " + str(animal) + " " + "in a" + " " + str(object) + " " + "in the" + " " + str(location) + ".")
    print("The" + " " + str(noun) + " " + str(verb) + " " + "the" + " " + str(animal) + " " + str(number) + " " + "times before the" + " " + str(animal) + " " + "left.")
    print("After that day, the" + " " + str(animal) + " " + "never came back again.")


#Main
madlibs()
