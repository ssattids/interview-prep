class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

from collections import OrderedDict

# important ordered dict methods
# Creating an empty OrderedDict
#od = OrderedDict()

# Creating an OrderedDict with initial elements
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Remove a specific item
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od.pop('a')
# od
# >> OrderedDict([('b', 2), ('c', 3)])

# Remove the last item
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od.popitem()  # By default, it removes the last item
# od
# >> OrderedDict([('a', 1), ('b', 2)])

# Remove the first item
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od.popitem(last=False)
# od
# >> OrderedDict([('b', 2), ('c', 3)])

# Move an existing key to the end
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od.move_to_end('b')
# od
# >> OrderedDict([('a', 1), ('c', 3), ('b', 2)])

# Move an existing key to the start
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od.move_to_end('b', last=False)
# od
# >> OrderedDict([('b', 2), ('a', 1), ('c', 3)])

class LRUCacheOrderedDict:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self.store.move_to_end(key)
        return self.store[key]

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.move_to_end(key)
            self.store[key] = value
        else:
            if len(self.store) == self.capacity:
                # remove the first item that was added
                self.store.popitem(last=False)
            # add the newest item at the end
            self.store[key] = value

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCacheOld:

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
