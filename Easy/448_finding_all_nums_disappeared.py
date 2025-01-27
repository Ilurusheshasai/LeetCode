class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        return [i + 1 for i, num in enumerate(nums) if num > 0]


# time complexity - O(n)
# space complexity is - O(1) according to the question.

# Explanation:
'''
Time Complexity: O(n)
The algorithm uses two passes through the array, each taking O(n) time:
First pass: Marks the presence of numbers by negating the values at their corresponding indices.
Second pass: Identifies missing numbers by checking for positive values.
Since both passes are linear, the overall time complexity is O(n).
Space Complexity: O(1)
The algorithm uses only the input array for its operations and doesn't require any additional data structures that grow with the input size. The only extra space used is for a few variables, which is constant regardless of the input size.
The returned list of missing numbers is not counted towards the space complexity as per the problem statement.

Given array: [4, 3, 2, 7, 8, 2, 3, 1]
Step 1: Marking numbers as present
We iterate through the array and use each number as an index to mark its presence:
For 4: Mark index 3 (4-1) negative. Array becomes [4, 3, 2, -7, 8, 2, 3, 1]
For 3: Mark index 2 (3-1) negative. Array becomes [4, 3, -2, -7, 8, 2, 3, 1]
For 2: Mark index 1 (2-1) negative. Array becomes [4, -3, -2, -7, 8, 2, 3, 1]
For 7: Mark index 6 (7-1) negative. Array becomes [4, -3, -2, -7, 8, 2, -3, 1]
For 8: Mark index 7 (8-1) negative. Array becomes [4, -3, -2, -7, 8, 2, -3, -1]
For 2: Already marked, skip
For 3: Already marked, skip
For 1: Mark index 0 (1-1) negative. Array becomes [-4, -3, -2, -7, 8, 2, -3, -1]
Step 2: Identifying missing numbers
We now check for positive values in the array. Their indices (+1) represent the missing numbers:
Index 4 is positive (8), so 5 is missing
Index 5 is positive (2), so 6 is missing
Therefore, the missing numbers are [5, 6].

'''

# one of the optimal solution