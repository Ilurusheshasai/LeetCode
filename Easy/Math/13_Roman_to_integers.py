class Solution:
    def romanToInt(self, s: str) -> int:
        t_tab = {'M': 1000,
             'D': 500,
             'C': 100,
             'L': 50,
             'X': 10,
             'V': 5,
             'I': 1
             }
       
        num = 0 
        for i in range(len(s)):
            if i+1 < len(s) and t_tab[s[i+1]] > t_tab[s[i]]:
                num -= t_tab[s[i]]
            else:
                num += t_tab[s[i]]
        return num
