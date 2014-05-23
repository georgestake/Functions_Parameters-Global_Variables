die roll program
#Describe the purpose of this program here.

import random,time
#dice face
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    roll = random.randint(1,6)#picks a random number from 1-6
    return roll
#displays the andom number in its dice form
def show_dice(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll ==4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)

def roll_dice():
    myroll = roll()
    time.sleep(1)
    show_dice(myroll)
def debug():#funtion for debuging
    while True:#for debugging purposes it infinetely repeats diferent random numbers so i could check if all numbers would be displayed
        myroll = roll()
        time.sleep(1)
        show_dice(myroll)#displays myroll
      
