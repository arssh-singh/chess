import pygame
from movement_check import *
from king_logic import *

pygame.init()
screen_h = 750
screen_w = 1200
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Drawing Shapes")

# board placement
box_size = 87
top = (screen_h-(box_size*8))/2
right = (screen_w-(box_size*8))/2
board = [[None for _ in range(8)]for _ in range(8)]

#drawing pieces
class Piece:
    def __init__(self, image_address, type, color):
        self.image = pygame.image.load(image_address)
        self.image = pygame.transform.scale(self.image, (box_size, box_size)) 
        self.type = type
        self.color = color

#king
# White
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

# Black
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


running = True
selected_piece = None
selected_pos = None
color_to_move = "white"
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checking if king is in danger
            king_pos=None
            if color_to_move == "white":
                king_pos = find_king(board, "white")
            else:
                king_pos = find_king(board, "black")
            
            # check_danger(king_pos, board)
            
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = int((mouse_x-right)//box_size)
            row = int((mouse_y-top)//box_size)


            if 0 <= row < 8 and 0 <= col < 8:
                if selected_piece is None:
                    if board[row][col] is not None and board[row][col].color == color_to_move:
                        selected_piece = board[row][col]
                        selected_pos = row, col
                else:
                    if board[row][col] is not None and board[row][col].color == selected_piece.color:
                        selected_piece = board[row][col]
                        selected_pos = row, col
                    else: 
                        movement = False
                        if selected_piece.type == "pawn":
                            check_pawn = check_pawn_movement(board, (selected_pos), (row, col), selected_piece)
                            if check_pawn==True or check_pawn==False:
                                allow_pawn=check_pawn
                            else:
                                val, p_row, p_col = check_pawn
                                if val == True:
                                    allow_pawn=True
                                    board[p_row][p_col] = None
                                    print(p_row, p_col)
                                else:
                                    allow_pawn=False

                            if allow_pawn==True:
                                movement = True
                        if selected_piece.type == "rook":
                            if check_rook_movement(board, (selected_pos), (row, col), selected_piece):
                                movement = True
                        if selected_piece.type == "knight":
                            if check_knight_movement((selected_pos), (row, col), selected_piece):
                                movement = True
                        if selected_piece.type == "bishop":
                            if check_bishop_movement(board, (selected_pos), (row, col), selected_piece):
                                movement = True 
                        if selected_piece.type == "queen":
                            if check_queen_movement(board, (selected_pos), (row, col), selected_piece):
                                movement = True  
                        if selected_piece.type == "king":
                            if check_king_movement((selected_pos), (row, col), selected_piece):
                                movement = True 
                        
                        if movement:
                            old_row, old_col = selected_pos
                            board[old_row][old_col] = None
                            board[row][col]=selected_piece

                            selected_piece = None
                            selected_pos = None
                            if color_to_move == "white":
                                color_to_move = "black"
                            else:
                                color_to_move = "white"

    
    screen.fill((121, 56, 27))
    for row in range(0,8):
        for col in range(0,8):
            if (row+col)%2 == 0:
                color = (240, 217, 181)
            else:
                color = (181, 136, 99)          
            pygame.draw.rect(screen, color, (right+col*box_size, top+row*box_size, box_size, box_size))


    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                y = top+(box_size*row)
                x = right+(box_size*col)
                screen.blit(piece.image, (x, y))

    if selected_pos:
        sel_row, sel_col = selected_pos
        pygame.draw.rect(screen, (0,255,0), (right+sel_col*box_size, top+sel_row*box_size, box_size, box_size), 4)

    text = font.render(f"Turn: {color_to_move.upper()}", True, (255, 255, 255))
    screen.blit(text, ((right/2)-(text.get_width()/2), top))


    pygame.display.update()

pygame.quit()