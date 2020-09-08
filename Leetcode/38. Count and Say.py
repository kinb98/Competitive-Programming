class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        res = self.countAndSay(n-1)
        ans = ""
        last = res[0]
        cnt = 0
        for l in res:
            if l == last:
                cnt += 1
            else:
                ans += str(cnt)+last
                last = l
                cnt = 1 
        ans += str(cnt)+last
        return ans
        