# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        time complexity = O(n), n = number of nodes
        space complexity = O(1)
        """

        if head == None:
            return None

        current_node = head
        list_count = 0
        while current_node != None:
            list_count += 1
            current_node = current_node.next

        remove_index = list_count - n
        # if the node to remove is at index 0, return the next node as head
        if remove_index == 0:
            return head.next
        # otherwise iterate to get the previous node
        else:
            current_node = head
            current_index = 0
            while (current_node != None):
                if current_index + 1 == remove_index:
                    # remove the node
                    temp = current_node.next.next
                    current_node.next = temp
                    return head
                else:
                    current_node = current_node.next
                    current_index += 1
            return head


    def removeNthFromEnd_v1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - Start the right pointer, move the right pointer along the list until n=0.
        - Start the left pointer
        - Continue moving both the right and left pointers (the difference between them is n)
        - Once the right pointer reaches the end, where the left pointer is where you have to remove the node!
        - Remove the node infront of the left pointer

        time complexity = O(n), n = number of nodes
        space complexity = O(1)
        """
        
        dummy = ListNode(0, head)

        left=dummy
        right=head
        while(n>0 and right):
            right = right.next
            n-=1

        while right:
            left = left.next
            right = right.next
        
        # delete the node
        left.next = left.next.next
        
        return dummy.next