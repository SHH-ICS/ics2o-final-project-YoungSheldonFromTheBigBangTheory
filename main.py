#python3 -m pip install --upgrade termcolor
import math, sys, random, json, time
from termcolor import colored, cprint

pos = float(0)

wpm = 85 #wpm
def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def qBasic():
    #while True:
    while True:
        temp = input("\n⇥   ")
        if tempPos4 != 1989:
            match temp:
                case "1":
                    pos = tempPos1
                    return pos
                case "2":
                    pos = tempPos2
                    return pos
                case "3":
                    pos = tempPos3
                    return pos    
                case "4":
                    pos = tempPos4
                    return pos
                case _:
                    print("\nInvalid")
        if tempPos4 == 1989:
            match temp:
                case "1":
                    pos = tempPos1
                    return pos
                case "2":
                    pos = tempPos2
                    return pos
                case "3":
                    pos = tempPos3
                    return pos    
                case _:
                    print("\nInvalid")

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
        pos = qBasic()
    if pos == 1: #House Entrance
        Type("You find yourself in the entrance of the house")
        Type("\n1)Head upstairs\n2)Head straight towards kitchen\n3)Turn right to the living room\n4)Exit the house")
        tempPos1 = 1.2 #Head upstairs
        tempPos2 = 1.11 #Head towards kitchen
        tempPos3 = 1.12 #Turn right to living room
        tempPos4 = 0 #Exit house
        pos = qBasic()
    if pos == 1.11: #Kitchen
        Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. ")
        Type("\n1)Search cabinet\n2)Search drawer\n3)Turn right to the living room\n4)Return to entrance")
        tempPos1 = 1.111 #Search cabinet
        tempPos2 = 1.112 #Seach drawer
        tempPos3 = 1.12 #Turn right to living room
        tempPos4 = 1 #Return to entrance
        pos = qBasic()
    if pos == 1.12: #Living Room
        Type("The hard wood creaks below you as you enter the living room. You aproach the window and look outside. It is dark.")
        Type("\n1)Look outside\n2)Go to kitchen\n3)Return to entrance")
        tempPos1 = 1.21 #Look outside
        tempPos2 = 1.11 #Go to kitchen
        tempPos3 = 1.12 #Return to entrance
        tempPos4 = 1989 #Does nothing
        pos = qBasic()