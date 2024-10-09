"""contains the dictionaries and configurations"""

BOARD_WIDTH = 8
BOARD_HEIGHT = 4

EMPTY_CHAR = "."
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
BLANK = "blank"
ZERO = "0"

char_dct = {
    "L": "┗",
    "J": "┛",
    "r": "┏",
    "7": "┓",
    "-": "━",
    "I": "┃",
    "o": "◆",
    "up": "▲",
    "down": "▼",
    "left": "◀",
    "right": "▶",
    "blank": "□",
    ".": ".",
}

piece_dct = {
    "v": {
        "face0": {
            "rotation0": [[DOWN, ZERO], ["L", "-"]],
            "rotation1": [["r", LEFT], ["I", ZERO]],
            "rotation2": [["-", "7"], [ZERO, UP]],
            "rotation3": [[ZERO, "I"], [RIGHT, "J"]]},
        "face1": {
            "rotation0": [["I", ZERO], ["L", "-"]],
            "rotation1": [["r", '-'], ["I", ZERO]],
            "rotation2": [["-", "7"], [ZERO, "I"]],
            "rotation3": [[ZERO, "I"], ["-", "J"]]}},
    "^": {
        "face0": {
            "rotation0": [["r", ZERO], ["L", "-"]],
            "rotation1": [["r", LEFT], ["I", ZERO]],
            "rotation2": [["-", "7"], [ZERO, UP]],
            "rotation3": [[ZERO, "I"], [RIGHT, "J"]]},
        "face1": {
            "rotation0": [[RIGHT, ZERO], ["-", "-"]],
            "rotation1": [["I", DOWN], ["I", ZERO]],
            "rotation2": [["-", "-"], [ZERO, LEFT]],
            "rotation3": [[ZERO, "I"], [UP, "I"]]}},
    "i": {
        "face0": {
            "rotation0": [[RIGHT, "7"]],
            "rotation1": [[DOWN], ["J"]],
            "rotation2": [["L", LEFT]],
            "rotation3": [["r"], [UP]]},
        "face1": {
            "rotation0": [["-", "-"]],
            "rotation1": [["I"], ["I"]]},
        "face2": {
            "rotation0": [[BLANK, BLANK]],
            "rotation1": [[BLANK], [BLANK]]}},
    "!": {
        "face0": {
            "rotation0": [[RIGHT, "-"]],
            "rotation1": [[DOWN], ["I"]],
            "rotation2": [["-", LEFT]],
            "rotation3": [["I"], [UP]]},
        "face1": {
            "rotation0": [["I", BLANK]],
            "rotation1": [["-"], [BLANK]],
            "rotation2": [[BLANK, "I"]],
            "rotation3": [[BLANK], ["-"]]},
        "face2": {
            "rotation0": [[BLANK, BLANK]],
            "rotation1": [[BLANK], [BLANK]]}},
    "I": {
        "face0": {
            "rotation0": [[RIGHT, "-", "-"]],
            "rotation1": [[DOWN], ["I"], ["I"]],
            "rotation2": [["-", "-", LEFT]],
            "rotation3": [["I"], ["I"], [UP]]},
        "face1": {
            "rotation0": [["-", "-", "J"]],
            "rotation1": [["I"], ["I"], ["L"]],
            "rotation2": [["r", "-", "-"]],
            "rotation3": [["7"], ["I"], ["I"]]},
        "face2": {
            "rotation0": [[BLANK, BLANK, BLANK]],
            "rotation1": [[BLANK], [BLANK], [BLANK]]}},
    "|": {
        "face0": {
            "rotation0": [["-", "J", BLANK]],
            "rotation1": [["I"], ["L"], [BLANK]],
            "rotation2": [[BLANK, "r", "-"]],
            "rotation3": [[BLANK], ["7"], ["I"]]},
        "face1": {
            "rotation0": [["r", LEFT, BLANK]],
            "rotation1": [["7"], [UP], [BLANK]],
            "rotation2": [[BLANK, RIGHT, "J"]],
            "rotation3": [[BLANK], [DOWN], ["L"]]},
        "face2": {
            "rotation0": [[BLANK, BLANK, BLANK]],
            "rotation1": [[BLANK], [BLANK], [BLANK]]}},
    "o": {
        "face0": {
            "rotation0": [["7", "I"], ["L", "J"]],
            "rotation1": [["r", "J"], ["L", "-"]],
            "rotation2": [["r", "7"], ["I", "L"]],
            "rotation3": [["-", "7"], ["r", "J"]]},
        "face1": {
            "rotation0": [["-", LEFT], ["-", "7"]],
            "rotation1": [["I", "I"], ["J", UP]],
            "rotation2": [["L", "-"], [RIGHT, "-"]],
            "rotation3": [[DOWN, "r"], ["I", "I"]]}},
    "L": {
        "face0": {
            "rotation0": [["I", ZERO, ZERO], ["L", "-", "J"]],
            "rotation1": [["r", "-"], ["I", ZERO], ["L", ZERO]],
            "rotation2": [["r", '-', '7'], [ZERO, ZERO, "I"]],
            "rotation3": [[ZERO, "7"], [ZERO, "I"], ["-", "J"]]},
        "face1": {
            "rotation0": [["r", "-", "J"], ["L", ZERO, ZERO]],
            "rotation1": [["r", "7"], [ZERO, "I"], [ZERO, "L"]],
            "rotation2": [[ZERO, ZERO, "7"], ["r", "-", "J"]],
            "rotation3": [["7", ZERO], ["I", ZERO], ["L", "J"]]}},
    "s": {
        "face0": {
            "rotation0": [[ZERO, "r", LEFT], [BLANK, "I", ZERO]],
            "rotation1": [[BLANK, ZERO], ["-", "7"], [ZERO, UP]],
            "rotation2": [[ZERO, "I", BLANK], [RIGHT, "J", ZERO]],
            "rotation3": [[DOWN, ZERO], ["L", "-"], [ZERO, BLANK]]},
        "face1": {
            "rotation0": [["r", "-", ZERO], [ZERO, BLANK, BLANK]],
            "rotation1": [[ZERO, "7"], [BLANK, "I"], [BLANK, ZERO]],
            "rotation2": [[BLANK, BLANK, ZERO], [ZERO, "-", "J"]],
            "rotation3": [[ZERO, BLANK], ["I", BLANK], ["L", ZERO]]}},
    "t": {
        "face0": {
            "rotation0": [[ZERO, "L", ZERO], ["L", "-", "-"]],
            "rotation1": [["r", ZERO], ["I", "r"], ["I", ZERO]],
            "rotation2": [["-", "-", "7"], [ZERO, "7", ZERO]],
            "rotation3": [[ZERO, "I"], ["J", "I"], [ZERO, "J"]]},
        "face1": {
            "rotation0": [[ZERO, "I", ZERO], ["L", "J", BLANK]],
            "rotation1": [["r", ZERO], ["L", "-"], [BLANK, ZERO]],
            "rotation2": [[BLANK, "r", "7"], [ZERO, "I", ZERO]],
            "rotation3": [[ZERO, BLANK], ["-", "7"], [ZERO, "J"]]}}
    }
