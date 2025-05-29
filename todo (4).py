#Jamie Huang
#Artists To Listen To
#1/22/25


#Initialize


#Functions

def todolist():
    artistList = []
    print("Welcome to The Artist List Organizer!")
    print(" ")
    while True:
        try:
            print("Select an option by entering a number: \n1. View Current List \n2. Add Item To List \n3. Remove Item From List \n4. Sort List Alphabetically \n5. Count + Print Number of Items In List \n6. Exit Program")
            print("----------------------------------------------------------------------------------")
            choice = int(input("Select an option by entering a number: "))

            if choice == 1:
                print(" ")
                print("Here is your artist list: ")
                print(" ")
                print(artistList)
            elif choice == 2:
                print(" ")
                print("What artist would you like to add?")
                ans = input("What artist would you like to add?")
                artistList.append(ans)
                print(" ")
                print("Successfully added!")
            elif choice == 3:
                print(" ")
                print("What artist would you like to remove?")
                ans = input("What artist would you like to remove?")
                artistList.remove(ans)
                print("Successfully removed!")
            elif choice == 4:
                artistList.sort()
                print(" ")
                print("Printing...")
                print(" ")
                print(artistList)
            elif choice == 5:
                print(" ")
                x = len(artistList)
                print("There are " + str(x) + " artist(s) in your list.")
            elif choice == 6:
                print(" ")
                print("Thank you for using The Artist List Organizer! Closing...")
                break
        except:
            print("ERROR: Please enter a NUMBER.")

#Main
todolist()
