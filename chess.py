import pygame

pygame.init()
screen_h = 750
screen_w = 750
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

def check_pawn_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos
    if piece.color == "white":
        # checking if pawn is moving side ways
        if row==old_row+1 and (col==old_col+1 or col==old_col-1):
            # allowing movement if pawn has a piece to take
            if board[row][col] is not None and board[row][col].color != "white":
                return True
            else:
                return False

        # declaring regular step of pawn
        step = 1
        # changing it to 2 only if pawn is on row 1 and has no piece on row 3
        if old_row == 1 and board[old_row+2][col] is None:
            step = 2
        # allowing {step} movemnt is if pawn has nothing in front and not moving sideways 
        if 1 <= row-old_row <= step and board[old_row+1][col] is None and col-old_col==0:
            return True
        return False

    if piece.color == "black":
        # checking if pawn is moving side ways
        if row==old_row-1 and (col==old_col+1 or col==old_col-1):
            # allowing movement if pawn has a piece to take
            if board[row][col] is not None and board[row][col].color != "black":
                return True
            else:
                return False

        # declaring regular step of pawn
        step = 1
        # changing it to 2 only if pawn is on row 6 and has no piece on row 4
        if old_row == 6 and board[old_row-2][col] is None:
            step = 2
        # allowing {step} movemnt is if pawn has nothing in front and not moving sideways 
        if 1 <= old_row-row <= step and board[old_row-1][col] is None and col-old_col==0:
            return True
        return False

def check_rook_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    if old_row != row and old_col != col:
        return False
    
    # moving vertically
    if old_col == col:
        step = 1 if row>old_row else -1
        for box in range(old_row+step, row, step):
            if board[box][col] is not None:
                return False

    # moving horizontally
    elif old_row == row:
        step = 1 if col>old_col else -1
        for box in range(old_col+step, col, step):
            if board[row][box] is not None:
                return False

    if board[row][col] is None or board[row][col].color != piece.color:
        return True

    return False

def check_knight_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    if (abs(row-old_row) == 2 and abs(col-old_col) == 1) or (abs(col-old_col) == 2 and abs(row-old_row) == 1):
        return True
    else: 
        return False

def check_bishop_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    #yx
    if row<old_row and col>old_col:
        for coords in zip(range(old_row+1, row), range(old_col+1, col)):
            y, x = coords
            if board[y][x] != None:
                return

    if row>old_row and row-old_row == col-old_col:
        return True
    if row<old_row and old_row-row == old_col-col:
        return True
    if row<old_row and old_row-row == col-old_col:
        return True
    if row>old_row and row-old_row == old_col-col:
        return True

def check_queen_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    return check_bishop_movement(old_pos, pos, piece) or check_rook_movement(old_pos, pos, piece)

def check_king_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = int((mouse_x-right)//box_size)
            row = int((mouse_y-top)//box_size)

            if 0 <= row < 8 and 0 <= col < 8:
                if selected_piece is None:
                    if board[row][col] is not None:
                        selected_piece = board[row][col]
                        selected_pos = row, col
                else:
                    if board[row][col] is not None and board[row][col].color == selected_piece.color:
                        selected_piece = board[row][col]
                        selected_pos = row, col
                    else: 
                        movement = False
                        if selected_piece.type == "pawn":
                            if check_pawn_movement((selected_pos), (row, col), selected_piece):
                                movement = True
                        if selected_piece.type == "rook":
                            if check_rook_movement((selected_pos), (row, col), selected_piece):
                                movement = True
                        if selected_piece.type == "knight":
                            if check_knight_movement((selected_pos), (row, col), selected_piece):
                                movement = True
                        if selected_piece.type == "bishop":
                            if check_bishop_movement((selected_pos), (row, col), selected_piece):
                                movement = True 
                        if selected_piece.type == "queen":
                            if check_queen_movement((selected_pos), (row, col), selected_piece):
                                movement = True  
                        if selected_piece.type == "king":
                            if check_queen_movement((selected_pos), (row, col), selected_piece):
                                movement = True 
                        
                        if movement:
                            old_row, old_col = selected_pos
                            board[old_row][old_col] = None
                            board[row][col]=selected_piece

                            selected_piece = None
                            selected_pos = None
    
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

    pygame.display.update()

pygame.quit()