"""contains the starting position"""

from config import  DOWN, LEFT, RIGHT, BLANK

MAP2 = [
    ("t", "face1", "rotation1", (0, 0)),
    ("|", "face1", "rotation2", (3, 0)),
    ("^", "face1", "rotation2", (0, 1)),
    ("i", "face0", "rotation0", (2, 1)),
    ("I", "face0", "rotation0", (3, 3)),
    ("!", "face0", "rotation0", (0, 4)),
    ("o", "face1", "rotation0", (0, 6)),
]

MAP1 = [
    ("!", "face0", "rotation1", (0, 1)),
    ("v", "face0", "rotation3", (2, 0)),
    ("|", "face1", "rotation0", (0, 2)),
    ("^", "face1", "rotation1", (1, 2)),
    ("t", "face1", "rotation0", (2, 2)),
    ("s", "face0", "rotation3", (1, 4)),
    ("i", "face0", "rotation2", (1, 5)),
]

tp1 = [
    [BLANK, DOWN, "r", LEFT, BLANK, "r", "-", "7"],
    [BLANK, "I", "I", DOWN, DOWN, "L", LEFT, "I"],
    [BLANK, "I", "I", "I", "L", "-", "7", "I"],
    [RIGHT, "J", "L", "J", BLANK, "L", "J"],
]

original_piece_map = MAP2
target_path = tp1
