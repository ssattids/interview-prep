class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        other_nums = {}
        for i, num in enumerate(nums):

            # if the difference exists previously in the array
            if (target-num) in other_nums:
                return [other_nums[target-num], i]

            # keep adding the previous nums to the dictionary
            other_nums[num] = i

        return [-1, -1]
        

    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        
        num_ind = {}
        for i, num in enumerate(nums):
            if target-num in num_ind:
                return [num_ind[target-num], i]
            num_ind[num] = i

        return [-1,-1]