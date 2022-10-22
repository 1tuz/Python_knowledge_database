from subprocess import run as sys
import re


def intro():
    print(50 * "*")
    print("Hello! This is my script for creating aliases!")
    print(50 * "*")
    print("Syntax : ealias <-key>")
    print(50 * "*")
    print("""Usage : \n -h - help\n -a - automatically makes alias from current path and filename\n -m - manually "
    makes alias(default)
    """)


q2 = input()

if "-a" in q2:
    print("Choosed '-a' flag! Alias will be created automatically from the filename and current directory")
    regular = re.findall(r'^\w+', q2)
    clear = regular[0]
    sys("DIR=$(pwd) && FOL=$(pwd | sed 's:.*/::') && echo $FOL=bash $DIR/", clear)
    quit()

elif "-h" in q2:
    intro()
    quit()
elif "-m" in q2:
    print("Choosed '-m' flag! Alias will be added manually after typing alias name and pipe...")
    read =
    sys("read -p 'Enter the new alias : ' new")
    sys("read -p 'Enter the pipe : ' old")
    sys("echo 'alias $new=\"$old\" >>~/.zshrc'")
    sys("'echo new alias was successfully added to .zshrc!' && zsh && source ~/.zshrc")
    quit()

else:
    print("No flags!Alias will be added manually after typing alias name and pipe...")
    read =
    sys("read -p 'Enter the new alias : ' new")
    sys("read -p 'Enter the pipe : ' old")
    sys("echo 'alias $new=\"$old\" >>~/.zshrc'")
    sys("'echo new alias was successfully added to .zshrc!' && zsh && source ~/.zshrc")
    quit()
