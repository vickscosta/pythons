"""class for board operations"""

import copy
import numpy as np
from config import EMPTY_CHAR, ZERO, piece_dct, char_dct

connector_dict = {
    "UP":["L", "J", "I", "up"],
    "DOWN": ["r", "7", "I", "down"],
    "LEFT": ["J", "7", "-", "left"],
    "RIGHT": ["L", "r", "-", "right"]}

board_connector_dict = {
    "UP": connector_dict["DOWN"],
    "DOWN": connector_dict["UP"],
    "LEFT": connector_dict["RIGHT"],
    "RIGHT": connector_dict["LEFT"]}

def print_board(board: np) -> None:
    """prints evething"""
    string = "\n" + "\n".join(" ".join(row) for row in board) + "\n"
    print(string)


class BoardClass:
    """creates and manages boards"""

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.piece_map = np.full((height, width), EMPTY_CHAR, dtype="<U1")
        self.matrix = np.full((height, width), EMPTY_CHAR, dtype="<U5")
        self.path = np.full((height, width), EMPTY_CHAR, dtype="<U1")

    def first_cell_free(self, position: tuple) -> bool:
        """checks if the first piece is occupied"""

        row, column = position
        if self.matrix[row, column] == EMPTY_CHAR:
            return True
        return False

    def set_piece(self, set_block: str, set_piece_desc: list, set_position: tuple) -> None:
        """writes into the matrix and the piece map"""

        for idx_ln, line in enumerate(set_piece_desc):
            for idx_char, char in enumerate(line):
                # exception for empty space
                if char != ZERO:
                    self.matrix[
                        set_position[0] + idx_ln, set_position[1] + idx_char
                    ] = char
                    self.piece_map[
                        set_position[0] + idx_ln, set_position[1] + idx_char
                    ] = set_block

    def respects_board_limits(self, pos: tuple[int], desc: list[list[str]]) -> bool:
        """checks if the piece fits the board as a function of it's position"""
        # rows check
        if pos[0] + len(desc)> self.height:
            return False
        # cols check
        if pos[1] + len(desc[0]) > self.width:
            return False
        return True

    def space_is_available(self, pos: tuple[int], desc: list[list[str]]) -> bool:
        """checks if the piece fits the available place"""

        for idx_ln, line in enumerate(desc):
            for idx_char, char in enumerate(line):
                # exception for zeros in the piece
                if char == ZERO:
                    continue
                if not (
                    self.matrix[pos[0] + idx_ln, pos[1] + idx_char] == ZERO
                    or self.matrix[pos[0] + idx_ln, pos[1] + idx_char] == EMPTY_CHAR
                ):
                    return False
        return True

    def edge_case_limitations(self, direction: str, position: tuple, piece: list) -> bool:
        '''checks for continuity in edge cases'''

        edge_conditions = {
            "UP": [position[0], 0, piece[0]],
            "DOWN": [position[0] + len(piece), self.height, piece[-1]],
            "LEFT": [position[1], 0, piece, 0],
            "RIGHT": [position[1] + len(piece[0]), self.width, piece, -1]}

        if edge_conditions[direction][0] == edge_conditions[direction][1]:
            for char in edge_conditions[direction][2]:
                if (direction in ["UP","DOWN"]
                    and char in connector_dict[direction]):
                    return False
                if (direction in ["LEFT","RIGHT"]
                    and char[edge_conditions[direction][3]] in connector_dict[direction]):
                    return False
        return True

    def board_limitations(self, direction: str, position: tuple, piece: list) -> bool:
        '''checks for continuity in edge cases'''

        conditions = {"UP": -1,"DOWN": +1,"LEFT": -1,"RIGHT": +1}

        for idxl, line in enumerate(piece):
            for idxc, char in enumerate(line):
                if direction in ["UP","DOWN"]:
                    try:
                        board_char = self.matrix[
                            position[0] + idxl + conditions[direction],
                            position[1] + idxc]
                    except IndexError:
                        continue
                else:
                    try:
                        board_char = self.matrix[
                            position[0] + idxl,
                            position[1] + idxc + conditions[direction]]
                    except IndexError:
                        continue

                if board_char == EMPTY_CHAR:
                    continue

                if char == ZERO:
                    continue

                if board_char in board_connector_dict[direction]:
                    if char in connector_dict[direction]:
                        continue
                    return False

                if char in connector_dict[direction]:
                    return False

        return True

    def generic_check(self, direction: str, position: tuple, piece: list) -> bool:
        """generic function to check path continuity"""

        if not self.edge_case_limitations(direction, position, piece):
            return False
        if not self.board_limitations(direction, position, piece):
            return False
        return True

    def valid_path(self, pos: tuple, desc: list) -> bool:
        """checks to see if pathways are respected"""

        # check for compatibility
        if not self.generic_check("UP", pos, desc):
            return False
        if not self.generic_check("DOWN", pos, desc):
            return False
        if not self.generic_check("LEFT", pos, desc):
            return False
        if not self.generic_check("RIGHT", pos, desc):
            return False
        return True

    def add_piece(self, new_piece: tuple[str, str, str, tuple]) -> bool:
        """add a piece to the board"""

        block, face, rotation, position = new_piece
        piece_description = piece_dct[block][face][rotation]

        # check if first cell is empty or nothing is required in that spot
        if not (self.first_cell_free(position) or piece_description[0][0] == ZERO):
            # print(new_piece, "corner occupied")
            return False
        # check if cell fits on the board
        if not self.respects_board_limits(position, piece_description):
            # print(new_piece, "border limits")
            return False
        # check if space is avalaible
        if not self.space_is_available(position, piece_description):
            # print(new_piece, "no space")
            return False
        # check if path is broken
        if not self.valid_path(position, piece_description):
            # print(new_piece, "invalid path")
            return False

        # puts piece
        self.set_piece(block, piece_description, position)
        self.set_path()
        # print('*** Added', block, piece_description, position)

        return True

    def set_path(self) -> None:
        """transforms symbols"""

        self.path = np.array(
            [[char_dct[self.matrix[height, width]] for width in range(self.width)]
                for height in range(self.height)])

    def initialise(self, start_map: list[tuple]) -> None:
        """puts first blocks in"""

        for piece in start_map:
            self.add_piece(piece)
            # self.set_path()
            # print_board(self.path)
        # self.set_path()

    def remove_piece(self, new_piece: tuple[str, str, str, tuple]) -> None:
        """remove a piece to the board"""

        block, face, rotation, position = new_piece
        piece_description = piece_dct[block][face][rotation]

        new_piece_description = copy.deepcopy(piece_description)

        block = EMPTY_CHAR

        for idxl, line in enumerate(piece_description):
            for idxc, char in enumerate(line):
                if char == ZERO:
                    new_piece_description[idxl][idxc] = ZERO
                else:
                    new_piece_description[idxl][idxc] = EMPTY_CHAR

        # removes piece
        self.set_piece(block, new_piece_description, position)
        self.set_path()
