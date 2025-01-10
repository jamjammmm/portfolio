#Jamie Huang
#10/17/24
#Name Generator Project

#Initialize

#Functions

#Artist Generator
def artistgen():
    
    #Introduction to Program
    print("Welcome to Your Artist Generator!")
    print("Please answer each prompt to generate an artist that best suits your musical preference.")
    ans = input("Which genre do you like more? Pop or nonpop?")

    #Person chooses "pop" genre
    if ans == "pop":
        ans = input("What type of music do you prefer? Party or sentimental?")
        if ans == "party":
            ans = input("Do you like karaoke or dance?")
            if ans == "karaoke":
                print("Your artist is Taylor Swift!")
            else:
                print("Your artist is The Weeknd!")
        else:
            ans = input("Would you rather listen to emotional or meaningful music?")
            if ans == "emotional":
                print("Your artist is Bruno Mars!")
            else:
                print("Your artist is Charlie Puth!")

    #Person chooses "nonpop" genre
    else:
        ans = input("Would you rather listen to indie or rock?")
        if ans == "indie":
            ans = input("Do you like upbeat or slow music?")
            if ans == "upbeat indie":
                print("Your artist is Ricky Montgomery!")
            else:
                print("Your artist is Cigarettes After Sex!")
        else:
            ans = input("Do you prefer alternative rock or pure rock?")
            if ans == "alternative rock":
                print("Your artist is Arctic Monkeys!")
            else:
                print("Your artist is Queen!")

#Main
artistgen()
