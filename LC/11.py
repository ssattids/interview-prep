# %%
from typing import List
class Solution:

    def maxArea(self, height: List[int]) -> int:

        l_p = 0 # index for starting bar
        r_p = len(height)-1 # index for ending bar

        max_water = 0

        while(l_p < r_p):

            width = r_p - l_p
            height_left = height[l_p] 
            height_right = height[r_p]
            print("left", height_left, "| right", height_right)
            current_min_height = min(height_left, height_right)

            container_size = width * current_min_height
            if container_size > max_water:
                max_water = container_size

            if height_left <= height_right:
                l_p += 1
            else:
                r_p -= 1

        return max_water


