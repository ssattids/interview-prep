"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node == None:
            return None

        queue = [node]

        # key:val = node_val:node_reference
        copied_nodes_dict = {}
        visited = {}

        while queue != []:

            q_node = queue.pop()

            if q_node.val in visited:
                continue
            else:
                visited[q_node.val]=True

            # copy the node
            # if it copy exists, grab it from the dict
            if q_node.val in copied_nodes_dict:
                copied_q_node = copied_nodes_dict[q_node.val]
            # else create a copy and put it in the dict
            else:
                copied_q_node = Node(val=q_node.val, neighbors=None)
                copied_nodes_dict[q_node.val] = copied_q_node
            

            for neighbor_node in q_node.neighbors:
                queue.append(neighbor_node)

                if copied_q_node.neighbors == None:
                    copied_q_node.neighbors = []
                # if copy exists, grab it from the node
                if neighbor_node.val in copied_nodes_dict:
                    copied_q_node.neighbors.append(copied_nodes_dict[neighbor_node.val])
                # otherwise create a copy and add a neightbor while adding it to the dict
                else:
                    copied_neighbor_node = Node(val=neighbor_node.val, neighbors=None)
                    copied_nodes_dict[neighbor_node.val] = copied_neighbor_node
                    copied_q_node.neighbors.append(copied_neighbor_node)
                
        return copied_nodes_dict[node.val]

