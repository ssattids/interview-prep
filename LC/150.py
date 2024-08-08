class Solution:
    # e.g.: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # step1: ["10","6","12","-11","*","/","*","17","+","5","+"]
    # step2: ["10","6", "-132", "/","*","17","+","5","+"]
    # step3: ["10", "0", "*","17","+","5","+"]
    # step4: ["0","17","+","5","+"]
    # step5: ["17","5","+"]
    # step6: ["22"]
    def evalRPN(self, tokens: List[str]) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        stack = []
        for t in tokens:
            #operator
            if t in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                elif t == "/":
                    res = int(a / b) # NOTE: a // b will fail - integer division fails
                print(res)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[0]

