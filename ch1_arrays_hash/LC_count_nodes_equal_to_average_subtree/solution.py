# %%
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def get_values(my_root, vals):
            vals.append(my_root.val)
            if my_root.left != None:
                get_values(my_root.left, vals)
            if my_root.right != None:
                get_values(my_root.right, vals)
            
        
        def subtree_avg_count(my_root):
            vals = []
            get_values(my_root, vals)
            average = sum(vals) // len(vals)
            count = 0
            for v in vals:
                if v == average:
                    count += 1
            return count
        
        def all_counts(my_root):

            sum_counts = subtree_avg_count(my_root)

            if my_root.left != None:
                sum_counts += all_counts(my_root.left)
            if my_root.right != None:
                sum_counts += all_counts(my_root.right)

            return sum_counts

        return all_counts(root)
# %%
    
leaf_0 = TreeNode(0)
leaf_1 = TreeNode(1)
leaf_6 = TreeNode(6)

node_8 = TreeNode(8, leaf_0, leaf_1)
node_5 = TreeNode(5, None, leaf_6)

node_4 = TreeNode(4, node_8, node_5)

s = Solution()

s.averageOfSubtree(node_4)
# %%


