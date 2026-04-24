from movement_check import *

def find_king(board, color):
	for row in range(0, 8):
		for col in range(0,8):
			if board[row][col] is not None and board[row][col].type=="king" and board[row][col].color==color:
				return row, col

def can_attack_square(board, old_pos, target_pos, piece):
    if piece.type == "pawn":
        return check_pawn_movement(board, old_pos, target_pos, piece)

    if piece.type == "rook":
        return check_rook_movement(board, old_pos, target_pos, piece)

    if piece.type == "bishop":
        return check_bishop_movement(board, old_pos, target_pos, piece)

    if piece.type == "queen":
        return check_queen_movement(board, old_pos, target_pos, piece)

    if piece.type == "knight":
        return check_knight_movement(old_pos, target_pos, piece)

    if piece.type == "king":
        return check_king_movement(old_pos, target_pos, piece)

    return False

def is_king_safe(board, king_pos, color):
	k_row, k_col = king_pos
	if color == "white":
		direction = 1
	else:
		direction = -1
	i=0
	for row in range(0, 8):
		for col in range(0, 8):
			if board[row][col] is not None and board[row][col].color != color:
				if can_attack_square(board, (row, col), (k_row, k_col), board[row][col]):
					return False

	return True

