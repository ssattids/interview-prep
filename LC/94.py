# Link:
# https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        values = []
        def inord_trav(root):

            if root == None:
                return

            inord_trav(root.left)
            values.append(root.val)
            inord_trav(root.right)

        inord_trav(root)

        return values