class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        for c in list(s):
            if c == '(':
                stack.append('(')
            elif c == ')':
                if stack == []:
                    stack.append(')')
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
        return len(stack)