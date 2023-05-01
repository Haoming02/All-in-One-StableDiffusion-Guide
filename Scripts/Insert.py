import sys
import os

FOLDER = sys.argv[1]
INSERT = sys.argv[2]

for FILE in os.listdir(FOLDER):
    if '.txt' not in FILE:
        continue

    with open(FOLDER + '/' + FILE, 'r') as f:
        lines = f.readlines()

    tags = [word.strip() for word in lines[0].split(',')]
    while '' in tags:
        tags.remove('')

    tags2 = [word.strip() for word in INSERT.split(',')]
    while '' in tags2:
        tags2.remove('')

    for tag in tags2:
        if tag in tags:
            tags.remove(tag)

    line = ', '.join(tags)
    IN = ', '.join(tags2)

    with open(FOLDER + '/' + FILE, 'w') as f:
        f.writelines(IN + ', ' + line)