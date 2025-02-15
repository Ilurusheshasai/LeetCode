class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y  #xor will have 1's at the positions where bits are different
        count = 0
        while xor: # Count the number of 1's in xor using Brian Kernighan's algorithm, which identifies the rightmost 1-bit in a number and clears it.
            xor &= xor - 1  # Clear the least-significant 1-bit
            count += 1
        return count

# Time complexity: O(k), where k is the number of bits in the input