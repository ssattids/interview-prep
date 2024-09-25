import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        time complexity: O(nlogn)
        space complexity: O(1) (no additional space used)
        """
        
        # choose the heaviest two stones
        # k (k=2) larges values

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            if x == y:
                continue
            else:
                heapq.heappush(stones, (y-x) * -1)

        if stones == []:
            return 0
        else:
            return stones[0]*-1
            
