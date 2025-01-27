class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l =len(nums)
        return (sum(range(l+1)) - sum(nums))

# time complexity - O(1)
# space complexity is - O(1)

# Explanation:
'''
    *) The time complexity of this algorithm is linear, O(n), where n is the length of the input list nums. This is because:
    
    *) len(nums) operation takes constant time, O(1).
    
    *) sum(range(l+1)) takes O(n) time, as it needs to iterate through all numbers from 0 to l.
    *) sum(nums) also takes O(n) time, as it iterates through all elements in the list.
    *) The subtraction operation is constant time, O(1).
    *) The dominant operations are the two sum calculations, both of which are O(n), resulting in an overall time complexity of O(n).

'''

# one of the optimal solution