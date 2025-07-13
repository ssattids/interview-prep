# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity = O(n + m), n = size of list1, m = size of list2
        """

        head = None
        org_head = None

        while (True):

            if list1 == None and list2==None:
                break

            move = ""
            if list1 == None:
                move = "list2"
            elif list2==None:
                move = "list1"
            elif list1.val <= list2.val:
                move = "list1"
            else:
                move = "list2"

            if head == None and move == "list1":
                head = list1
                org_head = head
                list1 = list1.next
            elif head == None and move == "list2":
                head = list2
                org_head = head
                list2 = list2.next
            elif move == "list1":
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next

        return org_head

                





    def mergeTwoLists_v1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None and list2==None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        new_head = ListNode(-1)

        cache_new_head = new_head
        while(True):
            if (list1 == None or list2 == None):
                break

            if list1.val >= list2.val:
                new_head.next = list2
                list2 = list2.next
            elif list1.val < list2.val:
                new_head.next = list1
                list1 = list1.next
            new_head=new_head.next

        if list1 == None:
            new_head.next = list2
        elif list2 == None:
            new_head.next = list1
        
        return cache_new_head.next