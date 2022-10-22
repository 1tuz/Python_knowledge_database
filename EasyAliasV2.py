from os import system as sys
import re


print(50 * "*")
print("Hello! This is my test script")
print(50 * "*")


def intro():
    print("Syntax : ealias <-key>")
    print(50 * "*")
    print("""Usage : \n -h - help\n -a - automatically makes alias from current path and filename\n -m - manually "
    makes alias(default)
    """)


intro()

loop = True
while loop:

    q1 = input("Do you want to continue? y/n : ")
    if q1 == "y":
        q2 = input("Okay, type filename and flag... \n")

        if "-a" in q2:
            print("Choosed '-a' flag! Alias will be created automatically from the filename and current directory")
            regular = re.findall(r'^\w+', q2)
            clear = regular[0]
            sys("DIR=$(pwd) && FOL=$(pwd | sed 's:.*/::') && echo $FOL=bash $DIR/", clear)
            q1

        elif "-h" in q2:
            intro()
        else:
            print("No flags!")
            break
    elif q1 == "n":
        print("bye")
        break
    else:
        print("Bad option!")
        intro()
        q1
