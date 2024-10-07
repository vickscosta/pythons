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

    def set_piece(
        self, set_block: str, set_piece_desc: list[list[str]], set_position: tuple[int]
    ) -> None:
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

    def add_piece(self, new_piece: tuple[str, str, str, tuple]) -> bool:
        """add a piece to the board"""

        block, face, rotation, position = new_piece
        piece_description = piece_dct[block][face][rotation]

        # check if first cell is empty or nothing is required in that spot
        if not (self.first_cell_free(position) or piece_description[0][0] == ZERO):
            print(
                f"This piece {block}, {face} and {rotation} first position is already taken: {position}."
            )
            return False

        # check if cell fits on the board
        if not self.respects_board_limits(position, piece_description):
            print(
                f"This piece {block}, {face} and {rotation} goes out of bounds when starting on position {position}."
            )
            return False

        # check if space is avalaible
        if not self.space_is_available(position, piece_description):
            print(
                f"There is no place for {block}, {face} and {rotation} starting on position {position}."
            )
            return False
        # check if path is broken

        # puts piece
        self.set_piece(block, piece_description, position)
        # self.matrix[] = 1

    def initialise(self, start_map: list[tuple]) -> None:
        """puts first blocks in"""

        for piece in start_map:
            self.add_piece(piece)
            # self.set_path()
            # print_board(self.path)

        self.set_path()
        # print_board(self.path)

    def set_path(self) -> None:
        """transforms symbols"""
        # for width in range(self.width):
        #     for height in range(self.height):
        #         self.path[height,width]=char_dct[self.matrix[height,width]]
        self.path = np.array(
            [
                [char_dct[self.matrix[height, width]] for width in range(self.width)]
                for height in range(self.height)
            ]
        )
