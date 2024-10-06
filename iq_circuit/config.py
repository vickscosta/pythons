'''contains the dictionaries and configurations'''

BOARD_WIDTH = 8
BOARD_HEIGHT = 4

EMPTY_CHAR = " "

char_dct = {
    "L": "┗",
    "J": "┛",
    "r": "┏",
    "7": "┓",
    "-": "━",
    "I": "┃",

    "o": "◆",
    "up":"▲",
    "down": "▼",
    "left": "◀",
    "right": "▶",
    "blank": "□"
    }

piece_dct = {
    "v1": {
        "face0": [["down",0],["L","-"]],
        "face1": [["I",0],["L","-"]]
        },
    "v2": {
        "face0": [["r",0],["L","-"]],
        "face1": [["right",0],["-","-"]],
        },
    "i1": {
        "face0": [["right","7"]],
        "face1": [["-","-"]],
        "face2": [["blank","blank"]]
        },
    "i2": {
        "face0": [["right","-"]],
        "face1": [["right","-"]],
        "face2": [["blank","blank"]]
        },
    "I1": {
        "face0": [["right","-","-"]],
        "face1": [["-","-","J"]],
        "face2": [["blank","blank","blank"]]
        },
    "I2": {
        "face0": [["-","J","blank"]],
        "face1": [["r","left","blank"]],
        "face2": [["blank","blank","blank"]]
        },
    "o": {
        "face0": [["7","I"],["L","J"]],
        "face1": [["-","left"],["-","7"]]
        },
    "L": {
        "face0": [["I",0,0],["L","-","J"]],
        "face1": [["r","-","J"],["L",0,0]]
        },
    "s": {
        "face0": [[0,"r","left"],["blank","I",0]],
        "face1": [["r","-",0],[0,"blank","blank"]]
        },
    "t": {
        "face0": [[0,"L",0],["L","-","-"]],
        "face1": [[0,"I",0],["L","J","blank"]]
        },
    }
