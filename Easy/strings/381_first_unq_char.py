class Solution:
    def firstUniqChar(self, s: str) -> int:
        unseen_hash = {}
        for index, elem in enumerate(s):
            if elem not in unseen_hash:
                unseen_hash[elem] = 1
            else:
                unseen_hash[elem] += 1 
        for elm, val in unseen_hash.items():
            if val == 1:
                return s.index(elm)
        return -1