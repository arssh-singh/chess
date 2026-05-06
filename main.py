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


chess = Game()
chess.box_size = 87
top = (screen_h-(chess.box_size*8))/2
right = (screen_w-(chess.box_size*8))/2

Piece.box_size = chess.box_size
#setting pieces on board
chess.board.setup()

selected_piece = None
sel_pos = None
font = pygame.font.Font(None, 36)

def select_or_move_piece(chess)->None:
    selected_piece = chess.selected_piece
    sel_pos = chess.sel_pos
    print(selected_piece, sel_pos)
    #getting mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #getting box coords according to mouse position
    mouse_col = int((mouse_x-right)//chess.box_size)
    mouse_row = int((mouse_y-top)//chess.box_size)

    #checking if box is available on board
    if 0 <= mouse_row <= 7 and 0 <= mouse_col <= 7:
        #if mouse is on a piece and no other piece is selected, also piece is of color with the turn. Select that piece.
        if selected_piece is None:
            if chess.board.grid[mouse_row][mouse_col] is not None and chess.board.grid[mouse_row][mouse_col].color == chess.turn:
                chess.selected_piece = chess.board.grid[mouse_row][mouse_col]
                chess.sel_pos = mouse_row, mouse_col           
        else:
            #if mouse is on a piece and, already selected piece is of same color the select the piece mouse is on
            if chess.board.grid[mouse_row][mouse_col] is not None and chess.board.grid[mouse_row][mouse_col].color == selected_piece.color:
                chess.selected_piece = chess.board.grid[mouse_row][mouse_col]
                chess.sel_pos = mouse_row, mouse_col
            
            #if mouse is on a piece and already selected piece is not of same color then capture the piece if possible
            else:        
                #checking if movement is valid and legal             
                movement = chess.is_valid_move(mouse_row, mouse_col) and chess.is_legal_move(mouse_row, mouse_col)
                if movement:                
                    new_pos = mouse_row, mouse_col
                    chess.board.move(sel_pos, new_pos)
                    
                    old_row, old_col = sel_pos
                    if selected_piece.type == "pawn":
                        selected_piece.last_pos = (old_row, old_col)   

                    if selected_piece.type == "king" or selected_piece.type == "rook":                        
                        selected_piece.move_made()                                                                  

                    chess.selected_piece = None
                    chess.sel_pos = None

                    #changing turn                            
                    chess.change_turn()

running = True
while running:
    #loop to get events done in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # detecting any mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:      
            select_or_move_piece(chess)
    
    draw(screen, chess, right, top)

    text = font.render(f"Turn: {chess.turn.upper()}", True, (255, 255, 255))
    screen.blit(text, ((right/2)-(text.get_width()/2), top))

    pygame.display.update()

pygame.quit()