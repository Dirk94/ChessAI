import chess, pieces, ai

board = chess.Board()
print board.to_string()

moves = board.get_possible_moves(pieces.Piece.WHITE)
move = moves[0]
print "Performing " + move.to_string()

board.perform_move(move)
print board.to_string()

print "Score: " + str(ai.Heuristics.evaluate(board))
