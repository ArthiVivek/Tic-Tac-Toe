import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
    
    return min_value <= value <= max_value
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
    
def game_board_full (game_board):
    """ (str) -> bool
    
    Ensure the game_board contains no empty spaces.
    
    >>> game_board_full ('xoxoxoxxo')
    True
    >>> game_board_full ('xoxo----oxox----')
    False
    """
    
    return EMPTY not in game_board

def get_board_size (game_board):
    """ (str) -> int
    
    Precondition: The gameboard size is a perfect square.
    
    Determine the length of each side of the square game_board.
    
    >>> get_board_size ('xoxo')
    2
    >>> get_board_size ('xox---oxo')
    3
    """
    
    return int (math.sqrt (len (game_board)))
    
def make_empty_board (board_size):
    """ (int) -> str
    
    Precondition: 1 <= board_size <= 9
    
    Return a string to represent the empty board of size board_size.
    
    >>> make_empty_board (1)
        '-'
    >>> make_empty_board (4)
    '----------------')
    """
    
    return (board_size ** 2) * EMPTY

def get_position (row_index, col_index, board_size):
    """ (int, int, int) -> int
    
    Precondition: The row_index and col_index are valid values that correspond 
    with the board_size.
    
    Return the index of the string game_board of size board_size that 
    corresponds to the value of the cell represented by col_index and row_index.
    
    >>> get_position (1, 2, 3)
    1
    >>> get_position (3, 3, 4)
    10
    """
    
    return (row_index - 1) * board_size + col_index -1
    
def make_move (char, row_index, col_index, game_board):
    """ (str, int, int, game_board) -> str
    
    Return the game board with char in place of the empty spot on the game_board
    that corresponds to the cell represented by row_index and col_index)
    
    >>> make_move ('X', 1, 1, '---------')
    'X--------'
    >>> make_move ('O', 4, 2, '-----X----------')
    '-----X------O---'
    """
    
    new_game_board = ""
    
    index = get_position (row_index, col_index, get_board_size (game_board))
    
    iteration = 0
    for C in game_board:
        if iteration == index:
            new_game_board += char
        else:
            new_game_board += C
        iteration = iteration + 1
    return new_game_board
            
def extract_line (game_board, direction, row_column_num):
    """ (str, str, int) -> str
    
    Return the characters on the game_board that are in the direction given,
     with the specified row_column_num.
     
     >>> extract_line ('xo--oxxo-o-xx-o-', 'up_diagonal', 6)
     'xox-'
     >>> extract_line ('xoxoxoxox', 'across', 2)
     'oxo'
     >>> extract_line ('xo--oxxo-o-xx-o-', 'down_diagonal', 1)
     'xx--'
     >>> extract_line ('xox---oxo', 'down', 2)
     'o-x'
     """
    
    section = ""
    size = get_board_size (game_board)
    
    if direction == 'down_diagonal':
        section = game_board [::size + 1]
    elif direction == 'up_diagonal':
        if size == 1:
            section = game_board
        else:
            section = game_board [- size :: 1 - size]
    elif direction == 'across':
        index = get_position (row_column_num, 1, get_board_size (game_board))
        section = game_board [index:index + size]
    elif direction == 'down':
        index = get_position (1, row_column_num, get_board_size (game_board))
        section = game_board [index::size]
    return section [:size]


    
