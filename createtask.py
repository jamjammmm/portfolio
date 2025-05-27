#Emily Mei, Jamie Huang
#CREATE AP Task




#INITIALIZE



carList = ["AcuraADX" , "AcuraZDX" , "AlfaRomeoTonale" , "AudiA3" , "AudiA6E-Tron" ,
           "BMW3SeriesPlug-inHybrid" , "BMWX5Plug-inHybrid" , "ChevroletColorado" ,
           "ChevroletEquinox" , "ChevroletMalibu" , "ChryslerPacificaHybrid" ,
           "DodgeCharger" , "FordMaverick" , "GMCHummerEV" , "HondaAccordHybrid" ,
           "HyundaiElantraHybrid" , "HyundaiSantaCruz" , "HyundaiSonata" , "JeepCompass" ,
           "JeepWagoneerS" , "KiaEV3" , "KiaForte" , "LexusLC" , "LucidGravity" ,
           "MaseratiQuattroporte" , "MazdaCX-70Plug-inHybrid" , "Mercedez-BenzS-Class" ,
           "MitsubishiMirage" , "Porsche911" , "PorscheMacanElectric" , "RivianR1T" ,
           "RivianR2" , "ScoutTerra" , "SubaruCrosstrekHybrid" , "TeslaCybertruck" ,
           "TeslaModelX" , "ToyotaCamryHybrid" , "ToyotaCorollaHybrid" , "ToyotaSupra" ,
           "VolkswagenID7" , "Ram2500" , "NissanTitan" , "NissanFrontier" ,
           "Mercedez-BenzG-Class" , "Mercedez-BenzEQS" , "Mercedez-BenzEQSSUV" ,
           "JeepGladiator" , "HondaRidgeline" , "GMCYukon" , "GMCSierraUV" , "GMCCanyon" ,
           "FordRanger" , "FordMaverickHybrid" , "FordF-150Hybrid" ,
           "DodgeHornetPlug-inHybrid" , "FordEscapeHybrid" , "FordF-150Lightning" ,
           "FordMustangMach-E" ,"GenesisElectrifiedG80" , "LexusESHybrid"]

carPrice = [35000, 65000, 36000, 38000, 65900, 44550, 73800, 31900, 28600,
            24700, 42450, 57995, 26995, 96550, 33655, 25450, 28750, 26900,
            26900, 70200, 35000, 19990, 99750, 94900, 139000, 54400, 117750,
            16695, 120100, 75300, 69900, 45000, 59000, 23645, 79900, 84990,
            28400, 22325, 56250, 45000, 45565, 46690, 32050, 148250, 104400,
            105250, 38100, 40150, 67200, 97500, 38400, 33080, 26995, 37450,
            41400, 29150, 47780, 36495, 74875, 41020]

carSize = ["SUV", "SUV", "SUV", "Sedan", "Sedan", "Sedan", "SUV", "Truck", "SUV",
           "Sedan", "SUV", "Sedan", "Truck", "Truck", "Sedan", "Sedan", "Truck",
           "Sedan", "SUV", "SUV", "SUV", "Sedan", "Sedan", "Sedan", "Sedan", "SUV",
           "Sedan", "SUV", "Sedan", "SUV", "Truck", "Truck", "Truck", "SUV", "Truck",
           "SUV", "Sedan", "Sedan", "Sedan", "Sedan", "Truck", "Truck", "Truck", "SUV",
           "Sedan", "SUV", "Truck", "Truck", "Truck", "Truck", "Truck", "Truck",
           "Truck", "Truck", "SUV", "SUV", "Truck", "SUV", "Sedan", "Sedan"]

carType = ["Gas", "Electric", "Gas", "Gas", "Electric", "Hybrid", "Hybrid", "Gas",
           "Gas", "Gas", "Hybrid", "Electric", "Gas", "Electric", "Hybrid", "Hybrid",
           "Gas", "Gas", "Gas", "Electric", "Electric", "Gas", "Gas", "Electric", "Gas",
             "Hybrid", "Gas", "Gas", "Gas", "Electric", "Electric", "Electric", "Gas",
             "Hybrid", "Electric", "Electric", "Hybrid", "Hybrid", "Gas", "Electric",
             "Gas", "Gas", "Gas", "Gas", "Electric", "Electric", "Gas", "Gas", "Gas",
             "Electric", "Gas", "Gas", "Hybrid", "Hybrid", "Hybrid", "Hybrid", "Electric",
             "Electric", "Electric", "Hybrid"]
filterList = []




#FUNCTIONS



#This function asks for the user's budget and filters the cars that meet the budget
#into the filtered list.
def findBudget(min, max):
    for i in range(len(carPrice)):
        if carPrice[i] >= int(min) and carPrice[i] <= int(max):
            filterList.append(carList[i])


#This function takes the user's vehicle size preference and filters cars
#that are of said size into the filtered list.
def findSize(size):
    #Size 1 represents a sedan vehicle.
    if size == "1":
        for i in range(len(carSize)):
            if carSize[i] == "Sedan":
                filterList.append(carList[i])
    #Size 2 represents an SUV vehicle.
    elif size == "2":
        for i in range(len(carSize)):
            if carSize[i] == "SUV":
                if carSize[i] not in filterList:
                    filterList.append(carList[i])
    #Size 3 represents a truck vehicle.
    elif size == "3":
        for i in range(len(carSize)):
            if carSize[i] == "Truck":
                if carSize[i] not in filterList:
                    filterList.append(carList[i])


#This function takes the user's preferred fuel type and filters the cars with
#that preference into the filtered list.
def findType(type):
    #Type 1 represents a gas car.
    if type == "1":
        for i in range(len(carType)):
            if carType == "Gas":
                if carSize[i] not in filterList:
                    filterList.append(carType[i])
    #Type 2 represents a hybrid car.
    if type == "2":
        for i in range(len(carType)):
            if carType == "Hybrid":
                if carSize[i] not in filterList:
                    filterList.append(carType[i])
    #Type 3 represents an electric car.
    if type == "3":
        for i in range(len(carType)):
            if carType == "Electric":
                if carSize[i] not in filterList:
                    filterList.append(carType[i])


#A function that combines all of our code into a more user-friendly format.
def menu():
    print("Welcome to the Car Finder app!")
    print("""After a couple of questions, we'll help generate an INCLUSIVE
list of possible cars that fits at least one of your preferences.""")
    print("First, we'll need your budget to help you find your ideal car(s).")


    #Program asks user for their budget range.
    print("""
Please type in the MINIMUM amount in your budget you intend to spend IN NUMBERS ONLY:  """)
    min = input("Please type in the MINIMUM amount in your budget you intend to spend IN NUMBERS ONLY:  ")
    print("""
Please type in the MAXIMUM amount in your budget you intend to spend IN NUMBERS ONLY:  """)
    max = input("Please type in the MAXIMUM amount in your budget you intend to spend IN NUMBERS ONLY:  ")
    findBudget(min, max)


    #Program asks user what their ideal car size is.
    print("""
Please input the number that corresponds with your desired value.

What is your ideal car size?
1. Sedan
2. SUV
3. Truck
""")
    size = input("""
Please input the number that corresponds with your desired value.

What is your ideal car size?
1. Sedan
2. SUV
3. Truck
""")
    findSize(size)


    #Program asks user their preference on their vehicle's fuel type.
    print("""
Please input the number that corresponds with your desired value.

What is your ideal fuel type?
1. Gas
2. Hybrid
3. Electric
""")
    type = input("""Please input the number that corresponds with your desired value.
What is your ideal fuel type?
1. Gas
2. Hybrid
3. Electric
""")
    findType(type)

    #The program will print an INCLUSIVE list of all vehicles that match at
    #least one of the user's preferences. Users will find vehicles that may
    #be, for example, a car with their ideal fuel type but not size.
    print(filterList)



#MAIN

menu()
