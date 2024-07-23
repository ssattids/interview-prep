class Solution:

    def trap(self, height: List[int]) -> int:
        
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
