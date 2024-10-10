#!/usr/bin/env python3

from checkmate import checkmate

def main():
    print("Make your own chess board!")
    print("Use (K) for Black King")
    print("Use (P) for White Pawn")
    print("Use (R) for White Rook")
    print("Use (B) for White Bishop")
    print("Use (Q) for White Queen")
    print("Use dots (.) for empty spaces.")
    print("Each row should be on a new line.")
    print("Press enter first then type (done) when you are finished entering the board.")

    # Capture the chessboard input from the user
    board = []
    while True:
        row = input("Enter row: ")
        if row.lower() == "done":
            break
        if row:  # Only add non-empty rows
            board.append(row)

    # Convert the list of rows into a string
    board_string = "\n".join(board)

    # Run the checkmate check
    checkmate(board_string)

if __name__ == "__main__":
    main()
