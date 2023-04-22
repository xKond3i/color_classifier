# Color Classifier Main Loop
# Created by Konrad Ceglarski 2019
__author__ = "Konrad Ceglarski"

import os, random

commands = ["help","exit","run","lang","data","coin"]
desc = ["prints a list of commands","closes the CLI (this window)","opens an Color Classifier instance - start color arg with [r,g,b] format","changes the language of Color Classifier - language arg with str format","displays the learning data","little game choosing randomly a 1 or a 0."]

os.system('title Color Classifier CLI')

# Functions
def main():
    os.system('cls')
    cmd = input('Color Classifier\nCommand Line Interface\nCreated by Konrad Ceglarski\n\nEnglish Only\n\n')
    cmd = cmd.split()
    os.system('cls')
    print('Color Classifier\nCommand Line Interface\nCreated by Konrad Ceglarski\n\nEnglish Only\n')
    if cmd[0] in commands:
        for x in commands:
            if cmd[0] == x:
                print(f"Executing the '{x}' command . . .")
                if len(cmd) == 1:
                    globals()[f"{x}_func"]()
                else:
                    globals()[f"{x}_func"](cmd[1], cmd[1:])
    else:
        os.system('echo \033[91mAn Error has occured.\033[0m')
        print(f"It looks like we don't have the '{cmd[0]}' command.")
    os.system('pause')

    main()

def help_func(*args, **kwargs):
    print("All the CLI Commands:")
    for index, cmd in enumerate(commands):
        print(f" • {cmd:<8} - {desc[index]}")

def exit_func(*args, **kwargs):
    print('Going toward an Exit . . .')
    exit()

def run_func(*args, **kwargs):
    if len(args) > 0:
        os.system(f"main.py {''.join(args[1])}")
    else:
        # os.startfile("main.py")
        os.system("main.py")

def lang_func(lang = "none", *args, **kwargs):
    langs = os.listdir("./lang")
    for index, item in enumerate(langs):
        langs[index] = item.replace(".lang", "")

    if lang == "none":
        # os.system('echo \033[91mAn Error has occured.\033[0m')
        # print("Missing language argument.")
        with open("inuse.lang", "r") as f:
            os.system(f"echo The actual language is: \033[93m{f.readlines()[0][5:].replace('.lang', '')}\033[0m.")
            print("Language can be change by the same command with language as an argument.\nLanguages available:")
            for item in langs:
                print(f" • {item}")
    elif lang in langs:
        with open("inuse.lang", "r") as f:
            current = f.readlines()[0][5:-5]
        if lang == current:
            os.system(f"echo The language of the Color Classifier is already set to: \033[93m{lang}\033[0m.")
        else:
            with open("inuse.lang", "w") as f:
                f.write(f"lang/{lang}.lang")
            os.system(f"echo The language of the Color Classifier has been successfully changed to: \033[93m{lang}\033[0m.")
            print("To see the difference You have to restart all of the Color Classifier instances.")
    else:
        os.system('echo \033[91mAn Error has occured.\033[0m')
        print(f"It looks like we don't have the '{lang}' language.")

def coin_func(*args, **kwargs):
    coin = random.randrange(0, 2)
    os.system(f'echo  ► It came out to be \033[93m{coin}\033[0m.')

def data_func(*args, **kwargs):
    with open('example_colors.csv', "r") as f:
        content = f.readlines()

    for line in content:
        column = line.replace('\n', '').split(',')
        print(f"{column[0]:<4} {column[1]:<4} {column[2]:<4} {column[3]:}")

main()