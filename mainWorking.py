#python3 -m pip install --upgrade termcolor
import sys, random, json, time
from termcolor import colored, cprint
from Inventory import *

class Scene:
    Room:str = "kitchen"
    Target:str = None


pos = float(0)

wpm = 85 #wpm
def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def qBasic(): #Basic Question(Movement)
    while True:
        temp = input("\n⇥   ")
        if temp == "1" and tempPos1 != 1989:
            pos = tempPos1
            return pos
        if temp == "2" and tempPos2 != 1989:
            pos = tempPos2
            return pos
        if temp == "3" and tempPos3 != 1989:
            pos = tempPos3
            return pos
        if temp == "4" and tempPos4 != 1989:
            pos = tempPos4
            return pos
        print("Invalid")

def Interact():
    while True:
        for item in Inventory.inventory:
                item:Item
                if item.Check(tempItem1) is False and tempItem1 != "null":
                    Inventory.inventory.append(tempItem1) 
                if item.Check(tempItem2) is False and tempItem2 != "null":
                    Inventory.inventory.append(tempItem2) 
                if item.Check(tempItem3) is False and tempItem3 != "null":
                    Inventory.inventory.append(tempItem3)
                if item.Check(tempItem4) is False and tempItem4 != "null":
                    Inventory.inventory.append(tempItem4)

Inventory.inventory.append(Items.Spoon)

def qInteract():
    while True:
        temp = input("\n⇥   ")
        for item in Inventory.inventory:
            item:Item
            if item.Check(tempItem1) is True or tempItem1 == Items.Null:
                if temp == "1" and tempPos1 != 1989:
                    pos = tempPos1
                    return pos

            if item.Check(tempItem2) is True or item.Check(Items.Null) is True:
                if temp == "2" and tempPos2 != 1989:
                    pos = tempPos2
                    return pos

            if item.Check(tempItem3) is True or item.Check(Items.Null) is True:
                if temp == "3" and tempPos3 != 1989:
                    pos = tempPos3
                    return pos
            
            if item.Check(tempItem4) is True or item.Check(Items.Null) is True:
                #Inventory.inventory.append(tempItem4)
                if temp == "4" and tempPos4 != 1989:
                    pos = tempPos4
                    return pos


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
        tempPos4 = 1989 #Does nothing
        tempItem1 = Items.Null #spoon
        tempItem2 = Items.Null #beans
        tempItem3 = Items.Null #Does nothing
        tempItem4 = Items.Null
        pos = qInteract()
    if pos == 1: #House Entrance
        Type("You find yourself in the entrance of the house")
        Type("\n1)Head upstairs\n2)Head straight towards kitchen\n3)Turn right to the living room\n4)Exit the house")
        tempPos1 = 1.2 #Head upstairs
        tempPos2 = 1.11 #Head towards kitchen
        tempPos3 = 1.12 #Turn right to living room
        tempPos4 = 0 #Exit house
        pos = qBasic()
    if True: #Kitchen
        if pos == 1.11: #Kitchen
            Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. ")
            Type("\n1)Search cabinet\n2)Search drawer\n3)Turn right to the living room\n4)Return to entrance")
            tempPos1 = 1.111 #Search cabinet
            tempPos2 = 1.112 #Seach drawer
            tempPos3 = 1.12 #Turn right to living room
            tempPos4 = 1 #Return to entrance
            pos = qBasic()
        if pos == 1.111: #Kitchen cabinet
            Type("You open the cabinet. There is nothing.")
            Type("\n1)Return")
            tempPos1 = 1.11 #Return to kitchen
            tempPos2 = 1989 #Does nothing
            tempPos3 = 1989 #Does nothing
            tempPos4 = 1989 #Does nothing
            pos = qBasic()
        if pos == 1.112: #Kitchen drawer  DOES NOT WORK
            Type("You pull open the drawer and peer inside.")
            #Type("\n1)Take", colored('spoon', 'red'), "\n2)Take", colored('canned beans', 'red'), "\n3)Return")
            temp = input("\n⇥   ")
            tempItem1 = Items.Spoon #spoon
            tempItem2 = Items.Beans #beans
            tempItem3 = "null" #Does nothing
            tempItem4 = "null"
            tempPos1 = 1989 #Does nothing
            pos == qInteract()
            

    #f True: #Living Room