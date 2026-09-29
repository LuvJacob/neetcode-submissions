class DoublyNode:
    def __init__(self, key= None, val= None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = DoublyNode()
        self.right = DoublyNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev

        prev = self.right.prev 

        prev.next = node
        
        node.prev = prev
        node.next = self.right

        self.right.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache.pop(key)

            old.prev.next = old.next
            old.next.prev = old.prev
        node = DoublyNode(key, value)

        self.cache[key] = node

        prev = self.right.prev

        prev.next = node

        node.prev = prev
        node.next = self.right

        self.right.prev = node

        if self.capacity < len(self.cache):
            old = self.left.next

            old.prev.next = old.next
            old.next.prev = old.prev

            self.cache.pop(old.key)
        
        
