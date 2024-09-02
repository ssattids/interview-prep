class Solution:
    def merge_sol1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        merge with copy
        
        
        """
        #make a copy of the first m elements of nums1
        nums1_copy = nums1[:m]
        p1, p2 = 0, 0

        for p in range(m + n):
            # if the second pointer has reached the end, keep adding value from where the first pointer is
            if p2 >= n:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            # if 
                # 1) p1 is less than m (or the number of possible values from p1) AND
                # 2) the current value in nums1 (represented by nums1_copy[p1]) is less than the current values in nums2 (represented by nums2[p2])
            # add the current value of nums1
            elif (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

    def merge_super_naive(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Time complexity: O((n+m)log(n+m))
        Space complexity: O(1)
        """
        
        for i in range(len(nums2)):
            nums1[i+m] = nums2[i]

        nums1.sort()

    def merge_naive(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Naive solution

        Time complexity: O(n + m)
        Space complexity: O(n + m)
        """
        
        nums1_copy = nums1.copy()
        p1 = 0
        p2 = 0
        m = len(nums2)
        n = len(nums1_copy)-m
        
        final = [] 
        while(True):
            
            if p1 == n and p2 == m:
                break
            elif (p1 == n):
                final.append(nums2[p2])
                p2+=1
                continue
            elif (p2==m):
                final.append(nums1[p1])
                p1+=1
                continue
            
            a, b = nums1[p1], nums2[p2]
            if a <= b:
                final.append(a)
                p1 += 1
            else:
                final.append(b)
                p2 += 1

        for i in range(len(nums1)):
            nums1[i] = final[i]


