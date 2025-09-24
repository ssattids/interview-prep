"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def copyRandomList(self, head: Node) -> Node:
        """
        most optimal solution
        time complexity: O(n)
        space: O(1) ...(if we don't count the additional space we need for the new linked list)
        """
        if head == None:
            return None
        
        # one large linked list
        current = head
        while (current!=None):
            current_copy = Node(current.val)
            current_copy.next = current.next
            current.next = current_copy
            current = current.next.next

        # link the randoms
        current = head
        while (current!=None):
            if current.random != None:
                current.next.random = current.random.next
            current = current.next.next
        
        # disconnect the linked lists
        current = head
        head_copy = head.next
        while(current!=None):
            copy_node = current.next

            current.next = current.next.next
            if copy_node.next != None:
                copy_node.next = copy_node.next.next

            current = current.next
            
        return head_copy

    def copyRandomListRecursive(self, head: Node) -> Node:
        """
        recursive solution
        time complexity: O(n)
        space complexity: O(n)
        """
        self.visited_hash = {}
        def cpRndRec(head):
            if head == None:
                return None
            if head in self.visited_hash:
                return self.visited_hash[head]

            node = Node(head.val, None, None)
            self.visited_hash[head] = node

            node.next = cpRndRec(head.next)
            node.random = cpRndRec(head.random)
            return node

        return cpRndRec(head)

    def copyRandomListIterative2(self, head: Node) -> Node:
        """
        Iterative solution (simpler)
        time complexity: O(n)
        space complexity: O(n)
        """
        if head == None:
            return None

        current = head
        head_copy = Node(current.val, None, None)
        current_copy = head_copy
        visited = {}
        while current != None:

            visited[current] = current_copy
            if current.next != None:
                current_copy.next = Node(current.next.val, None, None)
            
            current = current.next
            current_copy = current_copy.next
        
        current = head
        current_copy = head_copy
        while current != None:
            current_copy.random = visited.get(current.random, None)
            current = current.next
            current_copy = current_copy.next

        return head_copy

    def copyRandomListIterative(self, head: Node) -> Node:
        """
        Iterative solution
        time complexity: O(n)
        space complexity: O(n)
        """
        if head == None:
            return None
        current = head
        dict_address_index = {}
        dict_index_address_copy = {}

        copy_head = Node(head.val)
        copy_current = copy_head

        # initial deep copy
        current = head
        i=0
        while current != None:
            dict_address_index[current] = i
            dict_index_address_copy[i] = copy_current
            i+=1
            # link the next node to the current node
            if current.next != None:
                copy_current_next = Node(current.next.val)
                copy_current.next = copy_current_next
            
            current = current.next
            copy_current = copy_current.next
        
        # copy of the random
        current = head
        copy_current = copy_head
        i=0
        while current != None:
            # at what index does the original.random point to
            if current.random == None:
                copy_current.random = None
            else:
                index = dict_address_index[current.random]
                copy_current.random = dict_index_address_copy[index]
            current = current.next
            copy_current = copy_current.next

        return copy_head
    

# %%
# [[7,null],[13,0],[11,4],[10,2],[1,0]]
Node1 = Node(7)
Node2 = Node(13)
Node3 = Node(11)
Node4 = Node(10)
Node5 = Node(1)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5  
Node1.random = None
Node2.random = Node1
Node3.random = Node5
Node4.random = Node3
Node5.random = Node1

solution = Solution()
head = solution.copyRandomList(Node1)

current = head
while(current!=None):
    print("Val:", current.val, "Random:", current.random.val if current.random!=None else None)
    current = current.next

# %%