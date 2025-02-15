class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x != y:
            if x%2 != y%2:
                count += 1
            x = x//2
            y = y//2 
        return count
    
"""
Weaknesses
Inefficiency:

Time Complexity: O(max(log(x), log(y))), where log(x) represents the number of bits in x. The algorithm iterates until x and y become equal, which requires O(log(max(x,y))) iterations in the worst case. For numbers like x = 8 (1000), y = 0, it requires 4 iterations instead of directly checking only the differing bits.

Slower Operations: Uses division (//) and modulo (%), which are computationally slower than bitwise operations.

Fails for Negative Numbers:

In Python, // rounds toward negative infinity, causing infinite loops for negative inputs (e.g., x = -1, y = 0).

"""