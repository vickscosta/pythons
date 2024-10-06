'''game'''

# from config import char_dct
from config import BOARD_HEIGHT,BOARD_WIDTH, piece_dct
from board_class import BoardClass


def main()-> None:
    """does the main thing"""

    board = BoardClass(BOARD_WIDTH,BOARD_HEIGHT)
    print(board)

    pass

if __name__ == "__main__":
    main()


