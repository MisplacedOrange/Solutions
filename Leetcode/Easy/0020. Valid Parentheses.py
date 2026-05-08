class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in m:
                if not stack or stack.pop() != m[c]:
                    return False
            else:     
                stack.append(c)

        return not stack
