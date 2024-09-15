# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        n=number of nodes in a linked list
        time complexity: O(n)
        space complexity: O(n)
        """
        
        head_dict = {}
        while (head != None):
            if head in head_dict:
                return True
            head_dict[head] = True
            head = head.next

        return False
