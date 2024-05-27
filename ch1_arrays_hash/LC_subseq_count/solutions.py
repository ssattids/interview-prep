# %%
from typing import List
import math
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        subseq_count = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            print("i=",nums[i])
            if nums[i] < target:
                j=len(nums)-1
                while(j > i):
                    print("\t", nums[i], nums[j])
                    if i == j and nums[i]+nums[j] <= target:
                        subseq_count += 1
                        print(f"single: pos_{i}, val={nums[i]}")
                    elif nums[i] + nums[j] <= target:
                        print(f"multiple: pos_{i}, val={nums[i]}, pos_{j}, val={nums[j]}")
                        subseq_count += math.pow(2, j-i)-1
                    j-=1
                
        return subseq_count 
    
# %%
ans = Solution().numSubseq([3,5,6,7], 9)
print(ans)
print(f"expected = 4")
# %%
ans = Solution().numSubseq([3,3,6,8], 10)
print(ans)
print(f"expected = 6")
# %%
ans = Solution().numSubseq([2,3,3,4,6,7], 12)
print(ans)
print(f"expected = 61")
# %%
