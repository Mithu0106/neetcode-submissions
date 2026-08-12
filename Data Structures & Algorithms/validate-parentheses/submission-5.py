class Solution:
    def isValid(self, s: str) -> bool:
        d={"}":"{", "]":"[",")":"("}
        stack=[]
        for ch in s :
            if ch in d :
                if stack and d[ch] == stack[-1]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(ch)
        return len(stack)==0