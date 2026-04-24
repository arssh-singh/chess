
def check_pawn_movement(board, old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    direction = 1 if piece.color == "white" else -1
    start_row = 1 if piece.color == "white" else 6
    pasant_row = 4 if piece.color == "white" else 3

    if col == old_col:
        #allowing 1 step movement
        if row == old_row + direction:
            return board[row][col] is None

        #allowing 2 step movement if old row = start_row
        if row == old_row + 2*direction and old_row == start_row:
            return (board[row][col] is None and board[old_row+direction][col] is None)

        return False

    if old_row == pasant_row and abs(col - old_col) == 1 and row == old_row + direction and board[row][col] is None:

        if col < old_col:
            target = board[old_row][old_col - 1]
            if target and target.type == "pawn" and target.color != piece.color:
                return (True, old_row, old_col - 1)

        else:
            target = board[old_row][old_col + 1]
            if target and target.type == "pawn" and target.color != piece.color:
                return (True, old_row, old_col + 1)

        return False

    #allowing diagonal capture
    if row == old_row + direction and abs(col-old_col)==1:
        return (board[row][col] is not None and board[row][col].color != piece.color)

    return False



def check_rook_movement(board, old_pos, pos, piece):
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

def check_bishop_movement(board, old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    row_diff = row - old_row
    col_diff = col - old_col

    # Must move diagonally
    if abs(row_diff) != abs(col_diff):
        return False

    # Determine direction of movement
    step_row = 1 if row_diff > 0 else -1
    step_col = 1 if col_diff > 0 else -1

    # Check path for obstructions
    r, c = old_row + step_row, old_col + step_col
    while (r, c) != (row, col):
        if board[r][c] is not None:
            return False
        r += step_row
        c += step_col

    if board[row][col] is None or board[row][col].color != piece.color:
        return True
    
    return False

def check_queen_movement(board, old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    return check_bishop_movement(board, old_pos, pos, piece) or check_rook_movement(board, old_pos, pos, piece)

def check_king_movement(old_pos, pos, piece):
    old_row, old_col = old_pos
    row, col = pos

    row_diff = abs(old_row - row)
    col_diff = abs(old_col - col)

    return (row_diff <= 1 and col_diff <= 1) and (row_diff + col_diff != 0)