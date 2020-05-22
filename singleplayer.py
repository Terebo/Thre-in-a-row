import sys
import colorama
import random
##import mainmenu
A1, A2, A3, B1, B2, B3, C1, C2, C3 = "_", "_", "_", "_", "_", "_", "_", "_", "_"
bot = "O"
player = "X"
players = []
aic = []
empty = [['A','1'],['A','2'],['A','3'],['B','1'],['B','2'],['B','3'],['C','1'],['C','2'],['C','3']]

def picker(colour):
    picked = str(input("X or O ").upper())
    global player
    global bot
    if(picked != "X" and picked !=  "O"):
        picker("blue")
    if(picked == "X"):
        player = "X"
        bot = "O"
    if(picked == "O"):
        player = "O"
        bot = "X"
    print("it's\33[34m Blue's\33[0m turn!")
    person()

def person():
    inputt = input("A to C ").upper()
    inputt2 = int(input("1 to 3 "))
    if (inputt == "A" or inputt == "B" or inputt == "C"):
        if (inputt2 > 0 and inputt2 < 4):
            inputt = [inputt, str(inputt2)]
            draw(inputt, True)
        else:
            print("number from 1 to 3 expected, got: " + str(inputt2))
            person()
    else:
       print("letter from A to C expected, got: " + inputt)
       person()


def draw(cell, isperson):
    global empty, aic, players
    global A1, A2, A3, B1, B2, B3, C1, C2, C3
    selectedcell = ("".join(empty[empty.index(cell)]))
    if (isperson == True):
        empty.remove(cell)
        players.append(cell)
        exec(selectedcell + " = '" + "\33[34m" + str(player + "\33[0m" + "'"), globals())
        print(":)| 1 | 2 | 3 |")
        print("A | " + A1 + " | " + A2 + " | " + A3 + " |")
        print("B | " + B1 + " | " + B2 + " | " + B3 + " |")
        print("C | " + C1 + " | " + C2 + " | " + C3 + " |")
        if (len(empty) <= 0):
            print("it's a draw!")
            mainmenu()
        else:
            print("it's\033[1;32;40m greens's\33[0m turn!")
            ai()
    if (isperson == False):
        empty.remove(cell)
        aic.append(cell)
        exec(selectedcell + " = '" + "\033[1;32;40m" + str(bot + "\33[0m" + "'"), globals())
        print(":)| 1 | 2 | 3 |")
        print("A | " + A1 + " | " + A2 + " | " + A3 + " |")
        print("B | " + B1 + " | " + B2 + " | " + B3 + " |")
        print("C | " + C1 + " | " + C2 + " | " + C3 + " |")
        if (len(empty) <= 0):
            print("it's a draw!")
            mainmenu()
        else:
            print("it's\33[34m Blue's\33[0m turn!")
            person()
        
def ai():
    global empty, aic, players
    global A1, A2, A3, B1, B2, B3, C1, C2, C3
    letters = ["A", "B", "C"]
    randomcelllet = letters[random.randint(0,2)]
    randomcellnum = random.randint(1,3)
    cell = [randomcelllet, str(randomcellnum)]
    checker = cell in empty
    if(checker == False):
        ai()
    if(checker == True):
        draw(cell, False)

colorama.init()
print("\33[34mblue player \33[0mmay choose") 
picker("blue")


