from collections import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums == []:
            return [-1,-1]

        # use binary search
        start_ind = 0
        end_ind = len(nums)

        while (True):
            
            look_ind = start_ind + int((end_ind-start_ind) / 2)
            look_number = nums[look_ind]  
            
            if look_number == target:
                
                target_left_ind = look_ind
                target_right_ind = look_ind
                while(target_left_ind-1 >= 0):
                    if nums[target_left_ind-1] == target:
                        target_left_ind = target_left_ind - 1
                    else:
                        break
                while(target_right_ind+1 < len(nums)):
                    if nums[target_right_ind+1] == target:
                        target_right_ind = target_right_ind + 1
                    else:
                        break
                return([target_left_ind, target_right_ind])
                break
                # search left and right for the index

            if (look_number > target):
                # search left side
                start_ind = start_ind
                end_ind = look_ind

            elif (look_number < target):
                # search right side
                start_ind = look_ind + 1
                end_ind = end_ind

            else:
                raise Exception("Not possible")

            if(start_ind == end_ind):
                break
    
        return([-1,-1])

