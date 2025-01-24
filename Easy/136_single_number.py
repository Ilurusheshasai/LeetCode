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