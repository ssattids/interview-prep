class Solution:

    def threeSum_v3(self, nums: List[int]) -> List[List[int]]:
        """
        This is an editorial solution - that is identical to threeSum_v2 - it is placed here to show some optimizations with pointers
        """
        res = []
        def twoSum(nums: List[int], i: int, res: List[List[int]]):
            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(nums, i, res)
        return res

    

    def threeSum_v2(self, nums: List[int]) -> List[List[int]]:
        """
        This solution essentially says
        1) Sort the array
        2) Take the current number, nums[i], to find a 0 solution of 3 numbers, you need to find the 2 numbers ahead that sum to the negative of that number, e.g. nums[i] = -5, then the negative of that will be 5, and we need to find 2 number that add up to 5
        3) This is essentially 2 sum

        time complexity: O(n^2)
        space complexity: O(n) worse case
        """

        def twoSum(nums, j_start, target, org_number):
            remainders = {}
            for j in range(j_start, len(nums)):
                number = nums[j]
                remainder = target-number
                # we have found a solution, add it to the set
                if remainder in remainders:
                    solutions.add((number, remainder, org_number))
                else:
                    remainders[number] = True
        
        solutions = set()
        nums.sort() # sort in place
        print(nums)

        for i, num in enumerate(nums):
            if i == len(nums)-1:
                break
            # if the current number equals the previous number - we have duplicate numbers, and we have already taken into account solutions from duplicate numbers!
            if i == 0 or nums[i] != nums[i - 1]:
                # take the array infront of the ith pointer - and calculate 2 sum on it - to get zero, you need to calculate the negative of num (num = the number at the ith pointer)
                two_sum_solutions = twoSum(nums, i+1, -1*num, num)
            
        return list(solutions)


    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:

        def twoSum(numbers: List[int], i: int, solutions:List) -> List[int]:

            start = i+1
            end = len(numbers) - 1

            while(start < end):
                current_sum = numbers[i] + numbers[start] + numbers[end]
                # the sum is too large - decrement end
                if current_sum > 0:
                    end -= 1
                # the sum is too small - increment start
                elif current_sum < 0:
                    start += 1
                # the sum is exactly equal to zero
                else:                    
                    solutions.append([numbers[i], numbers[start], numbers[end]])
                    start+=1
                    end-=1
                    while start < end and numbers[start] == numbers[start-1]:   
                        start+=1 

        solutions = []
        nums = sorted(nums) # [-4,-1,-1,0,1,2] or [-4,2,2,5]
        for i in range(len(nums)):
            # if we start with negative number, we know we can never get to a zero
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]: # in the sorted array only take the first of the duplicate elements
                twoSum(nums, i, solutions) # [-4,-1,-1,0,1,2] 
            
        return solutions

    

            

