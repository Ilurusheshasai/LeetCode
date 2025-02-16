class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [ [ 1 for _ in range(i)] for i in range(1, numRows+1)]
        
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle
    
    '''
    Time Complexity
        Initialization: O(n) for creating the initial structure.

    Calculation: 
        O(n ^ 2) for filling in the triangle values.

    Total: 
        O(n ^ 2) + O(n) =  O(n ^ 2).

    Space Complexity
        Triangle Storage: O(n ^ 2) for storing the entire triangle.
        
    '''