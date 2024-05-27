# %%
# https://leetcode.com/problems/search-insert-position/description/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        
        import math

        start = 0
        end = len(nums)
        length = end-start
        while(length > 1):

            length = end-start
            print(nums[start:end])

            if length % 2 == 1:
                mid = math.floor((end-start)/2)         
                mid_index = start+mid
                mid_num = nums[mid_index]
                mid_num_plus1 = nums[mid_index + 1]
                mid_num_minus_1 = nums[mid_index - 1]

                if mid_num == target:
                    return mid_index
                if (target > mid_num ) and (target < mid_num_plus1):
                    return  mid_index + 1
                if (target > mid_num_minus_1 ) and (target < mid_num):
                    return  mid_index

                if target < mid_num:
                    end = mid_index+1
                if target > mid_num:
                    start = mid_index

            elif length % 2 == 0:
                mid = int((end-start)/2)-1          
                mid_index = start+mid
                mid_num = nums[mid_index]
                mid_num_plus1 = nums[mid_index + 1]

                if mid_num == target:
                    return mid_index
                if mid_num_plus1 == target:
                    return mid_index + 1
                if target > mid_num and target < mid_num_plus1:
                    return mid_index+1
                
                if mid_index + 1 == len(nums)-1:
                    if target > mid_num_plus1:
                        return mid_index + 2
                if mid_index == 0:
                    if target < mid_num:
                        return 0
  
                if target < mid_num:
                    end = mid_index+1
                if target > mid_num:
                    start = mid_index
                    
            else:
                raise Exception("Something went wrong")

        return -1
                    
# %%
s = Solution()
s.searchInsert([1,3,5,9],2)
# %%
