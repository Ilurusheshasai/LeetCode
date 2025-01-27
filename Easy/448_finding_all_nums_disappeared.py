class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        no_dups = set(nums)
        l = []
        
        for i in range(1, len(nums)+1):
            if i not in no_dups:
                l.append(i)
        return l

# time complexity - O(n)
# space complexity is - O(n)

# Explanation:
'''
Space complexity: 
    The returned list grows as per the size of set if there are more missing number s then the list is big, else the list will be small 

Time complexity:
    The time complexity of this algorithm is linear, O(n), where n is the length of the input list nums. Here's the breakdown:
    Creating set(nums) takes O(n) time, as it needs to iterate through all elements in nums.
    The for loop runs n times (from 1 to len(nums)+1).
    The in operation for a set is O(1) on average.
    Appending to a list is also O(1) on average.
Therefore, the overall time complexity is O(n) + O(n) * (O(1) + O(1)) = O(n).
'''

# one of the optimal solution