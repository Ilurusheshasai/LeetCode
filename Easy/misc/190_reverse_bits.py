class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = bin(n)[2:].zfill(32)[::-1]
        return int(reversed_bits, 2)