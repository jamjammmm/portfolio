#Jamie" , "Huang
#Dog" , "Breed" , "CREATE" , "Task
#2/27/25



#Initialize

dog_breeds = ["Affenpinscher" , "AfghanHound" , "AiredaleTerrier" , "AkbashDog" , "Akita" , "AlapahaBlueBloodBulldog" , "AlaskanHusky" , "AlaskanMalamute" , "AmericanEskimoDog" , "AmericanFoxhound" , "AmericanPitBullTerrier" , "AmericanWaterSpaniel" , "AnatolianShepherdDog" , "AustralianKelpie" , "AustralianShepherd" , "Azawakh" , "Basenji" , "BassetBleudeGascogne" , "Beagle" , "Beauceron" , "BedlingtonTerrier" , "BelgianMalinois" , "BelgianTervuren" , "BerneseMountainDog" , "BlackandTanCoonhound" , "Bloodhound" , "BluetickCoonhound" , "Boerboel" , "BorderTerrier" , "BostonTerrier" , "BouvierdesFlandres" , "Boxer" , "BoykinSpaniel" , "BraccoItaliano" , "Briard" , "Brittany" , "Bullmastiff" , "CairnTerrier" , "CaneCorso" , "CardiganWelshCorgi" , "CatahoulaLeopardDog" , "CaucasianShepherd(Ovcharka)" , "CavalierKingCharlesSpaniel" , "ChineseCrested" , "Chinook" , "ChowChow" , "ClumberSpaniel" , "CockerSpaniel(American)" , "CotondeTulear" , "Dalmatian" , "DogoArgentino" , "EnglishShepherd" , "EnglishSpringerSpaniel" , "Eurasier" , "FieldSpaniel" , "FinnishLapphund" , "GermanPinscher" , "GermanShepherdDog" , "GermanShorthairedPointer" , "GiantSchnauzer" , "GlenofImaalTerrier" , "GoldenRetriever" , "GordonSetter" , "GreatDane" , "GreatPyrenees" , "Greyhound" , "Harrier" , "Havanese" , "IrishSetter" , "IrishWolfhound" , "ItalianGreyhound" , "JapaneseChin" , "Keeshond" , "Komondor" , "Kuvasz" , "LabradorRetriever" , "LagottoRomagnolo" , "Leonberger" , "LhasaApso" , "Maltese" , "MiniatureSchnauzer" , "Newfoundland" , "NorfolkTerrier" , "Papillon" , "PembrokeWelshCorgi" , "PharaohHound" , "Plott" , "Pug" , "RedboneCoonhound" , "RhodesianRidgeback" , "Rottweiler" , "Samoyed" , "Schipperke" , "ScottishDeerhound" , "ShihTzu" , "SilkyTerrier" , "SoftCoatedWheatenTerrier" , "SpanishWaterDog" , "Vizsla" , "Weimaraner"]
dog_weights = [ 6  ,  50  ,  40  ,  90  ,  65  ,  55  ,  38  ,  65  ,  20  ,  65  ,  30  ,  25  ,  80  ,  31  ,  35  ,  33  ,  22  ,  35  ,  20  ,  80  ,  17  ,  40  ,  40  ,  65  ,  65  ,  80  ,  45  ,  110  ,  12  ,  10  ,  70  ,  50  ,  25  ,  55  ,  70  ,  30  ,  100  ,  13  ,  88  ,  25  ,  50  ,  80  ,  13  ,  10  ,  50  ,  40  ,  55  ,  20  ,  9  ,  50  ,  80  ,  44  ,  35  ,  40  ,  35  ,  33  ,  25  ,  50  ,  45  ,  65  ,  32  ,  55  ,  45  ,  110  ,  85  ,  50  ,  40  ,  7  ,  35  ,  105  ,  7  ,  4  ,  35  ,  80  ,  70  ,  55  ,  24  ,  120  ,  12  ,  4  ,  11  ,  100  ,  11  ,  3  ,  25  ,  40  ,  40  ,  14  ,  45  ,  75  ,  75  ,  50  ,  10  ,  70  ,  9  ,  8  ,  30  ,  30  ,  50  ,  55 ]
filtered_list = []
dog_temperaments = ["Stubborn,Curious,Playful,Adventurous,Active,Fun-loving" , "Aloof,Clownish,Dignified,Independent,Happy" , "Outgoing,Friendly,Alert,Confident,Intelligent,Courageous" , "Loyal,Independent,Intelligent,Brave" , "Docile,Alert,Responsive,Dignified,Composed,Friendly,Receptive,Faithful,Courageous" , "Loving,Protective,Trainable,Dutiful,Responsible" , "Friendly,Energetic,Loyal,Gentle,Confident" , "Friendly,Affectionate,Devoted,Loyal,Dignified,Playful" , "Friendly,Alert,Reserved,Intelligent,Protective" , "Kind,Sweet-Tempered,Loyal,Independent,Intelligent,Loving" , "StrongWilled,Stubborn,Friendly,Clownish,Affectionate,Loyal,Obedient,Intelligent,Courageous" , "Friendly,Energetic,Obedient,Intelligent,Protective,Trainable" , "Steady,Bold,Independent,Confident,Intelligent,Proud" , "Friendly,Energetic,Alert,Loyal,Intelligent,Eager" , "Good-natured,Affectionate,Intelligent,Active,Protective" , "Aloof,Affectionate,Attentive,Rugged,Fierce,Refined" , "Affectionate,Energetic,Alert,Curious,Playful,Intelligent" , "Affectionate,Lively,Agile,Curious,Happy,Active" , "Amiable,EvenTempered,Excitable,Determined,Gentle,Intelligent" , "Fearless,Friendly,Intelligent,Protective,Calm" , "Affectionate,Spirited,Intelligent,Good-tempered" , "Watchful,Alert,Stubborn,Friendly,Confident,Hard-working,Active,Protective" , "Energetic,Alert,Loyal,Intelligent,Attentive,Protective" , "Affectionate,Loyal,Intelligent,Faithful" , "Easygoing,Gentle,Adaptable,Trusting,EvenTempered,Lovable" , "Stubborn,Affectionate,Gentle,EvenTempered" , "Friendly,Intelligent,Active" , "Obedient,Confident,Intelligent,Dominant,Territorial" , "Fearless,Affectionate,Alert,Obedient,Intelligent,EvenTempered" , "Friendly,Lively,Intelligent" , "Protective,Loyal,Gentle,Intelligent,Familial,Rational" , "Devoted,Fearless,Friendly,Cheerful,Energetic,Loyal,Playful,Confident,Intelligent,Bright,Brave,Calm" , "Friendly,Energetic,Companionable,Intelligent,Eager,Trainable" , "Stubborn,Affectionate,Loyal,Playful,Companionable,Trainable" , "Fearless,Loyal,Obedient,Intelligent,Faithful,Protective" , "Agile,Adaptable,Quick,Intelligent,Attentive,Happy" , "Docile,Reliable,Devoted,Alert,Loyal,Reserved,Loving,Protective,Powerful,Calm,Courageous" , "Hardy,Fearless,Assertive,Gay,Intelligent,Active" , "Trainable,Reserved,Stable,Quiet,EvenTempered,Calm" , "Affectionate,Devoted,Alert,Companionable,Intelligent,Active" , "Energetic,Inquisitive,Independent,Gentle,Intelligent,Loving" , "Alert,Quick,Dominant,Powerful,Calm,Strong" , "Fearless,Affectionate,Sociable,Patient,Playful,Adaptable" , "Affectionate,Sweet-Tempered,Lively,Alert,Playful,Happy" , "Friendly,Alert,Dignified,Intelligent,Calm" , "Aloof,Loyal,Independent,Quiet" , "Affectionate,Loyal,Dignified,Gentle,Calm,Great-hearted" , "Outgoing,Sociable,Trusting,Joyful,EvenTempered,Merry" , "Affectionate,Lively,Playful,Intelligent,Trainable,Vocal" , "Outgoing,Friendly,Energetic,Playful,Sensitive,Intelligent,Active" , "Friendly,Affectionate,Cheerful,Loyal,Tolerant,Protective" , "Kind,Energetic,Independent,Adaptable,Intelligent,Bossy" , "Affectionate,Cheerful,Alert,Intelligent,Attentive,Active" , "Alert,Reserved,Intelligent,EvenTempered,Watchful,Calm" , "Docile,Cautious,Sociable,Sensitive,Adaptable,Familial" , "Friendly,Keen,Faithful,Calm,Courageous" , "Spirited,Lively,Intelligent,Loving,EvenTempered,Familial"]
dog_images = ["https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg" , "https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg" , "https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg" , "https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/36TXlWMDf.jpg" , "https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg" , "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg" , "https://cdn2.thedogapi.com/images/GhtSdrW29.jpg" , "https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg" , "https://cdn2.thedogapi.com/images/uISezUGDV.jpg" , "https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png" , "https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg" , "https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg" , "https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg" , "https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg" , "https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg" , "https://cdn2.thedogapi.com/images/HJAFgxcNQ_1280.jpg" , "https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg" , "https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg" , "https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg" , "https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg" , "https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg" , "https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg" , "https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg" , "https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg" , "https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg" , "https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg" , "https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg" , "https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg" , "https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg" , "https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg" , "https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg" , "https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg" , "https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg" , "https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg" , "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg" , "https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png" , "https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg" , "https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg" , "https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg" , "https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg" , "https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg" , "https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg" , "https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg" , "https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg" , "https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg" , "https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg" , "https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg" , "https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg" , "https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg" , "https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg" , "https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg" , "https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg" , "https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg" , "https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg" , "https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg" , "https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg" , "https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg" , "https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg" , "https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg" , "https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg" , "https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg" , "https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg" , "https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"]
dog_purpose = ["Smallrodenthunting,lapdog", "Coursingandhunting", "Badger,otterhunting", "Sheepguarding", "Huntingbears", "Guarding", "Sledpulling", "Haulingheavyfreight,Sledpulling", "Circusperformer", "Foxhunting,scenthound", "Fighting", "Birdflushingandretrieving", "Livestockherding", "Farmdog,Cattleherding", "Sheepherding", "Livestockguardian,hunting", "Hunting", "Huntingonfoot.", "Rabbit,harehunting", "Boarherding,hunting,guarding", "Killingrat,badger,othervermin", "Stockherding", "Guarding,Drafting,Policework.", "Draftwork", "Huntingraccoons,nighthunting", "Trailing", "Huntingwithasuperiorsenseofsmell.", "Guardingthehomestead,farmwork.", "Foxbolting,ratting", "Ratting,Companionship", "Cattleherding", "Bull-baiting,guardian", "Turkeyretrieving", "Versatilegundog", "Herding,guardingsheep", "Pointing,retrieving", "Estateguardian", "Boltingofotter,foxes,othervermin", "Companion,guarddog,andhunter", "Cattledroving", "Drivinglivestock", "Guarddogs,defendingsheepfrompredators,mainlywolves,jackalsandbears", "Flushingsmallbirds,companion", "Ratting,lapdog,curio", "Sledpulling", "Guardian,cartpulling,hunting", "Birdflushing,retrieving", "HuntingtheAmericanwoodcock", "Accompanyingladiesonlongseavoyages,rattersonboardship.", "Carriagedog-trotalongsidecarriagestoprotecttheoccupantsfrombanditryorotherinterference", "Big-gamehunting", "Herding&guardinglivestock,farmwatchdog", "Birdflushing,retrieving", "Companionship", "Birdflushing,retrieving", "Herdingreindeer", "Watchdog,Huntingverminonthefarm.", "Herding,Guarddog", "Generalhunting", "Herding,guarding", "Ridthehomeandfarmofvermin,andhuntbadgerandfox", "Retrieving", "Findandpointgamebirds", "Hunting&holdingboars,Guardian", "Sheepguardian", "Coursinghares", "Huntingharesbytrailingthem", "Companionship", "Birdsetting,retrieving", "Coursingwolves,elk", "Lapdog", "Lapdog", "Bargewatchdog", "Sheepguardian", "Guardian,huntinglargegame", "Waterretrieving", "WaterretrievaldoginthemarshesofRomagna", "Guardian,appearance.", "Guardinginsidethehome,companion", "Lapdog", "Ratting", "Allpurposewaterdog,fishingaid", "Ratting,foxbolting", "Lapdog", "DrivingstocktomarketinnorthernWales", "Huntingrabbits", "Huntingbig-gamelikeBoar.", "Lapdog", "Huntingraccoon,deer,bear,andcougar.", "Biggamehunting,guarding", "Cattledrover,guardian,draft", "Herdingreindeer,guardian,draft", "Bargewatchdog", "Coursingdeer", "Lapdog", "Smallverminhunting,companionship", "Verminhunting,guarding,all-aroundfarmhelper", "Herdingflocksofsheepandgoatsfromonepasturetoanother", "Pointingandtrailing", "Largegametrailingandversatilegundog"]
dog_purpose = [item.lower() for item in dog_purpose]
import random
from PIL import Image
import requests
from io import BytesIO



#Functions

def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#Filtering dog sizes
def dog_size():
    x = input("What size dog are you looking for? (tiny, small, medium, large)")

    #User inputs tiny size
    if x == "tiny":
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 10:
                filtered_list.append(dog_breeds[i])
        y = random.choice(filtered_list)
        print("Recommended dog breed: " + y)

    #User inputs small size
    if x == "small":
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 30 and dog_weights[i] > 10:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        y = random.choice(filtered_list)
        print("Recommended dog breed: " + y)

    #User inputs medium size
    if x == "medium":
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 50 and dog_weights[i] > 30:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        y = random.choice(filtered_list)
        print("Recommended dog breed: " + y)

    #User inputs large size
    if x == "large":
        for i in range(len(dog_weights)):
            if dog_weights[i] <= 100 and dog_weights[i] > 50:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        y = random.choice(filtered_list)
        print("Recommended dog breed: " + y)


#User is able to learn about the temperament of the dog + see a picture of it
def doginfo():
    breed = input("What kind of dog would you like to research about?")
    if breed not in dog_breeds:
        print("ERROR: Dog breed not found.")
    x = dog_breeds.index(breed)
    print(dog_temperaments[x])
    y = dog_images[x]
    open_image(y)


#User is able to receive dog breeds for their desired purpose
def dogpurpose():
    purpose = input("What type of dog would you like? (Ex: companion, sled, hunt, farm, etc)")
    purpose = purpose.lower()
    if purpose not in dog_purpose:
        print("ERROR: Dog type not found.")
    else:
        for i in range(len(dog_purpose)):
            if purpose in dog_purpose[i]:
                filtered_list.append(dog_breeds[i])
        print(filtered_list)
        print("Recommended breed: " + random.choice(filtered_list))

#App Menu
def doginfomenu():
    print("Welcome to the Dog Breed Info App! Please select a number.")
    while True: #Keep the app running until the player wants to quit
        print("""

    ============== MENU ==============
    1. Find Breed Based On Size/Weight
    2. Learn About Temperament Of Specific Dog
    3. Find Breed Based On Purpose
    4. View Dog Breed List
    5. Quit
    ==================================
              """)
        x = input("What would you like to do?")
        if x == "1":
            print("""
                    """)
            dog_size()

        if x == "2":
            print("""
                    """)
            doginfo()

        if x == "3":
            print("""
                    """)
            dogpurpose()

        if x == "4":
            print("""
                  """)
            print(dog_breeds)

        if x == "5":
            print("""
                    """)
            print("Thank you for using the Dog Info App! Closing now.")
            break



#Main
doginfomenu()
