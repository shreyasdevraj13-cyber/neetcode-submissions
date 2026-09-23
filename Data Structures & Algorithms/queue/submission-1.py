class ListNode:
    def __init__(self, val):
        self.prev = None 
        self.val = val
        self.next = None
    
    
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        before = self.tail.prev
        new_node.prev = before
        new_node.next = self.tail
        before.next = new_node
        self.tail.prev = new_node
            
    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        after = self.head.next
        new_node.prev = self.head
        new_node.next = after
        self.head.next = new_node
        after.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            before = self.tail.prev
            before.prev.next = self.tail
            self.tail.prev = before.prev
            before.prev = before.next = None
            return before.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            after = self.head.next
            after.next.prev = self.head
            self.head.next = after.next
            after.prev = after.next = None
            return after.val
        
