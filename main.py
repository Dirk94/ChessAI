import board, pieces, ai

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Returns a move object based on the users input. Does not check if the move is valid.
def get_user_move():
    print("Example Move: A2 A4")
    player_move = input("Your Move: ").split()

    try:
        _from = player_move[0]
        _to = player_move[1]
        
        xfrom = letter_to_xpos(_from[0])
        yfrom = 8 - int(_from[1]) # The board is drawn "upside down", so flip the y coordinate.
        xto = letter_to_xpos(_to[0])
        yto = 8 - int(_to[1]) # The board is drawn "upside down", so flip the y coordinate.
        
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

def letter_to_xpos(letter):
    return chars.index(letter)

#
# Entry point.
#
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