class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        result = 0
        i = 0
        
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        
        while i < len(s) and s[i].isnumeric():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
            # Check for overflow
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            elif result * sign < -2**31:
                return -2**31
        
        return result * sign

# first strip spaces
# then identify sign of the immediate digit first
# if it is + or - then we can determine the sign of the number
# Else we loop across the string until we see a non numeric charecter
# if we see a numeric charecter we just store it.
# finally we check the overflow