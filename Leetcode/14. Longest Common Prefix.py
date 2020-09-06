class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return res
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                res += c
            else:
                break 
        return res