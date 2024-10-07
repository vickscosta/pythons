'''game'''

import numpy as np
from config import BOARD_HEIGHT, BOARD_WIDTH, EMPTY_CHAR, piece_dct
from start_position import original_piece_map
from board_class import BoardClass, print_board


def build_list_of_pieces(block: str) -> list:
    """makes a list of hyphoteses to test"""

    final_list = []

    for key1, _ in piece_dct[block].items():
        for key2, _ in piece_dct[block][key1].items():

            final_list.append((key1, key2))

    return final_list


def main() -> None:
    """does the main thing"""

    # Initialisation
    board = BoardClass(BOARD_WIDTH, BOARD_HEIGHT)
    board.initialise(original_piece_map)
    print_board(board.path)

    # Solver
    full_bag = list(piece_dct.keys())
    piece_bag = [piece[0] for piece in original_piece_map]
    candidate_bag = [piece for piece in full_bag if piece not in piece_bag]
    print("Candidate pieces:", candidate_bag, "\n")

    empty_list = np.argwhere(board.matrix == EMPTY_CHAR)

    for block in candidate_bag:

        pieces_to_test = build_list_of_pieces(block)

        for piece in pieces_to_test:

            for position in empty_list:

                built_piece = tuple((block, piece[0], piece[1], tuple((position[0],position[1]))))

                result = board.add_piece(built_piece)

                # board.add_piece(piece)

                # ("!", "face0", "rotation1", (0, 1)),

if __name__ == "__main__":
    main()
