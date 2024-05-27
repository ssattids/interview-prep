# stack = []
# push = stack.append(x)
# pop = stack.pop()
# peek = 
# def peek(stack):
#     if stack:
#         return stack[-1]    # this will get the last element of stack
#     else:
#         return None

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x: int) -> None:
        if (self.stack == []):
            self.stack.append(x)
            self.stack_min.append(x)
        elif (x < self.stack_min[-1]):
            self.stack.append(x)
            self.stack_min.append(x)
        else:
            self.stack.append(x)
            self.stack_min.append(self.stack_min[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
                                  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]