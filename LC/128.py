class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        set solution
        time complexity: O(n)
        space complexity: O(n)
        """

        set_nums = set(nums)

        max_consec_set_count = 0
        for num in set_nums:
            consec_set_count = 1
            # start of unique consecutive sequence
            if num-1 not in set_nums:
                while(True):
                    if num+1 in set_nums:
                        consec_set_count += 1
                        num+=1
                    else:
                        break
            max_consec_set_count = max(max_consec_set_count, consec_set_count)

        return max_consec_set_count


    def longestConsecutive2Dict(self, nums: List[int]) -> int:
        """
        2 dict solution
        time complexity: O(n)
        space complexity: O(n)
        """
        nums_bucks = []
        number_visited = {}

        for num in nums:
            number_visited[num] = False
            
        max_consec = 0
        for key, val in number_visited.items():

            if number_visited[key] == False:
                number_visited[key] = True
                org_key = key
                consec_count = 1
                while(key-1 in number_visited and number_visited[key-1]==False):
                    number_visited[key-1] = True
                    consec_count += 1
                    key -= 1
                key = org_key
                while(key+1 in number_visited and number_visited[key+1]==False):
                    number_visited[key+1] = True
                    consec_count += 1
                    key += 1
                    
                max_consec = max(max_consec, consec_count)

        return max_consec