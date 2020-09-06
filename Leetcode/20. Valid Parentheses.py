class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        j = -1
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False
        for i in s:
            if i == '(' or i == '{' or i == '[':
                l.append(i)
                j += 1
            if i == ')':
                if j != - 1 and l[j] == '(':
                    l.pop()
                    j -= 1 
                else:
                    return False
            if i == '}':
                if j != - 1 and l[j] == '{':
                    l.pop()
                    j -= 1 
                else:
                    return False
            if i == ']':
                if j != - 1 and l[j] == '[':
                    l.pop()
                    j -= 1 
                else:
                    return False
        if j != -1:
            return False
        return True