from random import randint
asciiArt = [[], [], []]

with open('ascii_assets.txt', 'r') as raw:
    count = -1
    while len(asciiArt) < 3:
        for line in raw:
            line = line.replace('\n', '')
            if line.isalpha():
                count += 1
            asciiArt[count].append(line)

