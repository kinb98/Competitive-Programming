class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0 
        if needle not in haystack:
            return -1
        for i in range(len(haystack)): 
            if (haystack[i:i + len(needle)] == needle): 
                return i 