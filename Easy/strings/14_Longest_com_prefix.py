class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        s = ''
        i = 0
        while i < len(first_str):
            for elem in strs[1:]:
                    if  i >= len(elem) or first_str[i] != elem[i]:
                        return s
            s += first_str[i]
            i += 1
        return s