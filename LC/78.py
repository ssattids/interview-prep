class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            time complexity: O(2^n)
            space complexity: O(n) (and O(2^n) for the results array)
        """
        results = []
        subset = []

        def dfs(i):

            if i == len(nums):
                results.append(subset.copy())
                return

            current_num = nums[i]
            # include nums
            subset.append(current_num)
            dfs(i+1)
            # don't include nums
            subset.pop()
            dfs(i+1)


        dfs(0)

        return results
    
    def subsets_copy_arr(self, nums: List[int]) -> List[List[int]]:
        """
            time complexity: O(2^n)
            space complexity: O(n) (and O(2^n) for the results array)
        """
        results = []

        current_state = []

        def backtrack(i, current_state):

            if i == len(nums):
                results.append(current_state)
                return

            # left side - don't use num
            backtrack(i+1, current_state.copy())

            # right side - use num
            current_state.append(nums[i])
            backtrack(i+1, current_state.copy())

        backtrack(0, current_state.copy())

        return results
    
    
    def subsets_backtracking_copy(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking solution
        """
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decision NOT to inclide nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res            



    def subsets_cascading(self, nums: List[int]) -> List[List[int]]:
        """
        cascading solution
        e.g. [1,2,3]
        initial output = [[]], then
        output = [[],[1]], then
        output = [[],[1],[2],[1,2]], then
        output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] then

        as we iterate through nums, we append by 
        taking each element in output, and appending the number to each value in output
        then upadate output
        
        """
        output = [[]]
        for num in nums: # goes from 1-3 inclusive
            # add a number to every element in output
            additionalOutput = [] 
            for a_set in output:
                a_set_copy = a_set.copy()
                a_set_copy.append(num)
                additionalOutput.append(a_set_copy)

            # update output, similiar to output = output + additionalOutput
            for value in additionalOutput:
                output.append(value)

            print(additionalOutput)

        return output


