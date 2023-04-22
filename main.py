# Color Classifier Main Loop
# Created by Konrad Ceglarski 2019
__author__ = "Konrad Ceglarski"

import pygame, random, os, math, classifier, sys

# Language
os.system('title Color Classifier')
os.system('cls')
with open("inuse.lang") as f:
    lang_path = f.readlines()[0]
try:
    with open(lang_path) as f:
        lang = f.readlines()
    for index, content in enumerate(lang):
        lang[index] = content.replace('\n','')
except:
    os.system('echo \033[91mAn Error has occured.\033[0m')
    print("Try changing 'inuse.lang' file content to: 'lang/eng.lang'.")
    os.system('pause')
    print('\nGoing toward an Exit . . .')
    exit()
else:
    pass

pygame.init()

# Introduction - Welcome Text
os.system(f'title {lang[0]}')
os.system('cls')
print(f"{lang[0]}\n{lang[1]} Konrad Ceglarski\n")
os.system('echo \033[31m█▓▒░\033[91m█▓▒░\033[93m█▓▒░\033[0m')
print()
os.system('pause')
print()

# Pygame Setup
w, h = (350, 500)
window = pygame.display.set_mode([w, h])
pygame.display.set_caption(f"{lang[0]}")
clock = pygame.time.Clock()
running = True

# Functions
def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_color():
    pygame.draw.rect(window, [r,g,b], [25,25,w-50,w-50])

def type_rgb():
    font = pygame.font.SysFont("Arial", 24)
    text = f'[{r}, {g}, {b}]'
    label = font.render(text, 1, [255,255,255])
    textrect = label.get_rect()
    textrect.midtop = (w/2, 0.75*h+36)
    window.blit(label, textrect)

def type_prediction(r, g, b):
    font = pygame.font.SysFont("Arial Black", 24)
    prediction = len(lang) - (13 - classifier.predict_color(r, g, b)[0])
    sure = classifier.predict_color(r, g, b)[1]
    text = f'{lang[prediction]} ({sure}%)'
    print(f'{lang[2]} [{r}, {g}, {b}].\n{lang[4]} {lang[prediction]}.\n{lang[5]} - {sure}%.\n')
    label = font.render(text, 1, [255,255,255])
    textrect = label.get_rect()
    textrect.midtop = (w/2, 0.75*h)
    window.blit(label, textrect)

def main_job():
    global r, g, b
    window.fill([50,50,50])
    r, g, b = pick_color()
    draw_color()
    type_rgb()
    type_prediction(r, g, b)

# CLI Argument Managment
args = sys.argv[1:]
try:
    global r, g, b
    r, g, b = None, None, None
    if len(args) > 0:
        arg = ''.join(args)
        if len(arg) > 6 and arg.count(',') == 2:
            if (arg[0] == '[' and arg[-1] == ']') or (arg[0] == '(' and arg[-1] == ')'):
                arg = arg[1:-1]
                r, g, b = arg.replace(' ','').split(',')
                r, g, b = int(r), int(g), int(b)
except:
    pass

if None not in (r, g, b) and min(r, g, b) >= 0 and max(r, g, b) <= 255:
    window.fill([50,50,50])
    draw_color()
    type_rgb()
    type_prediction(r, g, b)
else:
    main_job()

# Main Loop
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key != pygame.K_ESCAPE):
            main_job()

    pygame.display.flip()        
    clock.tick(60)

# Exit
print(f'{lang[3]} . . .')
pygame.quit()