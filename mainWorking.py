#python3 -m pip install --upgrade termcolor
import sys, random, time
from termcolor import colored, cprint
from Inventory import *

class Scene:
    Room:str = "kitchen"
    Target:str = None


pos = float(0)

wpm = 600 #wpm 85
def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def Interact(): #Balls
    while True:
        temp = input("\n⇥   ")

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
            
            if temp == "1" and tempPos1 != "null":
                if item.Check(tempItem1) is True or tempItem1 == Items.Null:
                    pos = tempPos1
                    return pos

            if item.Check(tempItem2) is True or tempItem2 == Items.Null: 
                if temp == "2" and tempPos2 != "null":
                    pos = tempPos2
                    return pos

            if item.Check(tempItem3) is True or tempItem3 == Items.Null: 
                if temp == "3" and tempPos3 != "null":
                    pos = tempPos3
                    return pos
            
            if item.Check(tempItem4) is True or tempItem4 == Items.Null: 
                #Inventory.inventory.append(tempItem4)
                if temp == "4" and tempPos4 != "null":
                    pos = tempPos4
                    return pos
                
        if temp == "1": 
            Type("\nYou don't have the ")
            print(tempItem1)

        if temp == "2": 
            Type("\nYou don't have the ")
            print(tempItem2)
            
        if temp == "3": 
            Type("\nYou don't have the ")
            print(tempItem3)

        if temp == "4": 
            Type("\nYou don't have the ")
            print(tempItem4)

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
        Type("You find yourself on a rocky path in front of a slightly weathered, red bricked house")
        Type("\n1)Walk inside\n2)Continue path left\n3)Continue path right")
        tempPos1 = 1 #Walk inside
        tempPos2 = 0.1 #Continue path left
        tempPos3 = 0.2 #Continue path right
        tempPos4 = "null" #Does nothing
        tempPos:list = [1, 0.1, 0.2, "null"]
        tempItem1 = Items.HouseKey
        tempItem2 = tempItem3 = tempItem4 = Items.Null 
        pos = Interact()
    if pos == 1: #House Entrance
        Type("You find yourself in the entrance of the house")
        Type("\n1)Head upstairs\n2)Head straight towards kitchen\n3)Turn right to the living room\n4)Exit the house")
        tempPos1 = 1.2 #Head upstairs
        tempPos2 = 1.11 #Head towards kitchen
        tempPos3 = 1.12 #Turn right to living room
        tempPos4 = 0 #Exit house
        tempItem1 = tempItem2 = tempItem3 = tempItem4 = Items.Null 
        pos = Interact()
    if True: #Kitchen
        if pos == 1.11: #Kitchen
            Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. ")
            Type("\n1)Search cabinet\n2)Search drawer\n3)Turn right to the living room\n4)Return to entrance")
            tempPos1 = 1.111 #Search cabinet
            tempPos2 = 1.112 #Seach drawer
            tempPos3 = 1.12 #Turn right to living room
            tempPos4 = 1 #Return to entrance
            tempItem1 = tempItem2 = tempItem3 = tempItem4 = Items.Null 
            pos = Interact()
        if pos == 1.111: #Kitchen cabinet
            Type("You open the cabinet. There is nothing.")
            Type("\n1)Return")
            tempPos1 = 1.11 #Return to kitchen
            tempPos2 = "null" #Does nothing
            tempPos3 = "null" #Does nothing
            tempPos4 = "null" #Does nothing
            tempItem1 = tempItem2 = tempItem3 = tempItem4 = Items.Null 
            pos = Interact()
        if pos == 1.112: #Kitchen drawer  DOES NOT WORK
            Type("You pull open the drawer and peer inside.")
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
            Type("The hard wood creaks below you as you enter the living room.")
            Type("\n1)Look outside\n2)Go to kitchen\n3)Return to entrance")
            tempPos1 = 1.121 #Look outside
            tempPos2 = 1.11 #Go to kitchen
            tempPos3 = 1.12 #Return to entrance
            tempPos4 = "null" #Does nothing
            tempItem1 = tempItem2 = tempItem3 = tempItem4 = Items.Null 
            pos = Interact()
        if pos == 1.121: #Living Room Window
            Type("You aproach the window and look outside. It is dark. You see the faint outlines of trees")
            Type("\n1)Return")
            tempPos1 = 1.12 #Look outside
            tempPos2 = "null" #Does nothing
            tempPos3 = "null" #Does nothing
            tempPos4 = "null" #Does nothing
            tempItem1 = tempItem2 = tempItem3 = tempItem4 = Items.Null 
            pos = Interact()