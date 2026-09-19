class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next 
            i += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        new_node.prev = self.head

        if self.head.next:
            self.head.next.prev = new_node
        else:
            self.tail = new_node
        self.head.next = new_node
        
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node 
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        i = 0 
        while i < index and curr:
            curr = curr.next 
            i += 1
        
        if not curr:
            return 
        new_node = ListNode(val)
        new_node.prev = curr
        new_node.next = curr.next
        curr.next = new_node

        if new_node.next:
            new_node.next.prev = new_node

        else:
            self.tail = new_node
            
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = 0 
        while i < index and curr:
            curr = curr.next 
            i += 1
        
        if curr and curr.next:
            curr2 = curr.next 
            curr.next = curr2.next

            if curr2.next:
                curr2.next.prev = curr 
            else:
                self.tail = curr
            curr2.prev = curr2.next = None 

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)