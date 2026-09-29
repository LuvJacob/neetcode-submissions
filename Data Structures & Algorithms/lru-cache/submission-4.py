class DoublyNode:
    def __init__(self,key= None,  val= None, prev=None, next= None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
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
        else:
            node = self.cache[key]
            

            node.prev.next = node.next
            node.next.prev = node.prev

            prev = self.right.prev
            prev.next = node
            
            node.next = self.right
            node.prev = prev
            self.right.prev = node
            return node.val

        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache.pop(key)
            old.prev.next = old.next
            old.next.prev = old.prev
        node = DoublyNode(key, value)
        prev = self.right.prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev

        self.cache[key] = node

        if self.capacity < len(self.cache):
            old = self.left.next
            nxt = self.left.next.next
            self.left.next = nxt
            self.left.next.prev = self.left
            self.cache.pop(old.key)

         
        
