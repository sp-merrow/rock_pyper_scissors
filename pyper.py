from random import randint
from os import system, name
asciiArt = [[], [], []]
clear = lambda: system('cls' if name == 'nt' else 'clear') # OS-agnostic clear function

with open('ascii_assets.txt', 'r') as raw:
    count = -1
    for line in raw:
        line = line.replace('\n', '')
        if line.isalpha():
            count += 1
        else:
            asciiArt[count].append(line)

while True:
    clear()
    print('Options:\n\n1. Rock\n2. Paper\n3. Scissors')
    pick = input('\nEnter choice: ')
    while not pick.isdigit() or int(pick) not in range(1, 4):
        clear()
        print('Options:\n\n1. Rock\n2. Paper\n3. Scissors')
        pick = input('\nInvalid option.\nEnter choice: ')
    pick = int(pick) - 1

    compMove = randint(0, 2)

    clear()
    print('You picked:\n')
    for line in asciiArt[pick]:
        print(line)
    
    print('\nComputer picked:\n')
    for line in asciiArt[compMove]:
        print(line)
    
    if pick == compMove:
        print('\nDRAW!')
    elif pick == 0:
        if compMove == 1:
            print('\nYOU LOSE!')
        else:
            print('\nYOU WIN!')
    elif pick == 1:
        if compMove == 2:
            print('\nYOU LOSE!')
        else:
            print('\nYOU WIN!')
    elif pick == 2:
        if compMove == 0:
            print('\nYOU LOSE!')
        else:
            print('\nYOU WIN!')
    
    cont = input('\nPlay again? (y/n): ')
    if cont == 'n':
        break