from heapq import heapify, heappush, heappop, nsmallest, nlargest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        time complexity: O(n)
        space complexity: O(k)
        """
        self.k = k
        self.min_heap = nums[:k] # add uptil k elements
        heapify(self.min_heap)
        # keep removing, until the heap is of the size of k
        while(len(self.min_heap) > k):
            heappop(self.min_heap)
        # the heap is full at this point
        for num in nums[k:]:
            # # if the heap is full, and num is larger than the smallest value in the heap, we must pop the smallest element, and add the num into the heap
            if num > self.min_heap[0]:
                # heappop(self.min_heap)
                # heappush(self.min_heap, num)
                heapq.heapreplace(self.min_heap, num) # performs a heappop and heappush as well just more effeciently


    def add(self, val: int) -> int:
        """
        space complexity: O(1)
        time complexity: O(k)
        """
        # if the heap is not full, just add it
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
            return self.min_heap[0]
        # if the heap is full, and val is larger than the smallest value in the heap, we must pop the smallest element, and add the val into the heap
        elif val > self.min_heap[0]:
            # heappop(self.min_heap)
            # heappush(self.min_heap, val)
            heapq.heapreplace(self.min_heap, val) # performs a heappop and heappush as well just more effeciently
            return self.min_heap[0]
        # if the heap is full, and val is smaller than the smallest value in the heap, don't add any value, simply return the min value in the heap
        else:
            return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)