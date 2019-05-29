# rock paper scissor game

from random import randint

while True:
    user = input("rock:r paper:p scissor:s\n enter your choice:")

    comp = randint(1, 3)

    if comp == 1:
        comp = 'r'
    elif comp == 2:
        comp = 'p'
    else:
        comp = 's'


    if user == "r" or user == "p" or user == "s":
        print("computer randomly chose: %s" % comp)

        if user == "r" and comp == "s" or user == "s" and comp == "p" or user == "p" and comp == "r":
            print("you win!!!")
        elif user == "s" and comp == "r" or user == "p" and comp == "s" or user == "r" and comp == "p":
            print("computer wins!!!")
        else:
            print(" ohh, a draw!")
    else:
        print("***enter valid choice***")

