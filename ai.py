import chess, pieces

class Heuristics:

    @staticmethod
    def evaluate(board):
        material = Heuristics.get_material_score(board)

        return material


    @staticmethod
    def get_material_score(board):
        white = 0
        black = 0
        for x in range(chess.Board.WIDTH):
            for y in range(chess.Board.HEIGHT):
                piece = board.pieces[x][y]
                if (piece != 0):
                    if (piece.color == pieces.Piece.WHITE):
                        white += piece.value
                    else:
                        black += piece.value

        return white - black


class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto

    def to_string(self):
        return "(" + str(self.xfrom) + ", " + str(self.yfrom) + ") -> (" + str(self.xto) + ", " + str(self.yto) + ")"
