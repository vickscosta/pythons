"""game"""

import copy
import numpy as np
from config import BOARD_HEIGHT, BOARD_WIDTH, EMPTY_CHAR, piece_dct
from start_position import original_piece_map
from board_class import BoardClass, print_board


def build_list_of_pieces(block: str) -> list:
    """makes a list of hyphoteses to test"""
    return [(key1, key2) for key1 in piece_dct[block] for key2 in piece_dct[block][key1]]

def solver_init() -> list[str]:
    '''initializes the solver'''

    full_bag = list(piece_dct.keys())
    piece_bag = [piece[0] for piece in original_piece_map]
    bag = [piece for piece in full_bag if piece not in piece_bag]
    # print("Candidate pieces:", candidate_bag, "\n")
    return bag

def loop_pieces_to_test(test_bag:list, brick:str, mem: list, hbag:list, hboard:list, hempty_list:list) -> tuple:
    """deals with these loops"""

# TODO
#    when all the pieces were tried and nothig is good, that means that the previous solution was not good

    for piece in test_bag:
        for position in hempty_list:
            built_piece = tuple(
                (brick,
                piece[0],
                piece[1],
                tuple((int(position[0]), int(position[1]))))                )

            if build_list_of_pieces in mem:
                continue

            sucess = hboard.add_piece(built_piece)
            if sucess:
                mem.append(built_piece)
                hboard.set_path()
                print(f"{brick} added to position {position}")
                hbag.remove(brick)
                hempty_list = np.argwhere(hboard.matrix == EMPTY_CHAR)
                return sucess, mem, hbag, hboard, hempty_list

    return sucess, mem, hbag, hboard, hempty_list

def solver(bag: list[str], my_board: BoardClass) -> None:
    """solves it"""

    empty_list = np.argwhere(my_board.matrix == EMPTY_CHAR)

    hyp_board = copy.deepcopy(my_board)
    hyp_empty_list = copy.deepcopy(empty_list)
    hyp_bag = copy.deepcopy(bag)

    memory = []

    counter=0
    while np.any(hyp_empty_list) or counter==10:
        counter += 1
        for block in hyp_bag:
            pieces_to_test = build_list_of_pieces(block)
            status = False

            status, memory, hyp_bag, hyp_board, hyp_empty_list = loop_pieces_to_test(pieces_to_test, block, memory, hyp_bag, hyp_board, hyp_empty_list)
            if status:
                continue

            # for piece in pieces_to_test:
            #     for position in hyp_empty_list:
            #         built_piece = tuple(
            #             (block,
            #             piece[0],
            #             piece[1],
            #             tuple((int(position[0]), int(position[1]))))                )

            #         status = hyp_board.add_piece(built_piece)
            #         if status:
            #             hyp_board.set_path()
            #             print(f"{block} added to position {position}")
            #             hyp_bag.remove(block)
            #             hyp_empty_list = np.argwhere(hyp_board.matrix == EMPTY_CHAR)
            #             break
    print('hello')



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
