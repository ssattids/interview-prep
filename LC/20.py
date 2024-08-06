class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = { ")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping: # if closing brace
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

    def isValidFirst(self, s: str) -> bool:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if stack == []:
                    stack.append(c)
                    continue
                stack_top = stack[-1]
                if stack_top == '(' and c == ')':
                    stack.pop()
                elif stack_top == '{' and c == '}':
                    stack.pop()
                elif stack_top == '[' and c == ']':
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False
