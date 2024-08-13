class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        time complexity: O(n)
        space complexity: O(n)
        """

        # stack contains tuples (position/day, tempreature)
        # the items in the stack are meant to represent days that have not yet found a day in which the tempreature is larger
        stack = [] 
        # this stores the the day differences until the next larges temperature
        results = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):

            if stack == []:
                stack.append((i, temp))
            else:
                # stack should only contain items of decreasing order!
                prev_i, prev_temp = stack[-1]
                
                # if the current days tempreature is larger than the tempreature days in the stack, keep removing them
                while (temp > prev_temp):
                    # add the the day difference in the right position them remove it from the stack
                    results[prev_i] = (i-prev_i)
                    stack.pop()   

                    # if the stack is non-empty, keep checking
                    if stack != []:
                        prev_i, prev_temp = stack[-1]
                    # if the stack is empty, break
                    else:
                        break
                # add the current day to the stack
                stack.append((i, temp))
        
        return results
