# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Proof by example: think of a cycle with either an even or odd number of nodes and various starting positions for the slow and fast pointer

        time complexity: O(n)
        space complexity: O(1)
        """
        
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while (fast != None and fast.next != None):

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


    def hasCycle_initial(self, head: Optional[ListNode]) -> bool:
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
