#!/bin/bash

echo "+++ Level 9 game analysis +++"
echo "*** adventure ***"
python3 level9.py -g adventure -d >game-text/adventure-quest-v1-dict.txt
python3 level9.py -g adventure -m >game-text/adventure-quest-v1-descs.txt
python3 level9.py -g adventure -e >exits/adventure-quest-v1-exits.txt
python3 decompiler.py -g adventure >decompilation/adventure-quest-v1.txt
python3 level9.py -g adventure -a >full-game-text/adventure-quest-v1.txt
echo "*** adventurev2 ***"
python3 level9.py -g adventurev2 -d >game-text/adventure-quest-v2-dict.txt
python3 level9.py -g adventurev2 -m >game-text/adventure-quest-v2-descs.txt
python3 level9.py -g adventurev2 -e >exits/adventure-quest-v2-exits.txt
python3 decompiler.py -g adventurev2 >decompilation/adventure-quest-v2.txt
python3 level9.py -g adventurev2 -a >full-game-text/adventure-quest-v2.txt
echo "*** adventurev3 ***"
python3 level9.py -g adventurev3 -d >game-text/adventure-quest-v3-dict.txt
python3 level9.py -g adventurev3 -m >game-text/adventure-quest-v3-descs.txt
python3 level9.py -g adventurev3 -e >exits/adventure-quest-v3-exits.txt
python3 decompiler.py -g adventurev3 >decompilation/adventure-quest-v3.txt
python3 level9.py -g adventurev3 -a >full-game-text/adventure-quest-v3.txt
echo "*** colossal ***"
python3 level9.py -g colossal -d >game-text/colossal-adventure-v1-dict.txt
python3 level9.py -g colossal -m >game-text/colossal-adventure-v1-descs.txt
python3 level9.py -g colossal -e >exits/colossal-adventure-v1-exits.txt
python3 decompiler.py -g colossal >decompilation/colossal-adventure-v1.txt
python3 level9.py -g colossal -a >full-game-text/colossal-adventure-v1.txt
echo "*** colossalv2 ***"
python3 level9.py -g colossalv2 -d >game-text/colossal-adventure-v2-dict.txt
python3 level9.py -g colossalv2 -m >game-text/colossal-adventure-v2-descs.txt
python3 level9.py -g colossalv2 -e >exits/colossal-adventure-v2-exits.txt
python3 decompiler.py -g colossalv2 >decompilation/colossal-adventure-v2.txt
python3 level9.py -g colossalv2 -a >full-game-text/colossal-adventure-v2.txt
echo "*** colossalv3 ***"
python3 level9.py -g colossalv3 -d >game-text/colossal-adventure-v3-dict.txt
python3 level9.py -g colossalv3 -m >game-text/colossal-adventure-v3-descs.txt
python3 level9.py -g colossalv3 -e >exits/colossal-adventure-v3-exits.txt
python3 decompiler.py -g colossalv3 >decompilation/colossal-adventure-v3.txt
python3 level9.py -g colossalv3 -a >full-game-text/colossal-adventure-v3.txt
echo "*** dungeon ***"
python3 level9.py -g dungeon -d >game-text/dungeon-adventure-v1-dict.txt
python3 level9.py -g dungeon -m >game-text/dungeon-adventure-v1-descs.txt
python3 level9.py -g dungeon -e >exits/dungeon-adventure-v1-exits.txt
python3 decompiler.py -g dungeon >decompilation/dungeon-adventure-v1.txt
python3 level9.py -g dungeon -a >full-game-text/dungeon-adventure-v1.txt
echo "*** dungeonv2 ***"
python3 level9.py -g dungeonv2 -d >game-text/dungeon-adventure-v2-dict.txt
python3 level9.py -g dungeonv2 -m >game-text/dungeon-adventure-v2-descs.txt
python3 level9.py -g dungeonv2 -e >exits/dungeon-adventure-v2-exits.txt
python3 decompiler.py -g dungeonv2 >decompilation/dungeon-adventure-v2.txt
python3 level9.py -g dungeonv2 -a >full-game-text/dungeon-adventure-v2.txt
echo "*** dungeonv3 ***"
python3 level9.py -g dungeonv3 -d >game-text/dungeon-adventure-v3-dict.txt
python3 level9.py -g dungeonv3 -m >game-text/dungeon-adventure-v3-descs.txt
python3 level9.py -g dungeonv3 -e >exits/dungeon-adventure-v3-exits.txt
python3 decompiler.py -g dungeonv3 >decompilation/dungeon-adventure-v3.txt
python3 level9.py -g dungeonv3 -a >full-game-text/dungeon-adventure-v3.txt
echo "*** eden ***"
python3 level9.py -g eden -d >game-text/return-to-eden-v2-dict.txt
python3 level9.py -g eden -m >game-text/return-to-eden-v2-descs.txt
python3 level9.py -g eden -e >exits/return-to-eden-v2-exits.txt
python3 decompiler.py -g eden >decompilation/return-to-eden-v2.txt
python3 level9.py -g eden -a >full-game-text/return-to-eden-v2.txt
echo "*** edenv3 ***"
python3 level9.py -g edenv3 -d >game-text/return-to-eden-v3-dict.txt
python3 level9.py -g edenv3 -m >game-text/return-to-eden-v3-descs.txt
python3 level9.py -g edenv3 -e >exits/return-to-eden-v3-exits.txt
python3 decompiler.py -g edenv3 >decompilation/return-to-eden-v3.txt
python3 level9.py -g edenv3 -a >full-game-text/return-to-eden-v3.txt
echo "*** erik ***"
python3 level9.py -g erik -d >game-text/erik-the-viking-v2-dict.txt
python3 level9.py -g erik -m >game-text/erik-the-viking-v2-descs.txt
python3 level9.py -g erik -e >exits/erik-the-viking-v2-exits.txt
python3 decompiler.py -g erik >decompilation/erik-the-viking-v2.txt
python3 level9.py -g erik -a >full-game-text/erik-the-viking-v2.txt
echo "*** gnome ***"
python3 level9.py -g gnome -d >game-text/gnome-ranger-v4-1-dict.txt
python3 level9.py -g gnome -m >game-text/gnome-ranger-v4-1-descs.txt
python3 level9.py -g gnome -e >exits/gnome-ranger-v4-1-exits.txt
python3 decompiler.py -g gnome >decompilation/gnome-ranger-v4-1.txt
python3 level9.py -g gnome -a >full-game-text/gnome-ranger-v4-1.txt
echo "*** gnomep2 ***"
python3 level9.py -g gnomep2 -d >game-text/gnome-ranger-v4-2-dict.txt
python3 level9.py -g gnomep2 -m >game-text/gnome-ranger-v4-2-descs.txt
python3 level9.py -g gnomep2 -e >exits/gnome-ranger-v4-2-exits.txt
python3 decompiler.py -g gnomep2 >decompilation/gnome-ranger-v4-2.txt
echo "*** gnomep3 ***"
python3 level9.py -g gnomep3 -d >game-text/gnome-ranger-v4-3-dict.txt
python3 level9.py -g gnomep3 -m >game-text/gnome-ranger-v4-3-descs.txt
python3 level9.py -g gnomep3 -e >exits/gnome-ranger-v4-3-exits.txt
python3 decompiler.py -g gnomep3 >decompilation/gnome-ranger-v4-3.txt
echo "*** ingrid ***"
python3 level9.py -g ingrid -d >game-text/ingrids-back-v4-1-dict.txt
python3 level9.py -g ingrid -m >game-text/ingrids-back-v4-1-descs.txt
python3 level9.py -g ingrid -e >exits/ingrids-back-v4-1-exits.txt
python3 decompiler.py -g ingrid >decompilation/ingrids-back-v4-1.txt
python3 level9.py -g ingrid -a >full-game-text/ingrids-back-v4-1.txt
echo "*** ingridp2 ***"
python3 level9.py -g ingridp2 -d >game-text/ingrids-back-v4-2-dict.txt
python3 level9.py -g ingridp2 -m >game-text/ingrids-back-v4-2-descs.txt
python3 level9.py -g ingridp2 -e >exits/ingrids-back-v4-2-exits.txt
python3 decompiler.py -g ingridp2 >decompilation/ingrids-back-v4-2.txt
echo "*** ingridp3 ***"
python3 level9.py -g ingridp3 -d >game-text/ingrids-back-v4-3-dict.txt
python3 level9.py -g ingridp3 -m >game-text/ingrids-back-v4-3-descs.txt
python3 level9.py -g ingridp3 -e >exits/ingrids-back-v4-3-exits.txt
python3 decompiler.py -g ingridp3 >decompilation/ingrids-back-v4-3.txt
echo "*** isle ***"
python3 level9.py -g isle -d >game-text/emerald-isle-v2-dict.txt
python3 level9.py -g isle -m >game-text/emerald-isle-v2-descs.txt
python3 level9.py -g isle -e >exits/emerald-isle-v2-exits.txt
python3 decompiler.py -g isle >decompilation/emerald-isle-v2.txt
python3 level9.py -g isle -a >full-game-text/emerald-isle-v2.txt
echo "*** lancelot ***"
python3 level9.py -g lancelot -d >game-text/lancelot-v4-1-dict.txt
python3 level9.py -g lancelot -m >game-text/lancelot-v4-1-descs.txt
python3 level9.py -g lancelot -e >exits/lancelot-v4-1-exits.txt
python3 decompiler.py -g lancelot >decompilation/lancelot-v4-1.txt
python3 level9.py -g lancelot -a >full-game-text/lancelot-v4-1.txt
echo "*** lancelotp2 ***"
python3 level9.py -g lancelotp2 -d >game-text/lancelot-v4-2-dict.txt
python3 level9.py -g lancelotp2 -m >game-text/lancelot-v4-2-descs.txt
python3 level9.py -g lancelotp2 -e >exits/lancelot-v4-2-exits.txt
python3 decompiler.py -g lancelotp2 >decompilation/lancelot-v4-2.txt
echo "*** lancelotp3 ***"
python3 level9.py -g lancelotp3 -d >game-text/lancelot-v4-3-dict.txt
python3 level9.py -g lancelotp3 -m >game-text/lancelot-v4-3-descs.txt
python3 level9.py -g lancelotp3 -e >exits/lancelot-v4-3-exits.txt
python3 decompiler.py -g lancelotp3 >decompilation/lancelot-v4-3.txt
echo "*** lords ***"
python3 level9.py -g lords -d >game-text/lords-of-time-v1-dict.txt
python3 level9.py -g lords -m >game-text/lords-of-time-v1-descs.txt
python3 level9.py -g lords -e >exits/lords-of-time-v1-exits.txt
python3 decompiler.py -g lords >decompilation/lords-of-time-v1.txt
python3 level9.py -g lords -a >full-game-text/lords-of-time-v1.txt
echo "*** lordsv2 ***"
python3 level9.py -g lordsv2 -d >game-text/lords-of-time-v2-dict.txt
python3 level9.py -g lordsv2 -m >game-text/lords-of-time-v2-descs.txt
python3 level9.py -g lordsv2 -e >exits/lords-of-time-v2-exits.txt
python3 decompiler.py -g lordsv2 >decompilation/lords-of-time-v2.txt
python3 level9.py -g lordsv2 -a >full-game-text/lords-of-time-v2.txt
echo "*** lordsv4 ***"
python3 level9.py -g lordsv4 -d >game-text/lords-of-time-v4-dict.txt
python3 level9.py -g lordsv4 -m >game-text/lords-of-time-v4-descs.txt
python3 level9.py -g lordsv4 -e >exits/lords-of-time-v4-exits.txt
python3 decompiler.py -g lordsv4 >decompilation/lords-of-time-v4.txt
python3 level9.py -g lordsv4 -a >full-game-text/lords-of-time-v4.txt
echo "*** magik ***"
python3 level9.py -g magik -d >game-text/price-of-magik-v3-dict.txt
python3 level9.py -g magik -m >game-text/price-of-magik-v3-descs.txt
python3 level9.py -g magik -e >exits/price-of-magik-v3-exits.txt
python3 decompiler.py -g magik >decompilation/price-of-magik-v3.txt
python3 level9.py -g magik -a >full-game-text/price-of-magik-v3.txt
echo "*** magikv4 ***"
python3 level9.py -g magikv4 -d >game-text/price-of-magik-v4-dict.txt
python3 level9.py -g magikv4 -m >game-text/price-of-magik-v4-descs.txt
python3 level9.py -g magikv4 -e >exits/price-of-magik-v4-exits.txt
python3 decompiler.py -g magikv4 >decompilation/price-of-magik-v4.txt
python3 level9.py -g magikv4 -a >full-game-text/price-of-magik-v4.txt
echo "*** orc ***"
python3 level9.py -g orc -d >game-text/knight-orc-v4-1-dict.txt
python3 level9.py -g orc -m >game-text/knight-orc-v4-1-descs.txt
python3 level9.py -g orc -e >exits/knight-orc-v4-1-exits.txt
python3 decompiler.py -g orc >decompilation/knight-orc-v4-1.txt
python3 level9.py -g orc -a >full-game-text/knight-orc-v4-1.txt
echo "*** orcp2 ***"
python3 level9.py -g orcp2 -d >game-text/knight-orc-v4-2-dict.txt
python3 level9.py -g orcp2 -m >game-text/knight-orc-v4-2-descs.txt
python3 level9.py -g orcp2 -e >exits/knight-orc-v4-2-exits.txt
python3 decompiler.py -g orcp2 >decompilation/knight-orc-v4-2.txt
echo "*** orcp3 ***"
python3 level9.py -g orcp3 -d >game-text/knight-orc-v4-3-dict.txt
python3 level9.py -g orcp3 -m >game-text/knight-orc-v4-3-descs.txt
python3 level9.py -g orcp3 -e >exits/knight-orc-v4-3-exits.txt
python3 decompiler.py -g orcp3 >decompilation/knight-orc-v4-3.txt
echo "*** redmoon ***"
python3 level9.py -g redmoon -d >game-text/red-moon-v2-dict.txt
python3 level9.py -g redmoon -m >game-text/red-moon-v2-descs.txt
python3 level9.py -g redmoon -e >exits/red-moon-v2-exits.txt
python3 decompiler.py -g redmoon >decompilation/red-moon-v2.txt
python3 level9.py -g redmoon -a >full-game-text/red-moon-v2.txt
echo "*** redmoonv4 ***"
python3 level9.py -g redmoonv4 -d >game-text/red-moon-v4-dict.txt
python3 level9.py -g redmoonv4 -m >game-text/red-moon-v4-descs.txt
python3 level9.py -g redmoonv4 -e >exits/red-moon-v4-exits.txt
python3 decompiler.py -g redmoonv4 >decompilation/red-moon-v4.txt
python3 level9.py -g redmoonv4 -a >full-game-text/red-moon-v4.txt
echo "*** scapeghost ***"
python3 level9.py -g scapeghost -d >game-text/scapeghost-v4-1-dict.txt
python3 level9.py -g scapeghost -m >game-text/scapeghost-v4-1-descs.txt
python3 level9.py -g scapeghost -e >exits/scapeghost-v4-1-exits.txt
python3 decompiler.py -g scapeghost >decompilation/scapeghost-v4-1.txt
python3 level9.py -g scapeghost -a >full-game-text/scapeghost-v4-1.txt
echo "*** scapeghostp2 ***"
python3 level9.py -g scapeghostp2 -d >game-text/scapeghost-v4-2-dict.txt
python3 level9.py -g scapeghostp2 -m >game-text/scapeghost-v4-2-descs.txt
python3 level9.py -g scapeghostp2 -e >exits/scapeghost-v4-2-exits.txt
python3 decompiler.py -g scapeghostp2 >decompilation/scapeghost-v4-2.txt
echo "*** scapeghostp3 ***"
python3 level9.py -g scapeghostp3 -d >game-text/scapeghost-v4-3-dict.txt
python3 level9.py -g scapeghostp3 -m >game-text/scapeghost-v4-3-descs.txt
python3 level9.py -g scapeghostp3 -e >exits/scapeghost-v4-3-exits.txt
python3 decompiler.py -g scapeghostp3 >decompilation/scapeghost-v4-3.txt
echo "*** snowball ***"
python3 level9.py -g snowball -d >game-text/snowball-v1-dict.txt
python3 level9.py -g snowball -m >game-text/snowball-v1-descs.txt
python3 level9.py -g snowball -e >exits/snowball-v1-exits.txt
python3 decompiler.py -g snowball >decompilation/snowball-v1.txt
python3 level9.py -g snowball -a >full-game-text/snowball-v1.txt
echo "*** snowballv2 ***"
python3 level9.py -g snowballv2 -d >game-text/snowball-v2-dict.txt
python3 level9.py -g snowballv2 -m >game-text/snowball-v2-descs.txt
python3 level9.py -g snowballv2 -e >exits/snowball-v2-exits.txt
python3 decompiler.py -g snowballv2 >decompilation/snowball-v2.txt
python3 level9.py -g snowballv2 -a >full-game-text/snowball-v2.txt
echo "*** snowballv3 ***"
python3 level9.py -g snowballv3 -d >game-text/snowball-v3-dict.txt
python3 level9.py -g snowballv3 -m >game-text/snowball-v3-descs.txt
python3 level9.py -g snowballv3 -e >exits/snowball-v3-exits.txt
python3 decompiler.py -g snowballv3 >decompilation/snowball-v3.txt
python3 level9.py -g snowballv3 -a >full-game-text/snowball-v3.txt
echo "*** worm ***"
python3 level9.py -g worm -d >game-text/worm-in-paradise-v3-dict.txt
python3 level9.py -g worm -m >game-text/worm-in-paradise-v3-descs.txt
python3 level9.py -g worm -e >exits/worm-in-paradise-v3-exits.txt
python3 decompiler.py -g worm >decompilation/worm-in-paradise-v3.txt
python3 level9.py -g worm -a >full-game-text/worm-in-paradise-v3.txt
echo "*** wormv3 ***"
python3 level9.py -g wormv3 -d >game-text/worm-in-paradise-sd-v3-dict.txt
python3 level9.py -g wormv3 -m >game-text/worm-in-paradise-sd-v3-descs.txt
python3 level9.py -g wormv3 -e >exits/worm-in-paradise-sd-v3-exits.txt
python3 decompiler.py -g wormv3 >decompilation/worm-in-paradise-sd-v3.txt
python3 level9.py -g wormv3 -a >full-game-text/worm-in-paradise-sd-v3.txt
echo "*** archers ***"
python3 level9.py -g archers -d >game-text/archers-v3-1-dict.txt
python3 level9.py -g archers -m >game-text/archers-v3-1-descs.txt
python3 level9.py -g archers -e >exits/archers-v3-1-exits.txt
python3 decompiler.py -g archers >decompilation/archers-v3-1.txt
echo "*** archersp2 ***"
python3 level9.py -g archersp2 -d >game-text/archers-v3-2-dict.txt
python3 level9.py -g archersp2 -m >game-text/archers-v3-2-descs.txt
python3 level9.py -g archersp2 -e >exits/archers-v3-2-exits.txt
python3 decompiler.py -g archersp2 >decompilation/archers-v3-2.txt
echo "*** archersp3 ***"
python3 level9.py -g archersp3 -d >game-text/archers-v3-3-dict.txt
python3 level9.py -g archersp3 -m >game-text/archers-v3-3-descs.txt
python3 level9.py -g archersp3 -e >exits/archers-v3-3-exits.txt
python3 decompiler.py -g archersp3 >decompilation/archers-v3-3.txt
echo "*** archersp4 ***"
python3 level9.py -g archersp4 -d >game-text/archers-v3-4-dict.txt
python3 level9.py -g archersp4 -m >game-text/archers-v3-4-descs.txt
python3 level9.py -g archersp4 -e >exits/archers-v3-4-exits.txt
python3 decompiler.py -g archersp4 >decompilation/archers-v3-4.txt
echo "*** growing ***"
python3 level9.py -g growing -d >game-text/growing-pains-v3-1-dict.txt
python3 level9.py -g growing -m >game-text/growing-pains-v3-1-descs.txt
python3 level9.py -g growing -e >exits/growing-pains-v3-1-exits.txt
python3 decompiler.py -g growing >decompilation/growing-pains-v3-1.txt
python3 level9.py -g growing -a >full-game-text/growing-pains-v3-1.txt
echo "*** growingp2 ***"
python3 level9.py -g growingp2 -d >game-text/growing-pains-v3-2-dict.txt
python3 level9.py -g growingp2 -m >game-text/growing-pains-v3-2-descs.txt
python3 level9.py -g growingp2 -e >exits/growing-pains-v3-2-exits.txt
python3 decompiler.py -g growingp2 >decompilation/growing-pains-v3-2.txt
echo "*** growingp3 ***"
python3 level9.py -g growingp3 -d >game-text/growing-pains-v3-3-dict.txt
python3 level9.py -g growingp3 -m >game-text/growing-pains-v3-3-descs.txt
python3 level9.py -g growingp3 -e >exits/growing-pains-v3-3-exits.txt
python3 decompiler.py -g growingp3 >decompilation/growing-pains-v3-3.txt
echo "*** growingp4 ***"
python3 level9.py -g growingp4 -d >game-text/growing-pains-v3-4-dict.txt
python3 level9.py -g growingp4 -m >game-text/growing-pains-v3-4-descs.txt
python3 level9.py -g growingp4 -e >exits/growing-pains-v3-4-exits.txt
python3 decompiler.py -g growingp4 >decompilation/growing-pains-v3-4.txt
echo "*** secret ***"
python3 level9.py -g secret -d >game-text/secret-diary-v3-1-dict.txt
python3 level9.py -g secret -m >game-text/secret-diary-v3-1-descs.txt
python3 level9.py -g secret -e >exits/secret-diary-v3-1-exits.txt
python3 decompiler.py -g secret >decompilation/secret-diary-v3-1.txt
python3 level9.py -g secret -a >full-game-text/secret-diary-v3-1.txt
echo "*** secretp2 ***"
python3 level9.py -g secretp2 -d >game-text/secret-diary-v3-2-dict.txt
python3 level9.py -g secretp2 -m >game-text/secret-diary-v3-2-descs.txt
python3 level9.py -g secretp2 -e >exits/secret-diary-v3-2-exits.txt
python3 decompiler.py -g secretp2 >decompilation/secret-diary-v3-2.txt
echo "*** secretp3 ***"
python3 level9.py -g secretp3 -d >game-text/secret-diary-v3-3-dict.txt
python3 level9.py -g secretp3 -m >game-text/secret-diary-v3-3-descs.txt
python3 level9.py -g secretp3 -e >exits/secret-diary-v3-3-exits.txt
python3 decompiler.py -g secretp3 >decompilation/secret-diary-v3-3.txt
echo "*** secretp4 ***"
python3 level9.py -g secretp4 -d >game-text/secret-diary-v3-4-dict.txt
python3 level9.py -g secretp4 -m >game-text/secret-diary-v3-4-descs.txt
python3 level9.py -g secretp4 -e >exits/secret-diary-v3-4-exits.txt
python3 decompiler.py -g secretp4 >decompilation/secret-diary-v3-4.txt
echo "*** jewels ***"
python3 level9.py -g jewels -a >full-game-text/jewels-of-darkness-v3-1.txt
echo "*** jewelsp2 ***"
echo "*** jewelsp3 ***"
echo "*** silicon ***"
python3 level9.py -g silicon -a >full-game-text/silicon-dreams-v3-1.txt
echo "*** siliconp2 ***"
echo "*** siliconp3 ***"
echo "*** timemagik ***"
python3 level9.py -g timemagik -a >full-game-text/time-and-magik-v4-1.txt
echo "*** timemagikp2 ***"
echo "*** timemagikp3 ***"
rm -f parser.log
echo "+++ Level 9 picture decompilation +++"
python3 l9pic.py | gzip -9 -c >pics/decompiled.txt.gz
python3 l9bitmap.py
