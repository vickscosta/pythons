"""contains the starting position"""

from config import piece_dct, UP, DOWN, LEFT, RIGHT, BLANK

original_piece_map = [
    ("!", "face0", "rotation1", (0, 1)),
    ("v", "face0", "rotation3", (2, 0)),
    ("|", "face1", "rotation0", (0, 2)),
    ("^", "face1", "rotation1", (1, 2)),
    ("t", "face1", "rotation0", (2, 2)),
    ("s", "face0", "rotation3", (1, 4)),
    ("i", "face0", "rotation2", (1, 5)),
]

target_path = [
    [BLANK, DOWN, "r", LEFT, BLANK, "r", "-", "7"],
    [BLANK, "I", "I", DOWN, DOWN, "L", LEFT, "I"],
    [BLANK, "I", "I", "I", "L", "-", "7", "I"],
    [RIGHT, "J", "L", "J", BLANK, "L", "J"],
]
