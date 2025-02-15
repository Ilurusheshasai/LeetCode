class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # Clears the least-significant 1-bit
            count += 1
        return count

    
# time complexity - O(k) where k is the number of 1-bits in the binary representation of the input number n.