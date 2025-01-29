class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                    
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[r // 3, c // 3]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True
    
    # A way to do it
    # we just create rows, columns, square dictionaries
    # rows and column has keys as indeces and values as sets. when we try to access indeces thats not there in the list this creates that index.
    # square has tuple as index, this is done so that we can map the elements in a subgrid to a index. 