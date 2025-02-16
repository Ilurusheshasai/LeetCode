class Solution:
    def isValid(self, s: str) -> bool:
        d = {
                '(' : ')', 
                '[' : ']', 
                '{' : '}'
            }

        seen = []
        for elem in s:
            if elem in d.keys():
                seen.append(elem)
            else:
                if len(seen) == 0:
                    return False
                else:
                    if d[seen[-1]] == elem:
                        seen.pop()
                    else:
                        return False
        
        if len(seen):
            return False
        else:
            return True