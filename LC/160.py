# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getIntersectionNodeOptimal(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
            We will get the size of LL A, labelled N, and LL B, labelled M first
            If there is an intersection, we know from the intersection to the tail, the values are the same
            So we move the larger of the lists until they are the same length, and then we just keep checking if at point i any of the nodes are the same.
            If they are, we have found an intersection
        """


        # M = size of LL B
        # N = size of LL A
        # space = O(1)
        # time = O(N+M+)

        headA_tmp, headB_tmp = headA, headB

        N = 0
        while headA_tmp != None:
            headA_tmp = headA_tmp.next
            N += 1
        M = 0
        while headB_tmp != None:
            headB_tmp = headB_tmp.next
            M += 1

        if M >= N: # this is what the default code for
            pass
        else: # N > M - so swap them
            M,N = N,M
            headA, headB = headB, headA

        DIFF = M-N
        M_DIFF = 0
        while headB != None:
            if M_DIFF == DIFF:
                break
            headB = headB.next
            M_DIFF += 1
        # now headB and headA are the same length and search to see if they are the same
        while(headB!=None):
            if headB == headA:
                return headB
            else:
                headB = headB.next
                headA = headA.next
        
        return None

    def getIntersectionHash(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # M = size of LL B
        # N = size of LL A
        # space = O(M)
        # time = O(M+N)

        B_LL_items = set()
        while(headB != None):
            B_LL_items.add(headB)
            headB = headB.next

        while(headA != None):
            if headA in B_LL_items:
                return headA
            headA = headA.next
        
        return None
