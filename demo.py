from colorama import init, Fore, Back, deinit, Style
from random import randrange


fore_colors = [
    Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.LIGHTBLACK_EX,Fore.LIGHTBLUE_EX,Fore.MAGENTA,Fore.RED,Fore.WHITE
    ]
back_colors = [
    Back.BLUE,Back.CYAN,Back.GREEN,Back.LIGHTBLACK_EX,Back.LIGHTBLUE_EX,Back.MAGENTA,Back.RED,Back.WHITE
    ]

def gen_ran_col(color_list):
    return 
    return color_list[randrange(0,len(color_list))]

def ran_text():
    text = ""
    for i in range(1,randrange(1,28)):
        text += str(chr(randrange(0,26)+65))
    return text

init()

for i in range(1,randrange(1,2000)):
    print(gen_ran_col(back_colors) + gen_ran_col(fore_colors) + ran_text())

    print(Style.RESET_ALL)

deinit()
