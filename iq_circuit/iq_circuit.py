'''game'''

# from config import char_dct
from config import BOARD_HEIGHT, BOARD_WIDTH, piece_dct
from start_position import original_piece_map, target_path
from board_class import BoardClass, print_board


def main() -> None:
    """does the main thing"""

    board = BoardClass(BOARD_WIDTH, BOARD_HEIGHT)
    board.initialise(original_piece_map)
    print_board(board.path)
    print_board(board.matrix)
    print_board(board.piece_map)



if __name__ == "__main__":
    main()
