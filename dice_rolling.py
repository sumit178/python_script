import random
import sys


while True:
    start = input("Enter 1 to start the game. \nEnter q to exit the game. \nCHOICE ==>  ")
    if start == str(1):
        print("\nyou have stated")
        number = random.randint(1,6)

        print("\n\nDice has come up with number :",number,"\n\n")
    elif start == "q" :
        print("\nyou have exited the game! ^_^")
        sys.exit()
    else:
        print("\nerror! you have enter wrong string")
        sys.exit()

