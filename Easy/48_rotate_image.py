class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix)
        for i in range(len(matrix)):
            for j in range(i + 1, n):  # Only iterate over the upper triangle
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()

# generic way 
# step 1: transpose upper triangle with lower triangle, ie., rows become columns and column become rows
# step two just reverse the rows.