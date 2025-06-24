class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ')':
                if stack == []:
                    stack.append((i,')'))
                elif stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append((i,')'))
            elif c == '(':
                stack.append((i,'('))
            else:
                pass

        valid_s = ""
        pointer = 0
        for i, c in enumerate(s):
            # skip this
            if pointer < len(stack) and i == stack[pointer][0]:
                pointer+=1
            else:
                valid_s += c
        return valid_s
    
    def minRemoveToMakeValid_v1(self, s: str) -> str:

        list_s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(('(', i))
            elif c == ')':
                if stack != []:
                    peek_paren, peek_index = stack[-1]
                    if peek_paren == '(':
                        stack.pop()
                    else:
                        stack.append((')',i))
                else:
                    stack.append((')',i))

        for paren, i in stack:
            list_s[i] = ''

        return ''.join(list_s)
        
        