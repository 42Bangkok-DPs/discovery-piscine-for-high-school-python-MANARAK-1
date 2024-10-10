#!/usr/bin/env python3

class ChessPiece:
    def __init__(self, position):
        self.position = position

    def is_valid_move(self, target_position):
        raise NotImplementedError("Subclasses must implement this method")

    def position_to_coordinates(self):
        """Convert the piece's own string position like 'a1' to (row, col) tuple."""
        col = ord(self.position[0].lower()) - ord('a')
        row = 8 - int(self.position[1])
        return row, col

    @staticmethod
    def target_position_to_coordinates(position):
        """Convert any string position like 'a1' to (row, col) tuple."""
        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        return row, col

# Helper function to convert coordinates to a chessboard position string
def coordinates_to_position(row, col):
    """Convert (row, col) tuple back to string position like 'a1'."""
    return f"{chr(col + ord('a'))}{8 - row}"

class King(ChessPiece):
    def is_valid_move(self, target_position):
        king_row, king_col = self.position_to_coordinates()
        target_row, target_col = ChessPiece.target_position_to_coordinates(target_position)

        row_diff = abs(king_row - target_row)
        col_diff = abs(king_col - target_col)
        return max(row_diff, col_diff) == 1

class Pawn(ChessPiece):
    def is_valid_move(self, target_position):
        # Assuming white pawns are moving "up" the board (decreasing row number)
        pawn_row, pawn_col = self.position_to_coordinates()
        target_row, target_col = ChessPiece.target_position_to_coordinates(target_position)
        return target_row == pawn_row - 1 and abs(target_col - pawn_col) == 1

class Rook(ChessPiece):
    def is_valid_move(self, target_position):
        rook_row, rook_col = self.position_to_coordinates()
        target_row, target_col = ChessPiece.target_position_to_coordinates(target_position)
        return rook_row == target_row or rook_col == target_col

class Bishop(ChessPiece):
    def is_valid_move(self, target_position):
        bishop_row, bishop_col = self.position_to_coordinates()
        target_row, target_col = ChessPiece.target_position_to_coordinates(target_position)
        row_diff = abs(bishop_row - target_row)
        col_diff = abs(bishop_col - target_col)
        return row_diff == col_diff

class Queen(ChessPiece):
    def is_valid_move(self, target_position):
        queen_row, queen_col = self.position_to_coordinates()
        target_row, target_col = ChessPiece.target_position_to_coordinates(target_position)
        row_diff = abs(queen_row - target_row)
        col_diff = abs(queen_col - target_col)
        return queen_row == target_row or queen_col == target_col or row_diff == col_diff

def is_checkmate(king, white_pieces):
    king_row, king_col = king.position_to_coordinates()

    # Get all potential moves of the king
    possible_moves = [
        coordinates_to_position(king_row + i, king_col + j)
        for i in range(-1, 2) for j in range(-1, 2)
        if (i, j) != (0, 0) and 0 <= king_row + i <= 7 and 0 <= king_col + j <= 7
    ]

    # Check if each move is safe (not under attack by any white piece)
    for move in possible_moves:
        if not any(piece.is_valid_move(move) for piece in white_pieces):
            return False  # King can escape to at least one square

    # If no safe moves are found, the king is in checkmate
    return True

def checkmate(board_string):
    """This function parses the board string and checks if the black king is in checkmate."""
    # Parse the board into a 2D list
    board = board_string.splitlines()

    # Locate the black king and white pieces
    black_king = None
    white_pieces = []

    # Define a dictionary to convert board coordinates to chess positions (e.g., (0, 0) -> "a8")
    def board_coordinates_to_position(row, col):
        return f"{chr(col + ord('a'))}{8 - row}"

    # Parse the board
    for row in range(4):  # 4 rows
        for col in range(4):  # 4 columns
            piece = board[row][col]
            position = board_coordinates_to_position(row, col)
            if piece == 'K':
                black_king = King(position)
            elif piece == 'P':
                white_pieces.append(Pawn(position))
            elif piece == 'R':
                white_pieces.append(Rook(position))
            elif piece == 'B':
                white_pieces.append(Bishop(position))
            elif piece == 'Q':
                white_pieces.append(Queen(position))

    # Check if the black king is in checkmate
    if black_king:
        if is_checkmate(black_king, white_pieces):
            print("Success")
        else:
            print("Fail")
    else:
        print("Error")
    
#1.create a chess board that has only 1 king
#2.King is the only one who is on black team
#3.white team has pawn, rook, bishop, and queen
#4.this code only need to check if the king from black team got checkmate by any pieces from white teams
#5.make a chess board into table
