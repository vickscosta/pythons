'''class for board operations'''

import numpy as np
from config import EMPTY_CHAR

class BoardClass:
    '''creates and manages boards'''

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.matrix = np.full((height, width), EMPTY_CHAR, dtype='str')

    def __str__(self) -> str:
        return '\n' + '\n'.join(' '.join(row) for row in self.matrix) + '\n'
