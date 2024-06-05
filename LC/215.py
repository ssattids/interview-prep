class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        
        li = []
        # using heapify to convert list into heap
        heapq.heapify(li)

        for elem in nums:
            if len(li) == k:
                # if the element is greater than the smallest element in the heap - add it
                if elem > li[0]:
                    heapq.heappop(li)
                    heapq.heappush(li, elem)
            else:
                heapq.heappush(li, elem)

        return min(li)