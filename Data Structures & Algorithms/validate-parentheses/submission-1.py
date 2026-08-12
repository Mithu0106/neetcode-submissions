class Solution:
    def isValid(self, s: str) -> bool:
        d = { "]":"[","}":"{",")":"("}
        stack = []
        for b in s :
            if ( b in d) and stack and stack[-1] == d[b]:
                stack.pop()
            else :
                stack.append(b)
        return len(stack)==0