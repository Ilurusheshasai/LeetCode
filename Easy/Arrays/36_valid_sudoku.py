import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        subgrid_size = int(math.sqrt(N))
        
        rows = [0] * N
        cols = [0] * N
        squares = [0] * N
        
        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    continue
                    
                num = int(board[r][c]) - 1  # Convert to 0-based index
                square_index = (r // subgrid_size) * subgrid_size + c // subgrid_size
                
                # Check if the number already exists
                if (rows[r] & (1 << num) or 
                    cols[c] & (1 << num) or 
                    squares[square_index] & (1 << num)):
                    return False
                
                # Mark the number as present
                rows[r] |= (1 << num)
                cols[c] |= (1 << num)
                squares[square_index] |= (1 << num)
        
        return True

    
    # A way to do it
    # Optimal way to do it using bit manupulation
    # more efficient than previous solution.

    # Each row, column and square are initially set to zero's
    # then when we traverse the list of list that represents sudoku row wise we check if a bit is 1 or not if its 1 already when we are checking that means that it is already used. So we return invalid.

    # if its valid in row  then  we search in column if its valid in colum as well then we search it in the square.

    # The first row of sub-grids (top-left to top-right) maps to indices 0, 1, and 2.
    # The second row of sub-grids maps to indices 3, 4, and 5.
    # The third row of sub-grids maps to indices 6, 7, and 8.

    # If its not 1 then we set it as 1 using the or operator.
