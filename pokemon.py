#Jamie Huang
#Pokemon Evolution


#Init

pokemon_level = 0
pokemon_name = ("Squirtle")
day = 0


#Functions

def train():
    print(pokemon_name + " did 50 pushups and 25 jumping jacks. He is now level " + str(pokemon_level + 1))

def gymbattle():
    print(pokemon_name + " beat the Gym Leader after 6 hours! He is now level " + str(pokemon_level + 2))

def rest():
    print("")
    print("STATS")
    print("")
    print("Pokemon: " + pokemon_name)
    print("Level: " + str(pokemon_level))
    if pokemon_level < 5:
        print("""
        ⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜
        ⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜
        ⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦⬛
        ⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🏿⬛⬛⬜⬛🟦🟦🟦⬛🟦🟦⬛
        ⬛🟫🟦🟦🟦🟦🟦🟦🟦🟦🏿🟫🏿⬛🟦🟦🟦⬛🟦🟦🟦⬛
        ⬛🟦🟦🟦🟦⬜⬛🟦🟦🟦🏽🟫🟫🏿⬛🟦🟦⬛🟦🟦⬛⬜
        ⬛🟦🟦🟦🟦⬛🟫🟦🟦🟦⬜🟫🟫🟫⬛🟦⬛⬛⬛⬛⬜⬜
        ⬜⬛🟦🟦🟦⬛🟫🟦🟦🟦⬛⬜⬜🟫🟫⬛⬛⬜⬜⬜⬜⬜
        ⬜⬜⬛⬛🟦🟦🟦🟦⬛⬛🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬛🟦⬛⬛⬛⬛🟦🟦🟦🟦⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛⬛🟨🟨⬛🟦🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛🟨🟨⬛⬛⬛⬛🏽🟫🟫⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛🟦⬛🟫🟨🟨🟨🟫⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛⬛🟫🟫🟦⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟦⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
    if pokemon_level >= 5 and pokemon_level < 10:
        print("""
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
        ⬜⬜⬛⬜⬜⬛⬛⬛⬛⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜
        ⬜⬜⬜⬛🟦🟦🟦🟦🟪🟪⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜
        ⬜⬜⬛🟪🟦🟦🟦🟦🟦◼️⬜⬛⬜⬛⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜
        ⬜⬜⬛🟦🟦🟦🟦🟦🟦◼️⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜
        ⬜⬛🟦🟦🟦🟦🟦🟦⬛🟪⬛⬜⬜⬛🟨⬛⬜⬛⬜⬜⬛⬛⬜⬛⬜⬜
        ⬜⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦⬛⬛🟫🟨🟫⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
        ⬜⬜⬛🟦🟦🟦⬛⬛⬜⬜🟦⬛⬜⬜🟫🟨⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜
        ⬜⬜⬛🟦🟦🟦🟦🟫⬜🟦🟪⬛⬛⬜🟫🟨🟨⬛⬜⬜⬜⬛⬜⬜⬜⬜
        ⬜⬛🟦⬛🟦🟪🟦🟦🟦⬛⬛🟦🟦⬛⬜🟫🟫⬛⬜⬜⬜⬛⬜⬜⬜⬜
        ⬜⬛⬜🟦⬛⬛⬛⬛⬛🟨⬛🟦🟦🟦⬜🟫🟨⬛⬜⬜⬛⬜⬜⬜⬜⬜
        ⬜⬜⬛⬛⬜⬛⬜🟨🟨⬛⬜🟦🟦⬛⬜🟫🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛🟨🟨⬛🟦⬜⬛⬛⬜🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛🟦⬛⬛🟨⬛⬛🟨⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛🟦🟦⬛⬛🟨🟨⬛🟦⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟪🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")
    if pokemon_level >= 10:
        print("""
        ⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬜🏽🏽⬛⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛⬛⬜⬛⬜🟫🟫🟫🟫⬛⬛⬛🏽🏽⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬛🟦⬛⬛🟫🟫🟫🟫🟫🟫⬛⬜⬛⬛🏽⬛⬜⬜⬜⬜
        ⬜⬜⬜⬛🟦🟦🟦⬛⬛🟫⬛⬛🟫⬜⬜⬛⬛🏽⬛⬜⬜⬜⬜
        ⬜⬜⬛🟦🟦🟦🟦🟦🟦⬛🟦⬛🟫⬜🏽🏽🏽⬛⬜⬜⬜⬜⬜
        ⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟫🟫🏽🏽⬛🟫⬛⬜⬜⬜⬜
        ⬜⬛🟦🟦🟦🟦🟦⬛🟦🟦⬛🏽🏽🏽⬛⬛🟫🟫⬛⬜⬜⬜⬜
        ⬛🟦🟦🟦🟦🟦⬛⬜🟦🟦🟦⬛⬛⬛⬛⬛🏽🟫🟫⬛⬛⬛⬛
        ⬛🟦🟦🟦🟦⬛⬛🟦🟦🟨🟦⬛⬛🟦🟦🟦⬛🏽🟫⬛🟦🟦⬛
        ⬛⬜🟦🟦🟦🟦🟦🟦🟨🟨⬛🏽⬛🟦🟦🟦⬛🏽🟫⬛🟦⬛⬜
        ⬜⬛🟨🟨🟦🟦🟨🟨🟨⬛🏽⬛🟦🟦🟦🟦⬛🏽🏽⬛⬛⬜⬜
        ⬜⬜⬛⬛⬜🟨🟨⬛⬛🟨⬛🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛⬛🟦🟦⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜
        ⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨⬛⬜⬛⬛⬛⬛🟦🟦🟦⬛⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨⬛🟨⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜🟦🟦⬜⬛⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
        ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜""")


#Main

while True:
    day = day + 1
    print("Welcome to Pokemon Evolution! Day: " + str(day))
    print("Select an activity for the day.")
    print("""
    1. Train
    2. Gym Battle
    3. Rest (Display info)
    4. Quit Game""")
    activity = int(input("Activity: "))
    if pokemon_level >= 5 and pokemon_level < 10:
        pokemon_name = "Wartortle"
    if pokemon_level >= 10:
        pokemon_name = "Blastoise"
    if activity == 1:
        train()
        pokemon_level = pokemon_level + 1
    if activity == 2:
        gymbattle()
        pokemon_level = pokemon_level + 2
    if activity == 3:
        rest()
    if activity == 4:
        break
