import pieces, ai

class Board:

    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        self.init_default()

    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.pieces[x][y]
                if (piece != 0):
                    if (piece.color == color):
                        moves += piece.get_possible_moves(self)
        return moves

    def perform_move(self, move):
        piece = self.pieces[move.xfrom][move.yfrom]
        self.pieces[move.xto][move.yto] = piece
        self.pieces[move.xfrom][move.yfrom] = 0

    # Returns piece at given position or 0 if: No piece or out of bounds.
    def get_piece(self, x, y):
        if (not self.in_bounds(x, y)):
            return 0

        return self.pieces[x][y]

    def in_bounds(self, x, y):
        return (x >= 0 and y >= 0 and x < Board.WIDTH and y < Board.HEIGHT)

    # Creates the chess pieces at their default position.
    def init_default(self):
        # Create pawns.
        for y in range(Board.WIDTH):
            self.pieces[1][y] = pieces.Pawn(1, y, pieces.Piece.WHITE)
            self.pieces[Board.WIDTH-2][y] = pieces.Pawn(Board.WIDTH-2, y, pieces.Piece.BLACK)

        # Create rooks.
        self.pieces[0][0] = pieces.Rook(0, 0, pieces.Piece.WHITE)
        self.pieces[0][Board.HEIGHT-1] = pieces.Rook(0, Board.HEIGHT-1, pieces.Piece.WHITE)
        self.pieces[Board.WIDTH-1][0] = pieces.Rook(Board.WIDTH-1, 0, pieces.Piece.BLACK)
        self.pieces[Board.WIDTH-1][Board.HEIGHT-1] = pieces.Rook(Board.WIDTH-1, Board.HEIGHT-1, pieces.Piece.BLACK)

        # Create Knights.
        self.pieces[0][1] = pieces.Knight(0, 1, pieces.Piece.WHITE)
        self.pieces[0][Board.HEIGHT-2] = pieces.Knight(0, Board.HEIGHT-2, pieces.Piece.WHITE)
        self.pieces[Board.WIDTH-1][1] = pieces.Knight(Board.WIDTH-1, 1, pieces.Piece.BLACK)
        self.pieces[Board.WIDTH-1][Board.HEIGHT-2] = pieces.Knight(Board.WIDTH-1, Board.HEIGHT-2, pieces.Piece.BLACK)

        # Create Bishops.
        self.pieces[0][2] = pieces.Bishop(0, 2, pieces.Piece.WHITE)
        self.pieces[0][Board.HEIGHT-3] = pieces.Bishop(0, Board.HEIGHT-3, pieces.Piece.WHITE)
        self.pieces[Board.WIDTH-1][2] = pieces.Bishop(Board.WIDTH-1, 2, pieces.Piece.BLACK)
        self.pieces[Board.WIDTH-1][Board.HEIGHT-3] = pieces.Bishop(Board.WIDTH-1, Board.HEIGHT-3, pieces.Piece.BLACK)

        # Create King & Queen.
        self.pieces[0][3] = pieces.King(0, 3, pieces.Piece.WHITE)
        self.pieces[0][Board.HEIGHT-4] = pieces.Queen(0, Board.HEIGHT-4, pieces.Piece.WHITE)
        self.pieces[Board.WIDTH-1][3] = pieces.King(Board.WIDTH-1, 3, pieces.Piece.BLACK)
        self.pieces[Board.WIDTH-1][Board.HEIGHT-4] = pieces.Queen(Board.WIDTH-1, Board.HEIGHT-4, pieces.Piece.BLACK)

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
