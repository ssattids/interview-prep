class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """

        j = 0
        current_number_p1 = nums[j]

        for i in range(1,len(nums)):

            current_number_p2 = nums[i]
            if current_number_p1 == current_number_p2:
                continue
            else:
                j+=1
                nums[j] = current_number_p2
                current_number_p1 = nums[j]

        return j+1
    
    def removeDuplicates_v1(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
            
        if len(nums)==1:
            return 1

        pointer1 = 0
        pointer2 = 1
        total = 1
        while(pointer2 < len(nums)):
            prev_num = nums[pointer2-1]
            next_num = nums[pointer2]

            if prev_num != next_num:
                pointer1 += 1
                nums[pointer1] = next_num
                total+=1
            
            pointer2 += 1

        return total