import board, pieces, ai

# Returns a move object based on the users input. Does not check if the move is valid.
def get_user_move():
    print("Format: xfrom,yfrom xto,yto")
    move_str = input("Your Move: ")
    move_str = move_str.replace(" ", "")

    try:
        xfrom = int(move_str[0:1])
        yfrom = int(move_str[2:3])
        xto = int(move_str[3:4])
        yto = int(move_str[5:6])
    except ValueError:
        print("Invalid syntax. Format: xfrom,yfrom xto,yto")
        return get_user_move()

    return ai.Move(xfrom, yfrom, xto, yto, False)

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

# Entry point.
board = board.Board.new()
print(board.to_string())

while True:
    move = get_valid_user_move(board)
    if (move == 0):
        if (board.is_check(pieces.Piece.WHITE)):
            print("Checkmate. Black Wins.")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(move)

    print("User move: " + move.to_string())
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
