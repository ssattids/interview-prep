"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        current_node = head

        if current_node == None:
            current_node = Node(insertVal)
            current_node.next = current_node
            return current_node
        # this means that there is one value in the circular linked list
        elif current_node.next == current_node:
            current_node.next = Node(insertVal)
            current_node.next.next = current_node
            return head
        else:
            while (True):
                current_val = current_node.val
                current_next_val = current_node.next.val
                # 1) Check if we can add the current node
                # 1.1)here the current val is the largest value - so we are at the end
                if current_val > current_next_val:
                    # the insert val is greater than the largest value - insert it here
                    if insertVal >= current_val or insertVal <= current_next_val:
                        
                        new_node = Node(insertVal)
                        new_node.next = current_node.next
                        current_node.next = new_node
                        return head
                # 1.2) insert value is greater than current node and less than next node so we can easily add it
                elif(insertVal >= current_val and insertVal <= current_next_val):
                    new_node = Node(insertVal)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return head
                #2) the insert value cannot be added infront of the current node, so go to the next node
                current_node = current_node.next
                #3) edge case if all the values in the circular linked list are the same
                if current_node == head:
                    new_node = Node(insertVal)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return head