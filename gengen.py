# python3 gengen.py >generate.sh

from l9config import v1Configuration

print(f'#!/bin/bash\n')
for game in v1Configuration.keys():
    if v1Configuration[game]["version"] < 2: continue
    print(f'echo "*** {game} ***"')
    filename = v1Configuration[game]["filename"].replace('roms/', 'game-text/').replace('.dat', '-dict.txt')
    print(f'python3 level9.py -g {game} -d >{filename}')
    filename = v1Configuration[game]["filename"].replace('roms/', 'game-text/').replace('.dat', '-descs.txt')
    print(f'python3 level9.py -g {game} -m >{filename}')
    filename = v1Configuration[game]["filename"].replace('roms/', 'exits/').replace('.dat', '-exits.txt')
    print(f'python3 level9.py -g {game} -e >{filename}')
    filename = v1Configuration[game]["filename"].replace('roms/', 'decompilation/').replace('.dat', '.txt')
    print(f'python3 decompiler.py -g {game} >{filename}')
    filename = v1Configuration[game]["filename"].replace('roms/', 'full-game-text/').replace('.dat', '.txt')
    if game[-2] != 'p':
        print(f'python3 level9.py -g {game} -a >{filename}')
