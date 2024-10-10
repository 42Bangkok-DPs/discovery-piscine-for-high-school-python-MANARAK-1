def print_chess_board(king_position, white_pieces):
    # Create an 8x8 chessboard with dots for empty spaces
    board = [["." for _ in range(8)] for _ in range(8)]
    
    # Place the black king on the board
    board[king_position[0]][king_position[1]] = "K"

    # Place white pieces on the board
    for piece in white_pieces:
        row, col = piece['position']
        board[row][col] = piece['type'][0].upper()  # First letter as representation

    # Print the chessboard with swapped letters and numbers
    print("  h g f e d c b a")
    for i in range(8):
        print(8 - i, " ".join(board[i]))  # Rows numbered from 8 to 1
    print()

def is_in_check(position, white_pieces):
    return is_in_checkmate(position, white_pieces)

def is_in_checkmate(king_position, white_pieces):
    row, col = king_position

    # Check if the king is in check by any white piece
    for piece in white_pieces:
        if piece['type'] == 'pawn':
            if (row - 1 == piece['position'][0] and 
                (col - 1 == piece['position'][1] or col + 1 == piece['position'][1])):
                return True
        elif piece['type'] == 'rook':
            if (row == piece['position'][0] or col == piece['position'][1]):
                return True
        elif piece['type'] == 'bishop':
            if abs(row - piece['position'][0]) == abs(col - piece['position'][1]):
                return True
        elif piece['type'] == 'queen':
            if (row == piece['position'][0] or col == piece['position'][1] or
                abs(row - piece['position'][0]) == abs(col - piece['position'][1])):
                return True

    # Check if the king has any legal moves to escape check
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if not is_in_check((new_row, new_col), white_pieces):
                return False

    return True

# Example usage
king_position = (4, 4)  # e5
white_pieces = [
    {'type': 'pawn', 'position': (6, 0)},  # a7
    {'type': 'rook', 'position': (6, 1)},  # b7
    {'type': 'bishop', 'position': (6, 2)},  # c7
    {'type': 'queen', 'position': (6, 3)}   # d7
]

# Print the chess board
print_chess_board(king_position, white_pieces)

# Check and output if black king is in checkmate
if is_in_checkmate(king_position, white_pieces):
    print("Black King is in checkmate!")
else:
    print("Black King is not in checkmate.")
    
#1.create a chess board that has only 1 king
#2.King is the only one who is on black team
#3.white team has pawn, rook, bishop, and queen
#4.this code only need to check if the king from black team got checkmate by any pieces from white teams
#5.make a chess board into table
