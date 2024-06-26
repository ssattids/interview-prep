"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pass        

    def lowestCommonAncestor_visited2(self, p: 'Node', q: 'Node') -> 'Node':

        visited = set()

        while p != None:
            visited.add(p.val)
            p = p.parent

        while(q!=None):
            if q.val in visited:
                return q
            q = q.parent

        return None

    def lowestCommonAncestor_visited1(self, p: 'Node', q: 'Node') -> 'Node':
        p1, q1 = p, q
        visited = {}
        while(True):

            if p1.parent == None and q1.parent == None:
                break
            
            if p1.val in visited and p1.parent != None:
                return p1
            visited[p1.val]=True
            if q1.val in visited and q1.parent != None:
                return q1
            visited[q1.val]=True

            if p1.parent != None:
                p1 = p1.parent
            
            if q1.parent != None:
                q1 = q1.parent
            
        return p1


    def lowestCommonAncestor_copied(self, p: 'Node', q: 'Node') -> 'Node':

        p1, p2 = p, q
        i=0
        while(p1 != p2):
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q

            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p
            i+=1
        
        return p1
            

    def lowestCommonAncestor_0(self, p: 'Node', q: 'Node') -> 'Node':
        
        lca_found = [False]
        lca_val = [None]
        lca_node = [None]

        def lca_children(root, p):
            if root == None:
                return False
            if root.val == p.val:
                return True
            lf = lca_children(root.left, p)
            rf = lca_children(root.right, p)

            return lf or rf

        def lca_parent(root, from_child, p):
            if root == None:
                return False
            # if the root is the 
            if root.val == p.val:
                lca_found[0]=True
                lca_val[0] = root.val
                lca_node[0] = root
                return True
            
            child_flag = False
            # search the left side if not been searched from
            if from_child != root.left:
                child_flag = lca_children(root.left, p)
            # search the right side if not been searched from
            if from_child != root.right:
                child_flag = lca_children(root.right, p)

            if child_flag == True:
                lca_found[0]=True
                lca_val[0] = root.val
                lca_node[0] = root
                return True
            
            return lca_parent(root.parent, root, p)

        def lca(q, p):
            """
                Function to search for p
            """
            # check the children
            if lca_children(q.left, p) == True:
                return q
            if lca_children(q.right, p) == True:
                return q
            # check the parents
            if lca_parent(q.parent, q, p) == True:
                return lca_node[0]
            
        return lca(q,p)
