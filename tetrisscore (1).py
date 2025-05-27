#Jamie Huang
#Tetris Score Analysis
#2/7/25

#Init
scores = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]


#Function
def maxscore():
    highestscore = 0
    for highpoint in scores:
        if highpoint > highestscore:
            highestscore = highpoint
    print("Highest score: " + str(highestscore) + " points")
    return highestscore


def minscore():
    lowscore = 0
    for i in range(len(scores)):
        lowscore = scores[i]
        if lowscore < scores[i]:
            lowscore = scores[i]
    return lowscore

def averagescore():
    total = 0
    average = 0
    for i in range(len(scores)):
        total = scores[i] + total
        average = total/100
    return("The average score is: " + str(average) + " points.")


def newscore():
    x = input("Please enter a new Tetris score: ")

    if int(x) > maxscore():
        print("CONGRATULATIONS ON A NEW HIGH SCORE!!!")
        scores.append(x)
        scores.remove(minsore())
    else:
        print("Unfortunately, your score does not beat any of the top 100 scores. Keep playing!")

#Main
newscore()
