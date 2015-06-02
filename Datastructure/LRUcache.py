__author__ = 'effy'
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
'''
## normally a doubly linked list node is defined as follows:
class DoublyLinkedNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

# Use a modified doubly-linked list node
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        ## construct a doubly linked list, tail represent the most recent used node, head represent the
        ## least recent used node
        self.dummyNode = Node(-1,-1)
        self.tail = self.dummyNode
        self.capacity = capacity
        ## self.keyFinder is a dictionary, dict key is the key, dict value is a node of doubly linked list
        self.keyFinder = {}

    # @return an integer
    def get(self, key):
        if key not in self.keyFinder.keys():
            return -1
        else:
            self.renewOrder(key)
            return self.keyFinder[key].val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = self.keyFinder.get(key, None)
        if node is None:
            node = Node(key, value)
            self.keyFinder[key] = node
            self.tail.next = node
            node.prev = self.tail
            if self.capacity == 0:
                head = self.dummyNode.next
                self.dummyNode.next = head.next
                head.next.prev = self.dummyNode
                del self.keyFinder[head.key]
                self.capacity += 1
            self.tail = node
            self.capacity -= 1
        else:
            self.keyFinder[key].val = value
            self.renewOrder(key)


    def renewOrder(self,key):
        node = self.keyFinder[key]
        if node != self.tail:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node



class DoublyLinkedNode:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None




'''
secondround
'''
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = DoublyLinkedNode(0,0)
        self.end = DoublyLinkedNode(0,0)
        self.head.next = self.end
        self.end.prev = self.head
        self.dict = {}
        self.capacity = capacity
        self.content = 0

    def get(self,key):
        if key in self.dict:
            self.refresh(key)
            return self.dict[key].val
        else:
            return -1

    def set(self,key,val):
        if key in self.dict:
            self.refresh(key)
            self.dict[key].val = val
        else:
            self.content += 1
            if self.capacity < self.content:
                oldLRU = self.head.next
                newLRU = self.head.next.next
                self.head.next = newLRU
                newLRU.prev = self.head
                self.content -= 1
                del self.dict[oldLRU.head]
            oldmostcurrent = self.end.prev
            newmostcurrent = DoublyLinkedNode(key,val)
            newmostcurrent.next = self.end
            newmostcurrent.prev = oldmostcurrent
            self.end.prev = newmostcurrent
            oldmostcurrent.next = newmostcurrent
            self.dict[key] =newmostcurrent

    def refresh(self,key):
        node = self.dict[key]
        pre, post = node.prev, node.next
        pre.next = post
        post.prev = pre
        last_most_currente = self.end.prev
        self.end.prev = node
        node.next = self.end
        node.prev = last_most_currente
        last_most_currente.next = node
