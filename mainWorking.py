#python3 -m pip install --upgrade termcolor
import sys, random, time
from termcolor import colored, cprint
from Inventory import *

pos = float(0)
tempOpt:list = []
tempPos:list = []
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
                    #print(tempItem[i])
                    if item.Check(tempItem[i]) is True or tempItem[i] == Items.Null:
                        pos = tempPos[i]
                        return pos
                
        if temp == "1": 
            Type("\nYou don't have the ")
            print(tempItem)

        if temp == "2": 
            Type("\nYou don't have the ")
            print(tempItem)
            
        if temp == "3": 
            Type("\nYou don't have the ")
            print(tempItem)

        if temp == "4": 
            Type("\nYou don't have the ")
            print(tempItem)

def Interaction():
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
        tempItem = [Items.HouseKey, Items.Null, Items.Null, Items.Null]
        pos = Interact()

    if True: #Inside house

        if pos == 1: #House Entrance
            Type("You find yourself in the entrance of the house\n")
            tempOpt = ["Head upstairs", "Head straight towards kitchen", "Turn right to the living room", "Exit the house"]
            tempPos = [1.2, 1.11, 1.12, 0]
            tempItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
            pos = Interact()
        if True: #Kitchen
            if pos == 1.11: #Kitchen
                Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. \n")
                tempOpt = ["Search cabinet", "Search drawer", "Turn right to the living room", "Return to entrance"]
                tempPos = [1.111, 1.112, 1.12, 1]
                tempItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.111: #Kitchen cabinet
                Type("You open the cabinet. There is nothing.")
                tempOpt = ["Return"]
                tempPos = [1.11, "null", "null", "null"]
                tempItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.112: #Kitchen drawer  DOES NOT WORK
                Type("You pull open the drawer and peer inside. \n")
                #Type("\n1)Take", colored('spoon', 'red'), "\n2)Take", colored('canned beans', 'red'), "\n3)Return")
                temp = input("\n⇥   ")
                tempItem1 = Items.Spoon #spoon
                tempItem2 = Items.Beans #beans
                tempItem3 = "null" #Does nothing
                tempItem4 = "null"
                tempPos1 = "null" #Does nothing
                tempPos2 = "null" #Does nothing
                tempPos3 = "null" #Does nothing
                tempPos4 = "null" #Does nothing
                pos = Interact()
                

        if True: #Living Room
            if pos == 1.12: #Living Room
                Type("The hard wood creaks below you as you enter the living room. \n")
                tempOpt = ["Look outside", "Go to kitchen", "Return to entrance"]
                tempPos = [1.121, 1.11, 1.12, "null"]
                tempItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.121: #Living Room Window
                Type("You aproach the window and look outside. It is dark. You see the faint outlines of trees\n")
                tempOpt = ["Return"]
                tempPos = [1.12, "null", "null", "null"]
                tempItem = [Items.Null, Items.Null, Items.Null, Items.Null]
                pos = Interact()