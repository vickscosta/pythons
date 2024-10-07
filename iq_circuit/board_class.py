"""class for board operations"""

import numpy as np
from config import EMPTY_CHAR, ZERO, piece_dct, char_dct


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

    def check_up(self, position: tuple, line: int, col: int, letter: str) -> str:
        """checks UP for continuity"""

        if position[0] == 0 and line == 0 and letter in ["L","J","I","up"]:
            return "False"
        if position[0] != 0:
            board_char = self.matrix[position[0] + line - 1, position[1] + col]
            if board_char == EMPTY_CHAR:
                return "continue"
            if (board_char in ['r','7','I',"down"]
                and letter in ["r","7","-","down","left","right","blank"]):
                return "False"
        return "True"

    def check_down(self, position: tuple, line: int, col: int, letter: str) -> str:
        """checks DOWN for continuity"""

        if position[0] + line == self.height - 1 and letter in ["r","7","I","down"]:
            return "False"
        if position[0] + line < self.height - 1:
            board_char = self.matrix[position[0] + line + 1, position[1] + col]
            if board_char == EMPTY_CHAR:
                return "continue"
            if (board_char in ['L','J','I',"up"]
                and letter in ["L","J","-","up","left","right","blank"]):
                return "False"
        return 'True'

    ### nothing prevents that last square of the new piece to end abruptly

    def check_left(self, position: tuple, line: int, col: int, letter: str) -> str:
        """checks LEFT for continuity"""

        if position[1] == 0 and col == 0 and letter in ["J","7","-","left"]:
            return "False"

        if position[1] != 0:
            board_char = self.matrix[position[0] + line, position[1] + col - 1]
            if board_char == EMPTY_CHAR:
                return "continue"
            if (board_char in ['L','r','-',"right"]
                and letter in ["L","r","I","right","up","down","blank"]):
                return "False"
        return "True"

    def check_right(self, position: tuple, line: int, col: int, letter: str) -> str:
        """checks RIGHT for continuity"""

        if position[1] + col == self.width - 1 and letter in ["L","r","-","right"]:
            return "False"

        if position[1] + col < self.width - 1:
            board_char = self.matrix[position[0] + line, position[1] + col + 1]
            if board_char == EMPTY_CHAR:
                return "continue"
            if (board_char in ['J','7','-',"left"]
                and letter in ["J","7","I","left","up","down","blank"]):
                return "False"
        return 'True'

    def valid_path(self, pos: tuple, desc: list) -> bool:
        '''checks to see if pathways are respected'''

        for idx_ln, line in enumerate(desc):
            for idx_char, char in enumerate(line):

                if char == ZERO:
                    continue
                # check for compatibility UP
                status = self.check_up(pos, idx_ln, idx_char, char)
                if status == "continue":
                    continue
                if status == "False":
                    return False
                # check for compatibility DOWN
                status = self.check_down(pos, idx_ln, idx_char, char)
                if status == "continue":
                    continue
                if status == "False":
                    return False
                # check for compatibility LEFT
                status = self.check_left(pos, idx_ln, idx_char, char)
                if status == "continue":
                    continue
                if status == "False":
                    return False
                # check for compatibility RIGHT
                status = self.check_right(pos, idx_ln, idx_char, char)
                if status == "continue":
                    continue
                if status == "False":
                    return False
        return True

    def add_piece(self, new_piece: tuple[str, str, str, tuple]) -> bool:
        """add a piece to the board"""

        block, face, rotation, position = new_piece
        piece_description = piece_dct[block][face][rotation]

        # check if first cell is empty or nothing is required in that spot
        if not (self.first_cell_free(position) or piece_description[0][0] == ZERO):
            print(new_piece,'corner occupied')
            return False
        # check if cell fits on the board
        if not self.respects_board_limits(position, piece_description):
            print(new_piece, "border limits")
            return False
        # check if space is avalaible
        if not self.space_is_available(position, piece_description):
            print(new_piece,"no space")
            return False
        # check if path is broken
        if not self.valid_path(position,piece_description):
            print(new_piece,'valid path')
            return False

        # puts piece
        self.set_piece(block, piece_description, position)

        return True

    def set_path(self) -> None:
        """transforms symbols"""

        self.path = np.array(
            [
                [char_dct[self.matrix[height, width]] for width in range(self.width)]
                for height in range(self.height)
            ]
        )

    def initialise(self, start_map: list[tuple]) -> None:
        """puts first blocks in"""

        for piece in start_map:
            self.add_piece(piece)
            # self.set_path()
            # print_board(self.path)

        self.set_path()
