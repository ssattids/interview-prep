class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        """
        Using a 2 pointer solution


        time complexity: O(n^2)
        space complexity: O(1)
        """
        
        nums.sort() # sort in place

        current_sum = nums[0]+nums[1]+nums[len(nums)-1]
        distance = abs(current_sum - target)
        
        min_distance = distance
        closest_sum = current_sum


        for i, num in enumerate(nums):

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < target:
                    left += 1
                    distance = abs(current_sum - target)
                    if distance < min_distance:
                        min_distance = distance
                        closest_sum = current_sum  
                elif current_sum > target:
                    right -= 1
                    distance = abs(current_sum - target)
                    if distance < min_distance:
                        min_distance = distance
                        closest_sum = current_sum
                else:
                    return target

        return closest_sum