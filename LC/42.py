class Solution:

    def trap(self, height: List[int]) -> int:
        """
        2 pointer solution
        time: O(n)
        space: O(1)
        """
        l_p = 0
        r_p = len(height)-1
        max_l = height[l_p]
        max_r = height[r_p]
        water_trapped = 0
        while l_p < r_p:
            # if max_left value from the left is smaller than right we know that 
            # no matter what value in the right, the left value is the bottleneck
            # no matter the right value
            # (remember the water height is dependent on the value in the left and right)
            if max_l <= max_r:             
                l_p += 1
                max_l = max(max_l, height[l_p])
                water_trapped += max(0, max_l-height[l_p])
            else:
                r_p -= 1
                max_r = max(max_r, height[r_p])
                water_trapped += max(0, max_r-height[r_p])

        return water_trapped

    def trap_before(self, height: List[int]) -> int:
        """
        key is to come up with an equation per item 
        time: O(n)
        space: O(n)
        """
        max_left_arr = []
        max_left_current = 0
        for h in height:
            max_left_arr.append(max_left_current)
            if h > max_left_current:
                max_left_current = h

        max_right_arr = []
        max_right_current = 0
        for h in height[::-1]:
            max_right_arr.append(max_right_current)
            if h > max_right_current:
                max_right_current = h

        max_right_arr = max_right_arr[::-1]

        water_trapped = 0
        for max_left, max_right, h in zip(max_left_arr, max_right_arr, height):
            water_trapped += max(0, min(max_left, max_right)-h)

        return water_trapped



    def trap_original(self, height: List[int]) -> int:
        """
        First attempt
        time: O(n)
        space: O(1)
        """
        
        max_index = height.index(max(height))
        sub_area_water_part1 = self.water_till_max(height, max_index)

        height_reversed = height[::-1]
        max_index = len(height)-(max_index+1)
        sub_area_water_part2 = self.water_till_max(height_reversed, max_index)

        return sub_area_water_part1 + sub_area_water_part1

    def water_till_max(self, height, max_index):
        p1 = 0
        p2 = 0
        sub_area_water = 0
        while(p1 < len(height)-1 ):
            # when we see the max value, we will break
            if p1 == max_index:
                break
            if height[p1] == 0:
                p1+=1
                continue
            else:
                p2 = p1+1
                while(p2<len(height)-1):
                    if height[p2] < height[p1]:
                        sub_area_water += height[p1]-height[p2]
                    else:
                        break
                    p2 += 1
                p1=p2
        
        return sub_area_water
