class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()

# Time complexity: O(1), Space complexity: O(1), because the input is a fixed size (32 bits) and the number of operations is constant. hardware dependent.

'''
Method	                    Time Complexity	    Lines of Code	Readability	        Compatibility
Original Loop	                O(logn)	             7	            Low	            All versions
XOR + Bitwise AND Trick	        O(k)	             5	            Medium	        All versions
bin(x ^ y).count('1')	        O(logn)	             1	            High	        All versions
(x^y).bit_count()	            O(1)	             1	            Highest	        Python 3.10+
'''