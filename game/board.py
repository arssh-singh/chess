from game.piece import *
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def set(self, row, col, piece):
        self.grid[row][col] = piece

    def setup(self):
        self.set(0,0, Rook("pieces/rook.png", "white"))
        self.set(0,1, Knight("pieces/knight.png", "white"))
        self.set(0,2, Bishop("pieces/bishop.png", "white"))
        self.set(0,3, King("pieces/king.png", "white"))
        self.set(0,4, Queen("pieces/queen.png", "white"))
        self.set(0,5, Bishop("pieces/bishop.png", "white"))
        self.set(0,6, Knight("pieces/knight.png", "white"))
        self.set(0,7, Rook("pieces/rook.png", "white"))
        self.set(1,0, Pawn("pieces/pawn.png",  "white"))
        self.set(1,1, Pawn("pieces/pawn.png", "white"))
        self.set(1,2, Pawn("pieces/pawn.png", "white"))
        self.set(1,3, Pawn("pieces/pawn.png", "white"))
        self.set(1,4, Pawn("pieces/pawn.png", "white"))
        self.set(1,5, Pawn("pieces/pawn.png", "white"))
        self.set(1,6, Pawn("pieces/pawn.png", "white"))
        self.set(1,7, Pawn("pieces/pawn.png", "white"))

        self.set(7,0, Rook("pieces/black/rook.png", "black"))
        self.set(7,1, Knight("pieces/black/knight.png", "black"))
        self.set(7,2, Bishop("pieces/black/bishop.png", "black"))
        self.set(7,3, King("pieces/black/king.png", "black"))
        self.set(7,4, Queen("pieces/black/queen.png", "black"))
        self.set(7,5, Bishop("pieces/black/bishop.png", "black"))
        self.set(7,6, Knight("pieces/black/knight.png", "black"))
        self.set(7,7, Rook("pieces/black/rook.png", "black"))
        self.set(6,0, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,1, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,2, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,3, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,4, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,5, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,6, Pawn("pieces/black/pawn.png", "black"))
        self.set(6,7, Pawn("pieces/black/pawn.png", "black"))

    def get(self, row, col):
        return self.grid[row][col]
    
    def set(self, row, col, piece):
        self.grid[row][col] = piece

    def move(self, old_pos, new_pos):
        piece = self.get(*old_pos)
        self.set(*new_pos, piece)
        self.set(*old_pos, None)
