import pygame

def drawboard(screen, right, top, box_size):
        for row in range(0,8):
            for col in range(0,8):
                if (row+col)%2 == 0:
                    color = (240, 217, 181)
                else:
                    color = (181, 136, 99)          
                pygame.draw.rect(screen, color, (right+col*box_size, top+row*box_size, box_size, box_size))

def drawpieces(screen, chess, right, top, box_size):
    for row in range(8):
        for col in range(8):
            piece = chess.board.grid[row][col]
            if piece:
                y = top+(box_size*row)
                x = right+(box_size*col)
                screen.blit(piece.image, (x, y))

def drawselection(screen, right, top, box_size, sel_pos):
     if sel_pos == None:
         return
     row, col = sel_pos
     pygame.draw.rect(screen, (0, 255, 0), (right+col*box_size, top+row*box_size, box_size, box_size), 6)

def draw(screen, chess, right, top):
     drawboard(screen, right, top, chess.box_size)
     drawpieces(screen, chess, right, top, chess.box_size)
     drawselection(screen, right, top, chess.box_size, chess.sel_pos)
    