class MinStack:
    """
    Overall:
    time complexity: O(n)
    space complexity: O(n)
    """

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        """
        When adding a val to the stack - instead add a 2 value tuple
        The first is the actual val, and the second is the current minimum value
        """

        if self.stack:
            # the current stack min can be easily calculated by comparing the previous min with the current value
            prev_stack_min = self.stack[-1][1]
            current_stack_min = min(val, prev_stack_min)
            self.stack.append((val, current_stack_min))
        else:
            self.stack.append((val,val))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()