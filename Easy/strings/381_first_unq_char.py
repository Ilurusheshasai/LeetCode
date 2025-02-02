class Solution:
    def firstUniqChar(self, s: str) -> int:
        unseen_hash = {}
        for index, elem in enumerate(s):
            if elem not in unseen_hash:
                unseen_hash[elem] = 1
            else:
                unseen_hash[elem] += 1 
        for ind, elm in enumerate(s):
            if unseen_hash[elem] == 1:
                return ind
        return -1