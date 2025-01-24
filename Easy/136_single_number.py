# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Each element in the array appears twice except for one element which appears only once. So the below solution works.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

'''

To fully satisfy the conditions, an approach using constant extra space would be necessary, such as using bitwise operations or mathematical properties of XOR.

For the original problem of finding a single unique number, we need to be guaranteed that all numbers except one appear an even number of times. In that case, the XOR method will indeed identify the unique number. 

ie., it works for [4,1,2,1,2]
but not for [4,1,2,1,2,2]
'''