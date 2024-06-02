class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            Implement solution from scratch O(n)
        """
        cumalitive_sum = 0
        prefix_sums = {0:1}
        result_counts = 0

        for num in nums:

            cumalitive_sum += num
            diff = cumalitive_sum-k
            result_counts += prefix_sums.get(diff, 0)

            if cumalitive_sum in prefix_sums:
                prefix_sums[cumalitive_sum] += 1
            else:
                prefix_sums[cumalitive_sum] = 1

        return result_counts

    def subarraySum_solutioncopy(self, nums: List[int], k: int) -> int:
        """
            Copy online solution
        """
        result_ks = 0
        cumalitive_sum = 0
        prefix_sums = {0 : 1}

        for n in nums:
            cumalitive_sum += n
            diff = cumalitive_sum - k

            result_ks += prefix_sums.get(diff, 0)
            prefix_sums[cumalitive_sum] = 1 + prefix_sums.get(cumalitive_sum, 0)

        return result_ks

    def subarraySum_cumsum(self, nums: List[int], k: int) -> int:
        """ 
            Bruteforce solution with optimization: O(n^2)
        """
        answers = 0
        for i in range(len(nums)):
            total_sum = 0
            for j in range(i, len(nums)):
                total_sum += nums[j]
                if total_sum == k:
                    answers+=1

        return answers


    def subarraySum_bruteforce(self, nums: List[int], k: int) -> int:
        """
            Bruteforce solution: O(n^3)
        """
        answers=0
        for i in range(len(nums)):
            for j in range(len(nums)+1):
                if j > i:
                    if sum(nums[i:j]) == k:
                        answers+=1
        
        return answers
