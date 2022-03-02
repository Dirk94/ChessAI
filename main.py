import requests
import board, pieces, ai

# Returns a move object based on the users input. Does not check if the move is valid.
def get_user_move():
    print("Example Move: A2 A4")
    move_str = input("Your Move: ")
    move_str = move_str.replace(" ", "")

    try:
        xfrom = letter_to_xpos(move_str[0:1])
        yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
        xto = letter_to_xpos(move_str[2:3])
        yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
        return ai.Move(xfrom, yfrom, xto, yto, False)
    except ValueError:
        print("Invalid format. Example: A2 A4")
        return get_user_move()

# Returns a valid move based on the users input.
def get_valid_user_move(board):
    while True:
        move = get_user_move()
        valid = False
        possible_moves = board.get_possible_moves(pieces.Piece.WHITE)
        # No possible moves
        if (not possible_moves):
            return 0

        for possible_move in possible_moves:
            if (move.equals(possible_move)):
                move.castling_move = possible_move.castling_move
                valid = True
                break

        if (valid):
            break
        else:
            print("Invalid move.")
    return move

# Converts a letter (A-H) to the x position on the chess board.
def letter_to_xpos(letter):
    letter = letter.upper()
    if letter == 'A':
        return 0
    if letter == 'B':
        return 1
    if letter == 'C':
        return 2
    if letter == 'D':
        return 3
    if letter == 'E':
        return 4
    if letter == 'F':
        return 5
    if letter == 'G':
        return 6
    if letter == 'H':
        return 7

    raise ValueError("Invalid letter.")

def read_board(filename):
    board_matrix = []
    with open(filename,'r') as f:
        for line in f:
            line_matrix = []
            for word in line.split():
                line_matrix.append(word)
            board_matrix.append(line_matrix)

    return board_matrix

WEBSERVER = "http://127.0.0.1:5000"
def read_board_network():
    resp = requests.get(WEBSERVER)
    text = resp.content.decode("latin-1").strip().split("\n")
    board = [i.split() for i in text]
    return board

def convert_text_to_board(filename, board):
    if filename is None:
        tmp_board = read_board_network()
    else:
        tmp_board = read_board(filename)

    new_board = []
    for j in range(len(tmp_board)):
        row = []
        for i in range(len(tmp_board[0])):
            if tmp_board[i][j] == "BR":
                row.append(pieces.Rook(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WR":
                row.append(pieces.Rook(i, j, pieces.Piece.WHITE))
            elif tmp_board[i][j] == "BN":
                row.append(pieces.Knight(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WN":
                row.append(pieces.Knight(i, j, pieces.Piece.WHITE))
            elif tmp_board[i][j] == "BB":
                row.append(pieces.Bishop(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WB":
                row.append(pieces.Bishop(i, j, pieces.Piece.WHITE))
            elif tmp_board[i][j] == "BQ":
                row.append(pieces.Queen(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WQ":
                row.append(pieces.Queen(i, j, pieces.Piece.WHITE))
            elif tmp_board[i][j] == "BK":
                row.append(pieces.King(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WK":
                row.append(pieces.King(i, j, pieces.Piece.WHITE))
            elif tmp_board[i][j] == "BP":
                row.append(pieces.Pawn(i, j, pieces.Piece.BLACK))
            elif tmp_board[i][j] == "WP":
                row.append(pieces.Pawn(i, j, pieces.Piece.WHITE))
            else:
                row.append(0)
        new_board.append(row)
    
    board.chesspieces = new_board
    return board

#
# Entry point.
#
board = board.Board.new()
print(board.to_string())

while True:
    move = board.get_possible_moves(pieces.Piece.WHITE)
    if (move == 0):
        if (board.is_check(pieces.Piece.WHITE)):
            print("Checkmate. Black Wins.")
            break
        else:
            print("Stalemate.")
            break
    
    consoleInput = input()
    while consoleInput != "Next":
        consoleInput = input()

    # board = convert_text_to_board("input.txt", board)
    board = convert_text_to_board(None, board)
    print(board.to_string())

    ai_move = ai.AI.get_ai_move(board, [])
    if (ai_move == 0):
        if (board.is_check(pieces.Piece.BLACK)):
            print("Checkmate. White wins.")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(ai_move)
    print("AI move: " + ai_move.to_string())
    print(board.to_string())
