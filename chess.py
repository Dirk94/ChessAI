class Board:

    # The constants defining the piece type.
    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]

        for y in range(Board.WIDTH):
            self.pieces[1][y] = Piece(Piece.WHITE, Piece.PAWN)

    def to_string(self):
        string = ""
        for y in range(Board.HEIGHT):
            for x in range(Board.WIDTH):
                piece = self.pieces[x][y]
                if piece != 0:
                    string += piece.to_string()
                else:
                    string += "-- "
            string += "\n"
        return string






class Piece:

    # The constants defining black and white.
    WHITE = "W"
    BLACK = "B"

    # The constants defining the piece type.
    PAWN   = "P"
    ROOK   = "R"
    KNIGHT = "N"
    BISHOP = "B"
    QUEEN  = "Q"
    KING   = "K"

    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def to_string(self):
        return self.color + self.piece_type + " "
