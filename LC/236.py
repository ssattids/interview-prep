# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root, p, q):
            if root is None:
                return None
            if root == p:
                return p
            if root == q:
                return q

            left = search(root.left, p, q)
            right = search(root.right, p, q)

            if left != None and right!=None:
                return root
            elif (left != None):
                return left
            elif (right != None):
                return right

        root = search(root, p,q)

        return root


    def lowestCommonAncestor_copied_solution(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r