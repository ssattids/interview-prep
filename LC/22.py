class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Brute force implementation
        time complexity = O(n^2)
        space complexity = O(n^2)
        """

        def valid(my_str):
            stack = []
            for s in my_str:
                if stack == [] and s == ')':
                    return False
                elif( s == '('):
                    stack.append(s)
                elif( s == ')'):
                    stack.pop()
            if stack == []:
                return True
            else:
                return False

        results = []

        def depth(limit, n, my_str):
            print('x')
            if n == limit:
                print(my_str)
                # check if valid,
                if valid(my_str):
                    results.append(my_str)
                return

            depth(limit, n+1, my_str+'(')
            depth(limit, n+1, my_str+')')

        depth(n*2, 0, '')

        return results

