class Solution:

    def findMin(self, nums: List[int]) -> int:
        """
        official solution
        time complexity: O(log(n))
        space complexity: O(log(n))
        """
        res = nums[0]
        start = 0
        end = len(nums) - 1

        while(start <= end):

            if nums[start] < nums[end]:
                res = min(res, nums[start])

            mid = start + ((end-start) //2)
            # in this case, we know that the mid value is the
            # end of the original array, so we need to go left
            # [1,2,3,4,5] => nums[mid]>=nums[start] == 3>=1, False, go left
            # [5,1,2,3,4] => nums[mid]>=nums[start] == 2>=5, False, go left
            # [4,5,1,2,3] => nums[mid]>=nums[start] == 1>=4, False, go left, registers the global the min
            # [3,4,5,1,2] => nums[mid]>=nums[start] == 5>=3, True, go right
            # [2,3,4,5,1] => nums[mid]>=nums[start] == 4>=2, false, go right
            
            res = min(res, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1

        return res

    def findMinBinarySearch(self, nums: List[int]) -> int:
        """
        my solution
        time complexity: O(log(n))
        space complexity: O(1)
        """

        start = 0
        end = len(nums)-1

        while(True):

            mid = start + ((end-start) // 2)

            s1 = nums[start] # start value of left array
            e1 = nums[mid] # end value of left array
            # print("s1:", s1, "e1", e1)
            s2 = nums[mid] # start value of right array
            e2 = nums[end] # end value of right array
            # print("s2:", s2, "e2", e2)

            if end-start < 3:
                return min(nums[start:end+1])

            # the key to finding the minimum is to check where the rotation starts
            # special case where the array is not rotated (or rotated n times)
            if e1 > s1 and e2 > s2:
                # go left
                end = mid
            # the starting value is greater than the ending value - meaning the rotation start is the left array
            elif s1 > e1:
                # go left
                end = mid
            # otherwise the rotation start is in the right array
            else:
                # go right
                start = mid
                
        return None

    def findMin_old(self, nums: List[int]) -> int:
        """
        doesn't pass all tests
        """
        start = 0
        end = len(nums) - 1
        i = 0
        while(True):

            mid = start + ((end-start) // 2)
            print(mid)

            start_num = nums[start]
            end_num = nums[end]
            middle_num = nums[mid]
            
            mid_prev = (mid-1)%len(nums)
            mid_next = (mid+1)%len(nums)
            if middle_num <= nums[mid_prev] and middle_num <= nums[mid_next]:
                print("returned")
                return middle_num

            if start_num < end_num:
                end = mid-1
            if end_num < start_num:
                start = mid+1
            

        return -1
            