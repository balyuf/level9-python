###############################################################################
# Level 9 Version 1 Configuration Table
# -------------------------------------
#
# Later versions of Level 9 games have a configuration table at the start 
# however version 1 games do not have this. The BBC Micro version 1 games
# DO however have a configuration table for each game. I don't know if this is
# consistently implemented yet (need to learn some Z80 and memory addressing
# to understand the Spectrum ones). 
#
# A note on the configuration attributes:
#
# filename       - BBC Micro filename by run by default if you chooose
#                  game via a command line switched
# script         - Script to execute to test the game or get to a certain 
#                  point
# signatureBytes - First 5 bytes of the A-Code - allows a game file from
#                  any platform to be scanned and the game to be identified.
#                  Also used to find the offset from the start of the game file
#                  for the start of the A-Code (used below for the offsets)
# offsets        - Where each of the major game file components are relative
#                  to the start of the A-Code in the file
# lists          - For reference lists, location in the game file (reference
#                  list is e.g. starting location of each object). These will
#                  always be negative and are before the A-Code for version 1 
#                  games.
#                  
#                  For dynamic lists e.g. an objects current location, these will
#                  be 0 or greater (positive). This represents the starting
#                  offset on where to store them in the listarea e.g. 
#                  object location might start at 50 in the list area.
#
#                  Note that version 1 games can have a maximum  of 5 lists 
#                  per game (reference and dynamic).
###############################################################################
v1Configuration = {
    "adventure" : {
        "name"              : "Adventure Quest",
        "version"           : 1,
        "filename"          : "roms/ADQUEST",
        "script"            : "test-scripts/adventure-quest-v1.txt",
        "signatureBytes"    : b'\x00\x06\x00\x00\x46',
        "offsets" : {
            "dictionaryOffset"  : -0x04c8,
            "messagesOffset"    :  0x1000,
            "fragmentsOffset"   :  0x49d1,
            "exitsOffset"       : -0x0800            
        },
        "locationsStartMsgId" : 0x12d,                        
        "lists" : [
            -0x0583,
            0x0000,
            -0x0508,
            -0x04e0, 
            None        
        ],
    },    
    "adventurev2" : {
        "name"              : "Adventure Quest",
        "version"           : 2,
        "filename"          : "roms/adventure-quest-v2.dat",
        "script"            : "test-scripts/adventure-quest-v2.txt",
        "locationsStartMsgId" : 0x12d,
    },
    "adventurev3" : {
        "name"              : "Adventure Quest",
        "version"           : 3,
        "filename"          : "roms/adventure-quest-v3.dat",
        "script"            : "test-scripts/adventure-quest-v3.txt",
        "locationsStartMsgId" : 0x12d,
        "exitsStartMsgId"     : 0x3e8,
    },
    "colossal" : {
        "name"              : "Colossal Adventure",
        "version"           : 1,
        "filename"          : "roms/Coloss2",
        "script"            : "test-scripts/colossal-adventure-v1.txt",
        "signatureBytes"    : b'\x20\x04\x00\x49\x00',
        "offsets" : {
            "dictionaryOffset"  : -0x0760,
            "messagesOffset"    :  0x0f80,
            "fragmentsOffset"   :  0x57d7,
            "exitsOffset"       : -0x03b0
        },
        "locationsStartMsgId" : 0x64,                
        "lists" : [
            0x0000,
            -0x004b,
            0x0080,
            -0x002b, 
            0x00d0                
        ],
    },    
    "colossalv2" : {
        "name"              : "Colossal Adventure",
        "version"           : 2,
        "filename"          : "roms/colossal-adventure-v2.dat",
        "script"            : "test-scripts/colossal-adventure-v2.txt",
        "locationsStartMsgId" : 0x64,
    },
    "colossalv3" : {
        "name"              : "Colossal Adventure",
        "version"           : 3,
        "filename"          : "roms/colossal-adventure-v3.dat",
        "script"            : "test-scripts/colossal-adventure-v3.txt",
        "locationsStartMsgId" : 0x64,
        "exitsStartMsgId"     : 0x3e8,
    },
    "dungeon" : {
        "name"              : "Dungeon Adventure",
        "version"           : 1,
        "filename"          : "roms/Dungeo2",
        "script"            : "test-scripts/dungeon-adventure-v1.txt",
        "signatureBytes"    : b'\x00\x06\x00\x00\x44',
        "offsets" : {
            "dictionaryOffset"  : -0x0740,
            "messagesOffset"    :  0x16bf,
            "fragmentsOffset"   :  0x58cc,
            "exitsOffset"       :  0x63e0
        },
        "locationsStartMsgId" : 0x1f4,        
        "lists" : [
            -0x00d6,
            0x0000,
            None,
            None,
            None
        ]
    },    
    "dungeonv2" : {
        "name"              : "Dungeon Adventure",
        "version"           : 2,
        "filename"          : "roms/dungeon-adventure-v2.dat",
        "script"            : "test-scripts/dungeon-adventure-v2.txt",
        "locationsStartMsgId" : 0x1f4,
    },
    "dungeonv3" : {
        "name"              : "Dungeon Adventure",
        "version"           : 3,
        "filename"          : "roms/dungeon-adventure-v3.dat",
        "script"            : "test-scripts/dungeon-adventure-v3.txt",
        "locationsStartMsgId" : 0x1f4,
        "exitsStartMsgId"     : 0x3e8,
    },
    "eden" : {
        "name"              : "Return to Eden",
        "version"           : 2,
        #"filename"          : "roms/edenobj.bin",
        "filename"          : "roms/return-to-eden-v2.dat",
        "script"            : "test-scripts/return-to-eden-v2.txt",
        "locationsStartMsgId" : 0x190,
    },
    "edenv3" : {
        "name"              : "Return to Eden",
        "version"           : 3,
        "filename"          : "roms/return-to-eden-v3.dat",
        "script"            : "test-scripts/return-to-eden-v3.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
    },
    "erik" : {
        "name"              : "Erik the Viking",
        "version"           : 2,
        "filename"          : "roms/erik-the-viking-v2.dat",
        "script"            : "test-scripts/erik-the-viking-v2.txt",
        "locationsStartMsgId" : 0x190,
    },
    "gnome" : {
        "name"              : "to Gnome Ranger",
        "version"           : 4,
        "filename"          : "roms/gnome-ranger-v4-1.dat",
        "script"            : "test-scripts/gnome-ranger-v4-1.txt",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "gnome", "gnomep2", "gnomep3" ],
    },
    "gnomep2" : {
        "name"              : "second part of Gnome Ranger",
        "version"           : 4,
        "filename"          : "roms/gnome-ranger-v4-2.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "gnome", "gnomep2", "gnomep3" ],
    },
    "gnomep3" : {
        "name"              : "part 3 of Gnome Ranger",
        "version"           : 4,
        "filename"          : "roms/gnome-ranger-v4-3.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "gnome", "gnomep2", "gnomep3" ],
    },
    "ingrid" : {
        "name"              : "to Ingrid's Back",
        "version"           : 4,
        "filename"          : "roms/ingrids-back-v4-1.dat",
        "script"            : "test-scripts/ingrids-back-v4-1.txt",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "ingrid", "ingridp2", "ingridp3" ],
    },
    "ingridp2" : {
        "name"              : "second part of Ingrid's Back",
        "version"           : 4,
        "filename"          : "roms/ingrids-back-v4-2.dat",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "ingrid", "ingridp2", "ingridp3" ],
    },
    "ingridp3" : {
        "name"              : "third part of Ingrid's Back",
        "version"           : 4,
        "filename"          : "roms/ingrids-back-v4-3.dat",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "ingrid", "ingridp2", "ingridp3" ],
    },
    "isle" : {
        "name"              : "Emerald Isle",
        "version"           : 2,
        "filename"          : "roms/emerald-isle-v2.dat",
        "script"            : "test-scripts/emerald-isle-v2.txt",
        "locationsStartMsgId" : 0x190,
    },  
    "lancelot" : {
        "name"              : "to \"Lancelot\"",
        "version"           : 4,
        "filename"          : "roms/lancelot-v4-1.dat",
        "script"            : "test-scripts/lancelot-v4-1.txt",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "lancelot", "lancelotp2", "lancelotp3" ],
    },
    "lancelotp2" : {
        "name"              : "from Lancelot",
        "version"           : 4,
        "filename"          : "roms/lancelot-v4-2.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "lancelot", "lancelotp2", "lancelotp3" ],
    },
    "lancelotp3" : {
        "name"              : "final part of \"Lancelot\"",
        "version"           : 4,
        "filename"          : "roms/lancelot-v4-3.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "lancelot", "lancelotp2", "lancelotp3" ],
    },
    "lords" : {
        "name"              : "Lords of Time",
        "version"           : 1,
        "filename"          : "roms/LORDSOF",
        #"filename"          : "roms/lot.tzx",
        #"filename"          : "roms/LordsOfTime.ssd",
        "script"            : "test-scripts/lords-of-time-v1.txt",

        "signatureBytes"    : b'\x00\x06\x00\x00\x65',
        "offsets" : {
            "dictionaryOffset"  : -0x4a00,
            "messagesOffset"    : -0x3b9d,
            "fragmentsOffset"   : -0x0215,
            "exitsOffset"       : -0x4120
        },
        "locationsStartMsgId" : 0x190,        
        "lists" : [
            -0x3e70,
            0x0000,
            -0x3d30,
            0x0080,
            0x0100
        ]
    },
    "lordsv2" : {
        "name"              : "Lords of Time",
        "version"           : 2,
        "filename"          : "roms/lords-of-time-v2.dat",
        "script"            : "test-scripts/lords-of-time-v2.txt",
        "locationsStartMsgId" : 0x190,
    },
    "lordsv4" : {
        "name"              : "Time and Magik trilogy",
        "version"           : 4,
        "filename"          : "roms/lords-of-time-v4.dat",
        "script"            : "test-scripts/lords-of-time-v4.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
    },
    "magik" : {
        "name"              : "Price of Magik",
        "version"           : 3,
        "filename"          : "roms/price-of-magik-v3.dat",
        "script"            : "test-scripts/price-of-magik-v3.txt",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
    },
    "magikv4" : {
        "name"              : "Price of Magik",
        "version"           : 4,
        "filename"          : "roms/price-of-magik-v4.dat",
        "script"            : "test-scripts/price-of-magik-v4.txt",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
    },
    "orc" : {
        "name"              : "to Knight Orc",
        "version"           : 4,
        "filename"          : "roms/knight-orc-v4-1.dat",
        "script"            : "test-scripts/knight-orc-v4-1.txt",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "orc", "orcp2", "orcp3" ],
    },
    "orcp2" : {
        "name"              : "A Kind of Magic",
        "version"           : 4,
        "filename"          : "roms/knight-orc-v4-2.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "orc", "orcp2", "orcp3" ],
    },
    "orcp3" : {
        "name"              : "Hordes of the Mountain King",
        "version"           : 4,
        "filename"          : "roms/knight-orc-v4-3.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "orc", "orcp2", "orcp3" ],
    },
    "redmoon" : {
        "name"              : "Red Moon",
        "version"           : 2,
        "filename"          : "roms/red-moon-v2.dat",
        "script"            : "test-scripts/red-moon-v2.txt",
        "locationsStartMsgId" : 0x190,
    },
    "redmoonv4" : {
        "name"              : "Red Moon",
        "version"           : 4,
        "filename"          : "roms/red-moon-v4.dat",
        "script"            : "test-scripts/red-moon-v4.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
    },
    "scapeghost" : {
        "name"              : "\"Scapeghost\"",
        "version"           : 4,
        "filename"          : "roms/scapeghost-v4-1.dat",
        "script"            : "test-scripts/scapeghost-v4-1.txt",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "scapeghost", "scapeghostp2", "scapeghostp3" ],
    },
    "scapeghostp2" : {
        "name"              : "from Scapeghost",
        "version"           : 4,
        "filename"          : "roms/scapeghost-v4-2.dat",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "scapeghost", "scapeghostp2", "scapeghostp3" ],
    },
    "scapeghostp3" : {
        "name"              : "part 3 of Scapeghost",
        "version"           : 4,
        "filename"          : "roms/scapeghost-v4-3.dat",
        "locationsStartMsgId" : 0x320,
        "exitsStartMsgId"     : 0x32,
        "parts"             : [ "scapeghost", "scapeghostp2", "scapeghostp3" ],
    },
    "snowball" : {
        "name"              : "Snowball",
        "version"           : 1,
        "filename"          : "roms/SNOWBAL",
        "script"            : "test-scripts/snowball-v1.txt",
        "signatureBytes"    : b'\x00\x06\x00\x00\xd4',
        "offsets" : {
            "dictionaryOffset"  : -0x0a10,
            "messagesOffset"    :  0x1930,
            "fragmentsOffset"   :  0x5547,
            "exitsOffset"       : -0x0300
        },
        "locationsStartMsgId" : 0x190,
        "lists" : [
            -0x00f0,
            0x0000,
            -0x0050,
            None,
            None
        ],
    },
    "snowballv2" : {
        "name"              : "Snowball",
        "version"           : 2,
        "filename"          : "roms/snowball-v2.dat",
        "script"            : "test-scripts/snowball-v2.txt",
        "locationsStartMsgId" : 0x190,
    },
    "snowballv3" : {
        "name"              : "Snowball",
        "version"           : 3,
        "filename"          : "roms/snowball-v3.dat",
        "script"            : "test-scripts/snowball-v3.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
    },
    "worm" : {
        "name"              : "Worm in Paradise, copyright",
        "version"           : 3,
        "filename"          : "roms/worm-in-paradise-v3.dat",
        "script"            : "test-scripts/worm-in-paradise-v3.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
    },
    "wormv3" : {
        "name"              : "last of the Silicon Dreams",
        "version"           : 3,
        "filename"          : "roms/worm-in-paradise-sd-v3.dat",
        "script"            : "test-scripts/worm-in-paradise-sd-v3.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
    },
    "archers" : {
        "name"              : "part one of the \"The Archers\"",
        "version"           : 3,
        "filename"          : "roms/archers-v3-1.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "archers", "archersp2", "archersp3", "archersp4" ],
    },
    "archersp2" : {
        "name"              : "part two of the \"The Archers\"",
        "version"           : 3,
        "version"           : 3,
        "filename"          : "roms/archers-v3-2.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "archers", "archersp2", "archersp3", "archersp4" ],
    },
    "archersp3" : {
        "name"              : "part three of the \"The Archers\"",
        "version"           : 3,
        "version"           : 3,
        "filename"          : "roms/archers-v3-3.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "archers", "archersp2", "archersp3", "archersp4" ],
    },
    "archersp4" : {
        "name"              : "part four of the \"The Archers\"",
        "version"           : 3,
        "version"           : 3,
        "filename"          : "roms/archers-v3-4.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "archers", "archersp2", "archersp3", "archersp4" ],
    },
    "growing" : {
        "name"              : "to the Growing Pains",
        "version"           : 3,
        "filename"          : "roms/growing-pains-v3-1.dat",
        "script"            : "test-scripts/growing-pains-v3-1.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "growing", "growingp2", "growingp3", "growingp4" ],
    },
    "growingp2" : {
        "name"              : "part 2 of the Growing Pains",
        "version"           : 3,
        "filename"          : "roms/growing-pains-v3-2.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "growing", "growingp2", "growingp3", "growingp4" ],
    },
    "growingp3" : {
        "name"              : "part 3 of the Growing Pains",
        "version"           : 3,
        "filename"          : "roms/growing-pains-v3-3.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "growing", "growingp2", "growingp3", "growingp4" ],
    },
    "growingp4" : {
        "name"              : "Part 4 of the Growing Pains",
        "version"           : 3,
        "filename"          : "roms/growing-pains-v3-4.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "growing", "growingp2", "growingp3", "growingp4" ],
    },
    "secret" : {
        "name"              : "and it is still running",
        "version"           : 3,
        "filename"          : "roms/secret-diary-v3-1.dat",
        "script"            : "test-scripts/secret-diary-v3-1.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "secret", "secretp2", "secretp3", "secretp4" ],
    },
    "secretp2" : {
        "name"              : "part two of the Secret Diary",
        "version"           : 3,
        "filename"          : "roms/secret-diary-v3-2.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "secret", "secretp2", "secretp3", "secretp4" ],
    },
    "secretp3" : {
        "name"              : "to the Secret Diary",
        "version"           : 3,
        "filename"          : "roms/secret-diary-v3-3.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "secret", "secretp2", "secretp3", "secretp4" ],
    },
    "secretp4" : {
        "name"              : "final part of the Secret Diary",
        "version"           : 3,
        "filename"          : "roms/secret-diary-v3-4.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "secret", "secretp2", "secretp3", "secretp4" ],
    },
    "jewels" : {
        "name"              : "first of the Jewels of Darkness",
        "version"           : 3,
        "filename"          : "roms/colossal-adventure-v3.dat",
        "script"            : "test-scripts/jewels-of-darkness-v3-1.txt",
        "locationsStartMsgId" : 0x64,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "jewels", "jewelsp2", "jewelsp3" ],
    },
    "jewelsp2" : {
        "name"              : "second of the Jewels of Darkness",
        "version"           : 3,
        "filename"          : "roms/adventure-quest-v3.dat",
        "locationsStartMsgId" : 0x12d,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "jewels", "jewelsp2", "jewelsp3" ],
    },
    "jewelsp3" : {
        "name"              : "last of the Jewels of Darkness",
        "version"           : 3,
        "filename"          : "roms/dungeon-adventure-v3.dat",
        "locationsStartMsgId" : 0x1f4,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "jewels", "jewelsp2", "jewelsp3" ],
    },
    "silicon" : {
        "name"              : "first of the Silicon Dreams",
        "version"           : 3,
        "filename"          : "roms/snowball-v3.dat",
        "script"            : "test-scripts/silicon-dreams-v3-1.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "silicon", "siliconp2", "siliconp3" ],
    },
    "siliconp2" : {
        "name"              : "second of the Silicon Dreams",
        "version"           : 3,
        "filename"          : "roms/return-to-eden-v3.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "silicon", "siliconp2", "siliconp3" ],
    },
    "siliconp3" : {
        "name"              : "last of the Silicon Dreams",
        "version"           : 3,
        "filename"          : "roms/worm-in-paradise-sd-v3.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "silicon", "siliconp2", "siliconp3" ],
    },
    "timemagik" : {
        "name"              : "Time and Magik trilogy",
        "version"           : 4,
        "filename"          : "roms/lords-of-time-v4.dat",
        "script"            : "test-scripts/time-and-magik-v4-1.txt",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "timemagik", "timemagikp2", "timemagikp3" ],
    },
    "timemagikp2" : {
        "name"              : "second part of Time and Magik",
        "version"           : 4,
        "filename"          : "roms/red-moon-v4.dat",
        "locationsStartMsgId" : 0x190,
        "exitsStartMsgId"     : 0x3e8,
        "parts"             : [ "timemagik", "timemagikp2", "timemagikp3" ],
    },
    "timemagikp3" : {
        "name"              : "third part of Time and Magik",
        "version"           : 4,
        "filename"          : "roms/price-of-magik-v4.dat",
        "locationsStartMsgId" : 0x3e8,
        "exitsStartMsgId"     : 0x64,
        "parts"             : [ "timemagik", "timemagikp2", "timemagikp3" ],
    },
}
