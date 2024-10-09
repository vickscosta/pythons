"""class for board operations"""

import numpy as np
import copy
from config import EMPTY_CHAR, ZERO, BLANK, piece_dct, char_dct


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
        if pos[0] + len(desc) > self.height:
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

    def check_up(self, position: tuple, piece: list) -> bool:
        """checks UP for continuity"""

        list_of_connectors = ["L", "J", "I", "up"]

        # first line limitations
        for char in piece[0]:
            if position[0] == 0 and char in list_of_connectors:
                return False

        # limitations based on the existing
        for idxl, line in enumerate(piece):
            for idxc, char in enumerate(line):
                if position[0] == 0 and idxl == 0 :
                    continue
                board_char = self.matrix[position[0] + idxl - 1, position[1] + idxc]

                if board_char == EMPTY_CHAR:
                    continue

                if char == ZERO:
                    continue

                if board_char in ["r", "7", "I", "down"]:
                    if char in list_of_connectors:
                        continue
                    return False

                if char in list_of_connectors:
                    return False
        return True

    def check_down(self, position: tuple, piece: list) -> bool:
        """checks down for continuity"""

        list_of_connectors = ["r", "7", "I", "down"]

        # bottom of the board limitations
        for char in piece[-1]:
            if position[0] + len(piece) == self.height and char in list_of_connectors:
                return False

        # limitations based on the existing
        if position[0] + len(piece) < self.height:
            for idxl, line in enumerate(piece):
                for idxc, char in enumerate(line):
                    board_char = self.matrix[position[0] + idxl + 1, position[1] + idxc]

                    if board_char == EMPTY_CHAR:
                        continue

                    if char == ZERO:
                        continue

                    if board_char in ["L", "J", "I", "up"]:
                        if char in list_of_connectors:
                            continue
                        return False

                    if char in list_of_connectors:
                        return False
        return True

    def check_left(self, position: tuple, piece: list) -> bool:
        """checks LEFT for continuity"""

        list_of_connectors = ["J", "7", "-", "left"]

        # first column limitations
        if position[1] == 0:
            for line in piece:
                char = line[0]
                if char in list_of_connectors:
                    return False

        # limitations based on the existing
        for idxl, line in enumerate(piece):
            for idxc, char in enumerate(line):
                if position[1] == 0 and idxc == 0 :
                    continue
                board_char = self.matrix[position[0] + idxl, position[1] + idxc - 1]

                if board_char == EMPTY_CHAR:
                    continue

                if char == ZERO:
                    continue

                if board_char in ["L", "r", "-", "right"]:
                    if char in list_of_connectors:
                        continue
                    return False

                if char in list_of_connectors:
                    return False
        return True

    def check_right(self, position: tuple, piece: list) -> bool:
        """checks right for continuity"""

        # last column limitations
        if position[1] + len(piece[0]) == self.width:
            for line in piece:
                char = line[-1]
                if char in ["L", "r", "-", "right"]:
                    return False

        # limitations based on the existing
        if position[1] + len(piece[0]) < self.width:
            for idxl, line in enumerate(piece):
                for idxc, char in enumerate(line):
                    board_char = self.matrix[position[0] + idxl, position[1] + idxc + 1]
                    if board_char in ["J", "7", "-", "left"] and char in [
                        "-",
                        "L",
                        "r",
                        "right",
                    ]:
                        continue
                    if board_char == EMPTY_CHAR or char in [
                        ZERO,
                        "down",
                        "up",
                        "left",
                        "J",
                        "7",
                        "I",
                        BLANK
                    ]:
                        continue
                    return False
        return True

    def valid_path(self, pos: tuple, desc: list) -> bool:
        """checks to see if pathways are respected"""

        # check for compatibility
        if not self.check_up(pos, desc):
            return False
        if not self.check_down(pos, desc):
            return False
        if not self.check_left(pos, desc):
            return False
        if not self.check_right(pos, desc):
            return False
        return True

    def add_piece(self, new_piece: tuple[str, str, str, tuple]) -> bool:
        """add a piece to the board"""

        block, face, rotation, position = new_piece
        piece_description = piece_dct[block][face][rotation]

        # check if first cell is empty or nothing is required in that spot
        if not (self.first_cell_free(position) or piece_description[0][0] == ZERO):
            print(new_piece, "corner occupied")
            return False
        # check if cell fits on the board
        if not self.respects_board_limits(position, piece_description):
            print(new_piece, "border limits")
            return False
        # check if space is avalaible
        if not self.space_is_available(position, piece_description):
            print(new_piece, "no space")
            return False
        # check if path is broken
        if not self.valid_path(position, piece_description):
            print(new_piece, "invalid path")
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
