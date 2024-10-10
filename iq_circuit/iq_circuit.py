"""game"""

import sys
import copy
from config import BOARD_HEIGHT, BOARD_WIDTH, piece_dct
from start_position import original_piece_map
from board_class import BoardClass, print_board

def solver_init() -> list[str]:
    '''initializes the solver'''

    full_bag = list(piece_dct.keys())
    piece_bag = [piece[0] for piece in original_piece_map]
    bag = [piece for piece in full_bag if piece not in piece_bag]
    # print("Candidate pieces:", candidate_bag, "\n")
    return bag

def solver(bag: list[str], my_board: BoardClass) -> None:
    """solves it"""

    hyp_board = copy.deepcopy(my_board)
    hyp_bag = copy.deepcopy(bag)

    while hyp_bag:
        block = hyp_bag.pop(0)
        pieces_to_test = [(key1, key2)
                          for key1 in piece_dct[block]
                          for key2 in piece_dct[block][key1]]

        while pieces_to_test:
            piece = pieces_to_test.pop(0)
            empty_list = [[i, j] for i in range(4) for j in range(8)]

            while empty_list:
                position = empty_list.pop(0)
                built_piece = tuple(
                    (block, piece[0], piece[1],
                    tuple((int(position[0]), int(position[1])))))

                sucess = hyp_board.add_piece(built_piece)
                # print(".", end="")
                if sucess:
                    # print(f"{block} added to position {position}")
                    # print_board(hyp_board.path)
                    solver(hyp_bag, hyp_board)
                    if not hyp_bag:
                        print_board(hyp_board.path)
                        print_board(hyp_board.piece_map)
                        sys.exit() # END SOLUTION
                    hyp_board.remove_piece(built_piece)

        # print('Nothing fits with', block)
        return # we are here if nothing fits

def main() -> None:
    """does the main thing"""

    # Board initialisation
    board = BoardClass(BOARD_WIDTH, BOARD_HEIGHT)
    board.initialise(original_piece_map)
    print_board(board.path)

    # Solver init
    candidate_bag = solver_init()

    # Solver
    solver(candidate_bag, board)

    # Final print
    print("\n")
    print_board(board.path)


if __name__ == "__main__":
    main()
