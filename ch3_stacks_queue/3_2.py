# Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum eiement? Push, pop and min should all operate in 0 ( 1 ) time.
# %%
def push(stack, min_stack, val):
    if stack:
        stack.append(val)
        if min_stack[-1] > val:
            min_stack.append(val)
        else:
            min_stack.append(min_stack[-1])
    else:
        stack.append(val)
        min_stack.append(val)

def pop(stack, min_stack):
    if stack:
        min_stack.pop()
        return stack.pop()
    else:
        return None

def get_minimum(stack, min_stack):
    return min_stack[-1]


min_stack = []
stack = []


# %%
push(stack, min_stack, 1)
push(stack, min_stack, 5)
push(stack, min_stack, 3)
push(stack, min_stack, 8)
# %%
