def find_king(board, color):
	for row in range(0, 8):
		for col in range(0,8):
			if board[row][col] is not None and board[row][col].type=="king" and board[row][col].color==color:
				print("King fouund at: ", (row, col))