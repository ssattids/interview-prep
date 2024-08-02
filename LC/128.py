class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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


            
