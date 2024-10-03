class Solution:
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

        return output


