class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l =len(nums)
        for i in range(l+1):
            if i not in nums:
                return i

# time complexity - O(n^2)
# space complexity is - O(1)

# O(n) for the outer loop and O(n) for the "in" operator 

# brute force solution