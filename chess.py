import pygame
from movement_check import *
from king_logic import *

#creating pygame window
pygame.init()
screen_h = 750
screen_w = 1200
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Drawing Shapes")

# board placement
#size of one box on board
box_size = 87
top = (screen_h-(box_size*8))/2
right = (screen_w-(box_size*8))/2
board = [[None for _ in range(8)]for _ in range(8)]

#Creating a Piece Class to store data of pieces
class Piece:
    def __init__(self, image_address, type, color):
        self.image = pygame.image.load(image_address)
        self.image = pygame.transform.scale(self.image, (box_size, box_size)) 
        self.type = type
        self.color = color

#Creating Game Class 
class Game:
    def __init__(self, board):
        self.board = board
        self.turn = "white"
        self.selected_piece = None
        self.old_pos = None
        self.last_move = None
    
    def is_valid_move(self, selected_piece, old_pos, row, col):
        if selected_piece.type == "pawn":
            check_pawn = check_pawn_movement(self.board, (old_pos), (row, col), selected_piece)
            if check_pawn==True or check_pawn==False:
                allow_pawn=check_pawn
            else:
                val, p_row, p_col = check_pawn
                if val == True:
                    allow_pawn=True
                    self.board[p_row][p_col] = None
                    print(p_row, p_col)
                else:
                    allow_pawn=False

            if allow_pawn==True:
                return True
        if selected_piece.type == "rook":
            return check_rook_movement(self.board, (old_pos), (row, col), selected_piece)
        if selected_piece.type == "knight":
            return check_knight_movement((old_pos), (row, col), selected_piece)                                
        if selected_piece.type == "bishop":
            return check_bishop_movement(self.board, (old_pos), (row, col), selected_piece)                                    
        if selected_piece.type == "queen":
            return check_queen_movement(self.board, (old_pos), (row, col), selected_piece)                                    
        if selected_piece.type == "king":
            return check_king_movement((old_pos), (row, col), selected_piece)
    
    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
    
    def simulate_move(self, selected_piece, old_pos, row, col):
        board_copy = [row[:] for row in self.board]
        old_row, old_col = old_pos
        piece = board[old_row][old_col]
        board_copy[old_row][old_col] = None
        board_copy[row][col] = piece

        return board_copy
    
    def is_legal_move(self, selected_piece, old_pos, row, col):
        #simulating move
        test_board = self.simulate_move(selected_piece, old_pos, row, col)
        king_pos = find_king(test_board, selected_piece.color)

        if not is_king_safe(test_board, king_pos, selected_piece.color):
            print("Danger To King")
            return False
        
        return True
        

# placing white pieces on board
board[0][0] = Piece("pieces/rook.png", "rook", "white")
board[0][1] = Piece("pieces/knight.png", "knight", "white")
board[0][2] = Piece("pieces/bishop.png", "bishop", "white")
board[0][3] = Piece("pieces/king.png", "king", "white")
board[0][4] = Piece("pieces/queen.png", "queen", "white")
board[0][5] = Piece("pieces/bishop.png", "bishop", "white")
board[0][6] = Piece("pieces/knight.png", "knight", "white")
board[0][7] = Piece("pieces/rook.png", "rook", "white")
board[1][0] = Piece("pieces/pawn.png", "pawn", "white")
board[1][1] = Piece("pieces/pawn.png", "pawn", "white")
board[1][2] = Piece("pieces/pawn.png", "pawn", "white")
board[1][3] = Piece("pieces/pawn.png", "pawn", "white")
board[1][4] = Piece("pieces/pawn.png", "pawn", "white")
board[1][5] = Piece("pieces/pawn.png", "pawn", "white")
board[1][6] = Piece("pieces/pawn.png", "pawn", "white")
board[1][7] = Piece("pieces/pawn.png", "pawn", "white")

# placing black pieces on board
board[7][0] = Piece("pieces/black/rook.png", "rook", "black")
board[7][1] = Piece("pieces/black/knight.png", "knight", "black")
board[7][2] = Piece("pieces/black/bishop.png", "bishop", "black")
board[7][3] = Piece("pieces/black/king.png", "king", "black")
board[7][4] = Piece("pieces/black/queen.png", "queen", "black")
board[7][5] = Piece("pieces/black/bishop.png", "bishop", "black")
board[7][6] = Piece("pieces/black/knight.png", "knight", "black")
board[7][7] = Piece("pieces/black/rook.png", "rook", "black")
board[6][0] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][1] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][2] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][3] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][4] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][5] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][6] = Piece("pieces/black/pawn.png", "pawn", "black")
board[6][7] = Piece("pieces/black/pawn.png", "pawn", "black")

#creating chess game
chess=Game(board)

running = True
selected_piece = None
old_pos = None
chess.turn = "white"
font = pygame.font.Font(None, 36)

#creating while loop for updating game
while running:
    #creating for loop to detect events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #detecting mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:        
            #getting mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            #getting box coords according to mouse position
            col = int((mouse_x-right)//box_size)
            row = int((mouse_y-top)//box_size)

            #checking if box is available on board
            if 0 <= row <= 7 and 0 <= col <= 7:
                #if mouse is on a piece and no other piece is selected, also piece is of color with the turn. Select that piece.
                if selected_piece is None:
                    if board[row][col] is not None and board[row][col].color == chess.turn:
                        selected_piece = board[row][col]
                        old_pos = row, col                
                else:
                    #if mouse is on a piece and already selected piece is of same color the select the piece mouse is on
                    if board[row][col] is not None and board[row][col].color == selected_piece.color:
                        selected_piece = board[row][col]
                        old_pos = row, col
                    
                    #if mouse is on a piece and already selected piece is not of same color then capture the piece if possible
                    else:        
                        #checking if movement is valid and legal             
                        movement = chess.is_valid_move(selected_piece, old_pos, row, col) and chess.is_legal_move(selected_piece, old_pos, row, col)
                        if movement:                            
                            old_row, old_col = old_pos
                            #setting old position of piece to none
                            board[old_row][old_col] = None
                            #putting piece on new positions
                            board[row][col]=selected_piece

                            selected_piece = None
                            old_pos = None

                            #changing turn                            
                            chess.change_turn()

    
    #filling background with color
    screen.fill((121, 56, 27))

    #making board
    for row in range(0,8):
        for col in range(0,8):
            if (row+col)%2 == 0:
                color = (240, 217, 181)
            else:
                color = (181, 136, 99)          
            pygame.draw.rect(screen, color, (right+col*box_size, top+row*box_size, box_size, box_size))

    #adding pieces to board
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                y = top+(box_size*row)
                x = right+(box_size*col)
                screen.blit(piece.image, (x, y))

    if old_pos:
        sel_row, sel_col = old_pos
        pygame.draw.rect(screen, (0,255,0), (right+sel_col*box_size, top+sel_row*box_size, box_size, box_size), 4)

    text = font.render(f"Turn: {chess.turn.upper()}", True, (255, 255, 255))
    screen.blit(text, ((right/2)-(text.get_width()/2), top))


    pygame.display.update()

pygame.quit()