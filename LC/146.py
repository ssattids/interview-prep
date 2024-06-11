class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict_memory_address = {}
        self.head = None
        self.tail = None
    
    def add_node_to_LL_start(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head=node
    
    def remove_node(self, node):
        # if at the start
        if node.prev == None:
            # if there is only one node
            if self.head.next == None:
                self.head = None
                self.tail = None
            # if there is more than one node
            else:
                next_node = node.next
                self.head = next_node
                node.next = None
                next_node.prev = None

        # if at the end
        elif node.next == None:
            self.tail = node.prev # move tail the 2nd last last node
            node.prev.next = None # make the 2nd last node the last node
            node.prev = None # sever the link with the linked list
        # remove from the middle
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            
            node.prev = None # sever the links
            node.next = None # sever the links

    def get(self, key: int) -> int:
        if key not in self.dict_memory_address:
            return -1

        key_node = self.dict_memory_address[key]
        self.remove_node(key_node)
        self.add_node_to_LL_start(key_node)
        return key_node.val

        
    def put(self, key: int, value: int) -> None:
        # if it is in the dict already, update the value and put in the front
        if key in self.dict_memory_address:
            key_node = self.dict_memory_address[key]
            key_node.val = value
            self.remove_node(key_node)
            self.add_node_to_LL_start(key_node)
        else:
            new_node = Node(key, value)
            self.dict_memory_address[key] = new_node
            # check if there is space for the new nede, if there is add it in the beginning
            if len(self.dict_memory_address) <= self.capacity:
                self.add_node_to_LL_start(new_node)
            # otherwise evict the last element and then add the new ndoe
            else:
                del self.dict_memory_address[self.tail.key]
                self.remove_node(self.tail)
                self.add_node_to_LL_start(new_node)
