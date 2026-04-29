import pygame
from game.piece import Piece
from game.game import Game
from game.board import Board
from ui.renderer import draw

pygame.init()
screen_h = 750
screen_w = 1200
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Drawing Shapes")

box_size = 87
top = (screen_h-(box_size*8))/2
right = (screen_w-(box_size*8))/2

Piece.box_size = box_size

chess = Game()
#setting pieces on board
chess.board.setup()

selected_piece = None
sel_pos = None
font = pygame.font.Font(None, 36)

def select_or_move_piece(selected_piece, sel_pos, chess):
    #getting mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #getting box coords according to mouse position
    mouse_col = int((mouse_x-right)//box_size)
    mouse_row = int((mouse_y-top)//box_size)

    #checking if box is available on board
    if 0 <= mouse_row <= 7 and 0 <= mouse_col <= 7:
        #if mouse is on a piece and no other piece is selected, also piece is of color with the turn. Select that piece.
        if selected_piece is None:
            if chess.board.grid[mouse_row][mouse_col] is not None and chess.board.grid[mouse_row][mouse_col].color == chess.turn:
                selected_piece = chess.board.grid[mouse_row][mouse_col]
                sel_pos = mouse_row, mouse_col           
        else:
            #if mouse is on a piece and, already selected piece is of same color the select the piece mouse is on
            if chess.board.grid[mouse_row][mouse_col] is not None and chess.board.grid[mouse_row][mouse_col].color == selected_piece.color:
                selected_piece = chess.board.grid[mouse_row][mouse_col]
                sel_pos = mouse_row, mouse_col
            
            #if mouse is on a piece and already selected piece is not of same color then capture the piece if possible
            else:        
                #checking if movement is valid and legal             
                movement = chess.is_valid_move(selected_piece, sel_pos, mouse_row, mouse_col) and chess.is_legal_move(selected_piece, sel_pos, mouse_row, mouse_col)
                if movement:                            
                    old_row, old_col = sel_pos
                    #setting old position of piece to none
                    chess.board.grid[old_row][old_col] = None
                    #putting piece on new positions
                    chess.board.grid[mouse_row][mouse_col]=selected_piece

                    if selected_piece.type == "pawn":
                        selected_piece.last_pos = (old_row, old_col)   

                    if selected_piece.type == "king" or selected_piece.type == "rook":                        
                        selected_piece.move_made()                                                                  

                    selected_piece = None
                    sel_pos = None

                    #changing turn                            
                    chess.change_turn()

    return selected_piece, sel_pos


running = True
while running:
    #loop to get events done in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # detecting any mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:      
            selected_piece, sel_pos = select_or_move_piece(selected_piece, sel_pos, chess)
    
    draw(screen, chess, right, top, box_size, sel_pos)

    text = font.render(f"Turn: {chess.turn.upper()}", True, (255, 255, 255))
    screen.blit(text, ((right/2)-(text.get_width()/2), top))

    pygame.display.update()

pygame.quit()