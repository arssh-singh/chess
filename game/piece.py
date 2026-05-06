import pygame
class Piece:
    box_size = None
    def __init__(self, image_address,  color):
        self.image = pygame.image.load(image_address)
        self.image = pygame.transform.scale(self.image, (self.box_size, self.box_size)) 
        self.color = color

class Pawn(Piece):    
    type = "pawn"
    def __init__(self, image_address, color, last_pos=None):
        super().__init__(image_address, color)
        self.last_pos = last_pos
    
    def last_pos(self, row, col):
        self.last_pos = row, col

class Rook(Piece):
    type = "rook"
    def __init__(self, image_address, color):
        super().__init__(image_address, color)
        self.moved = False
    
    def move_made(self):
        self.moved = True

class Knight(Piece):
    type = "knight"
    def __init__(self, image_address, color):
        super().__init__(image_address, color)

class Bishop(Piece):
    type = "bishop"
    def __init__(self, image_address, color):
        super().__init__(image_address, color)

class Queen(Piece):
    type = "queen"
    def __init__(self, image_address, color):
        super().__init__(image_address, color)

class King(Piece):
    type = "king"
    def __init__(self, image_address, color):
        super().__init__(image_address, color)
        self.moved = False
    
    def move_made(self):
        self.moved = True
