class Solution:
    def romanToInt(self, s: str) -> int:    
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        prev = m[s[0]]
        integer = prev
        for x in s[1:]:
            cur = m[x]
            integer += cur if prev>=cur else cur - (2*prev)
            prev = cur
        return integer