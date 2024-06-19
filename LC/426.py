"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # use a dummy node
        dummy = Node()
        self.head = dummy

        def traverse(root):
            """
                in-order traversal will access the node in ascending order
            """
            if root == None:
                return

            traverse(root.left)
            
            # initially head is the previously accessed node!
            # link up the nodes
            self.head.right = root
            root.left = self.head
            # increment head to the next node
            self.head = self.head.right

            traverse(root.right)

        traverse(root)

        if dummy.right == None:
            return None
        else:
            # link up the first node to the last node
            dummy.right.left = self.head
            # link up the last node to the first node
            self.head.right = dummy.right

        return dummy.right


    def treeToDoublyList_2n(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        sorted_results = [] 

        def traverse(root, parent):
            if root == None:
                return
            traverse(root.left, root)
            sorted_results.append(root)
            traverse(root.right, root)

        traverse(root, None)

        if sorted_results == []:
            return root
        if len(sorted_results)==1:
            root.left = root
            root.right = root
            return root

        head = sorted_results[0]
        
        for i in range(0, len(sorted_results)-1):
            node=sorted_results[i]
            node_plus1=sorted_results[i+1]

            node.right = node_plus1
            node_plus1.left = node

        sorted_results[-1].right = head
        head.left = sorted_results[-1]

        return head