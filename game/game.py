from movement_check import *
from king_logic import *
from game.board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.selected_piece = None
        self.sel_pos = None
        self.last_move = None
        self.box_size = 87
    
    def is_valid_move(self, row, col):
        if self.selected_piece.type == "pawn":
            check_pawn = check_pawn_movement(self.board.grid, (self.sel_pos), (row, col), self.selected_piece)
            if check_pawn==True or check_pawn==False:
                allow_pawn=check_pawn
            else:
                val, p_row, p_col = check_pawn
                if val == True:
                    allow_pawn=True
                    self.board.grid[p_row][p_col] = None
                    print(p_row, p_col)
                else:
                    allow_pawn=False

            if allow_pawn==True:
                return True
        if self.selected_piece.type == "rook":
            return check_rook_movement(self.board.grid, (self.sel_pos), (row, col), self.selected_piece)
        if self.selected_piece.type == "knight":
            return check_knight_movement((self.sel_pos), (row, col), self.selected_piece)                                
        if self.selected_piece.type == "bishop":
            return check_bishop_movement(self.board.grid, (self.sel_pos), (row, col), self.selected_piece)                                    
        if self.selected_piece.type == "queen":
            return check_queen_movement(self.board.grid, (self.sel_pos), (row, col), self.selected_piece)                                    
        if self.selected_piece.type == "king":
            return check_king_movement(self.board.grid, (self.sel_pos), (row, col), self.selected_piece)
    
    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
    
    def simulate_move(self, old_pos, row, col):
        board_copy = [row[:] for row in self.board.grid]
        old_row, old_col = old_pos
        piece = self.board.grid[old_row][old_col]
        board_copy[old_row][old_col] = None
        board_copy[row][col] = piece

        return board_copy
    
    def is_legal_move(self, row, col):
        #simulating move
        test_board = self.simulate_move(self.sel_pos, row, col)
        king_pos = find_king(test_board, self.selected_piece.color)

        if not is_king_safe(test_board, king_pos, self.selected_piece.color):
            print("Danger To King")
            return False
        
        return True