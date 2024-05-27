# https://leetcode.com/problems/search-insert-position/editorial/
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1
        while start <= end:
            pivot = (start + end) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                end = pivot - 1
            else:
                start = pivot + 1
        return start
    
# %%
s = Solution()
s.searchInsert([1,3,5,9],2)

# %%
# %%
s = Solution()
s.searchInsert([1],2)
# %%
s = Solution()
s.searchInsert([1],0)
# %%
