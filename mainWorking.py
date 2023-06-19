#python3 -m pip install --upgrade termcolor
import sys, random, time
from termcolor import colored, cprint
from Inventory import *

pos = float(0)
tempOpt:list = []
tempPos:list = []
reqdItem:list = []
tempItem:list = []

wpm = 600 #wpm 85
def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def Interact(): #Balls

    for i in range(0, len(tempOpt)):
        print((i + 1), ")", tempOpt[i])

    while True:

        temp = input("⇥   ")

        if temp == "give items":
            #Inventory.inventory.append(Items.HouseKey)
            Inventory.inventory.append(Items.Beans)
            #Inventory.inventory.append(Items.Spoon)
            print("given items")

        if temp == "key":
            Inventory.inventory.append(Items.HouseKey)

        #print(*Inventory.inventory, sep = "\n")

        for item in Inventory.inventory:
            item:Item
            #print(str(item))
            for i in range(0, len(tempPos)): #Range of 0 to list
                #print(tempPos[i])
                if temp == str(i+1) and tempPos[i] != "null": #Compare if input is equal to list
                    #print(reqdItem[i])
                    if item.Check(reqdItem[i]) is True or reqdItem[i] == Items.Null:
                        pos = tempPos[i]
                        return pos
                
        if temp == "1": 
            Type("\nYou don't have the ")
            print(reqdItem)

        if temp == "2": 
            Type("\nYou don't have the ")
            print(reqdItem)
            
        if temp == "3": 
            Type("\nYou don't have the ")
            print(reqdItem)

        if temp == "4": 
            Type("\nYou don't have the ")
            print(reqdItem)


    while True:
        temp = input("\n⇥   ")

        if temp == "give items":
            Inventory.inventory.append(Items.Beans)

        for item in Inventory.inventory:
            item:Item

            for i in range(len(tempPos)):

                if item.Check(tempItem1) is True or tempItem1 == Items.Null:
                    if temp == i and tempPos1 != "null":
                        pos = tempPos1
                        print("i")

def pickUp():
    opt:list = []
    for i in range(0, len(tempOpt)):
        prb:list = []
        for item in Inventory.inventory:
            item:Item
            if item.Check(tempItem[i]) is True:
                prb.append(True)
        if not any(prb):
            opt.append(tempOpt[i])
    #print(len(opt))
    for num, letter in enumerate(opt):
        print(num + 1, ")", letter)

    temp = input("⇥   ")

    for i in range(0, len(opt)):
        if temp == str(i+(len(tempOpt))-(len(opt))) and tempItem[i+(len(tempOpt))-(len(opt))] != Items.Null:
            Inventory.inventory.append(tempItem[i])
            print(Inventory.inventory)

while True: #Start Game
    temp = input("start game? y/n: ").lower()

    if temp == "yes" or temp == "y":
        break
    elif temp == "no" or temp == "n":
        sys.exit("Ok then")
    Type("Um what?")

while True: #Pos 0

    if pos == 0: #Spawn
        Type("You find yourself on a rocky path in front of a slightly weathered, red bricked house\n")
        tempOpt = ["Walk inside", "Continue path left", "Continue path right"]
        tempPos = [1, 0.1, 0.2, "null"]
        reqdItem = [Items.HouseKey, Items.Null, Items.Null, Items.Null]
        pos = Interact()

    if True: #Inside house

        if pos == 1: #House Entrance
            Type("You find yourself in the entrance of the house\n")
            tempOpt = ["Head upstairs", "Head straight towards kitchen", "Turn right to the living room", "Exit the house"]
            tempPos = [1.2, 1.11, 1.12, 0]
            reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
            pos = Interact()
        if True: #Kitchen
            if pos == 1.11: #Kitchen
                Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. \n")
                tempOpt = ["Search cabinet", "Search drawer", "Turn right to the living room", "Return to entrance"]
                tempPos = [1.111, 1.112, 1.12, 1]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.111: #Kitchen cabinet
                Type("You open the cabinet. There is nothing.\n")
                tempOpt = ["Return"]
                tempPos = [1.11, "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.112: #Kitchen drawer 
                Type("You pull open the drawer and peer inside. \n")
                tempOpt = ["Take spoon", "Take canned beans", "Return"]
                tempItem = [Items.Spoon, Items.Beans, Items.Null, Items.Null]
                tempPos = ["null", "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pickUp()
                

        if True: #Living Room
            if pos == 1.12: #Living Room
                Type("The hard wood creaks below you as you enter the living room. \n")
                tempOpt = ["Look outside", "Go to kitchen", "Return to entrance"]
                tempPos = [1.121, 1.11, 1.12, "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.121: #Living Room Window
                Type("You aproach the window and look outside. It is dark. You see the faint outlines of trees\n")
                tempOpt = ["Return"]
                tempPos = [1.12, "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null]
                pos = Interact()