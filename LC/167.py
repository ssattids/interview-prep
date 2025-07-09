class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l_p, r_p = 0, len(numbers)-1

        while l_p < r_p:

            if numbers[l_p] + numbers[r_p] == target:
                return [l_p+1, r_p+1]
            elif numbers[l_p] + numbers[r_p] > target:
                r_p -= 1
            elif numbers[l_p] + numbers[r_p] < target:
                l_p += 1

        return [-1,-1]


    def twoSum_v1(self, numbers: List[int], target: int) -> List[int]:

        l_p = 0
        r_p = len(numbers)-1
        while(l_p < r_p):
            a_sum = numbers[l_p] + numbers[r_p]
            if a_sum == target:
                return [l_p+1, r_p+1]
            if a_sum > target:
                r_p-=1
            if a_sum < target:
                l_p+=1


        return [-1,-1]