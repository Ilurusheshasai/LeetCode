# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for el in nums:
            if el in d:
                d[el] += 1
                
            else:
                d[el] = 1
        
        for key, value in d.items():
            if value == 1:
                return key
        return 
    
    '''
    The provided solution does not fully satisfy the given conditions. Let's analyze it:
Time Complexity
The solution has a linear runtime complexity (O(n)), which satisfies the first part of the condition. It uses two loops:
The first loop iterates through the input list nums once.
The second loop iterates through the dictionary d, which in the worst case could be as large as nums.
Both of these contribute to a linear time complexity, O(n).
Space Complexity
The solution does not satisfy the condition of using only constant extra space. Here's why:
The dictionary d is used to store the count of each number in nums.
In the worst case, where all numbers in nums are unique, the dictionary will store n key-value pairs, where n is the length of nums.
This results in a space complexity of O(n), which is not constant extra space as required.
To satisfy the condition of using only constant extra space (O(1)), the solution would need to avoid using data structures that grow with the input size, such as the dictionary in this case.
    '''