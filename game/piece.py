import pygame
class Piece:
    box_size = None
    def __init__(self, image_address, type, color):
        self.image = pygame.image.load(image_address)
        self.image = pygame.transform.scale(self.image, (self.box_size, self.box_size)) 
        self.type = type
        self.color = color

class Pawn(Piece):    
    def __init__(self, image_address, type, color, last_pos=None):
        super().__init__(image_address, type, color)
        self.last_pos = last_pos
    
    def last_pos(self, row, col):
        self.last_pos = row, col

class Rook(Piece):

    def __init__(self, image_address, type, color):
        super().__init__(image_address, type, color)
        self.moved = False
    
    def move_made(self):
        self.moved = True

class Knight(Piece):
    def __init__(self, image_address, type, color):
        super().__init__(image_address, type, color)

class Bishop(Piece):
    def __init__(self, image_address, type, color):
        super().__init__(image_address, type, color)

class Queen(Piece):
    def __init__(self, image_address, type, color):
        super().__init__(image_address, type, color)

class King(Piece):

    def __init__(self, image_address, type, color):
        super().__init__(image_address, type, color)
        self.moved = False
    
    def move_made(self):
        self.moved = True
