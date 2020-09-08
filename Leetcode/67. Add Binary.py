import math
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a)
        b = int(b)
        binary1 = a 
        decimal, i, n = 0, 0, 0
        while(a != 0): 
            dec = a % 10
            decimal = decimal + dec * pow(2, i) 
            a = a//10
            i += 1
        binary2 = b 
        decimal1, i, n = 0, 0, 0
        while(b != 0): 
            dec = b % 10
            decimal1 = decimal1 + dec * pow(2, i) 
            b = b//10
            i += 1
        res = decimal + decimal1 
        ans = str(bin(res))[2:]
        return ans
         