#!/bin/env python3
# gengen.py >generate.sh

from l9config import v1Configuration

print(f'#!/bin/bash\n')
print(f'echo "+++ Level 9 game analysis +++"')
for game in v1Configuration.keys():
    if v1Configuration[game]["version"] == 1:
        filename = v1Configuration[game]["script"].replace('test-scripts/', 'roms/').replace('.txt', '.dat')
        v1Configuration[game]["filename"] = filename
    print(f'echo "*** {game} ***"')
    if ((v1Configuration[game]["version"] != 3 and not "timemagik" in game) or
       not "parts" in v1Configuration[game] or len(v1Configuration[game]["parts"]) > 3):
        filename = v1Configuration[game]["filename"].replace('roms/', 'game-text/').replace('.dat', '-dict.txt')
        print(f'python3 level9.py -g {game} -d >{filename}')
        filename = v1Configuration[game]["filename"].replace('roms/', 'game-text/').replace('.dat', '-descs.txt')
        print(f'python3 level9.py -g {game} -m >{filename}')
        filename = v1Configuration[game]["filename"].replace('roms/', 'exits/').replace('.dat', '-exits.txt')
        print(f'python3 level9.py -g {game} -e >{filename}')
        filename = v1Configuration[game]["filename"].replace('roms/', 'decompilation/').replace('.dat', '.txt')
        print(f'python3 decompiler.py -g {game} >{filename}')
    if "script" in v1Configuration[game]:
        filename = v1Configuration[game]["script"].replace('test-scripts/', 'full-game-text/').replace('.dat', '.txt')
        print(f'python3 level9.py -g {game} -a >{filename}')
print(f'rm -f parser.log')
print(f'echo "+++ Level 9 picture decompilation +++"')
print(f'python3 l9pic.py | gzip -9 -c >pics/decompiled.txt.gz')
print(f'python3 l9bitmap.py')
