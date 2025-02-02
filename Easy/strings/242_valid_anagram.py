class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ht = {}
        t_ht = {}
        
        for elem in s:
            if elem in s_ht:
                s_ht[elem] +=1
            else:
                s_ht[elem] =1
        
        for elem in t:
            if elem in t_ht:
                t_ht[elem] +=1
            else:
                t_ht[elem] =1
        
        if s_ht == t_ht:
            return True
    
        return False
                