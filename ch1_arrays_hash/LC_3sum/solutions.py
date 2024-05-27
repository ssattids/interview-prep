# %%
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        solutions = []
        nums = sorted(nums) # [-4,-1,-1,0,1,2]
        for start in range(len(nums)):
            if nums[start] > 0: # if start is positive in sorted array there is no solution
                break
            if start > 0 and nums[start] == nums[start-1]: # skip duplicates - use the first element in the group of duplicates and then keep skipping the duplicates
                continue
            
            mid, end = start+1, len(nums)-1
            while mid < end:
                threeSum = nums[start] + nums[mid] + nums[end]
                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    mid += 1
                else:
                    solutions.append([nums[start], nums[mid], nums[end]])
                    mid += 1
                    while nums[mid] == nums[mid-1] and mid < end:
                        mid += 1
        return solutions

               
   

# %%
nums = [-1,0,0,0,0] 
Solution().threeSum(nums)
# %%
nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)    

# %%
