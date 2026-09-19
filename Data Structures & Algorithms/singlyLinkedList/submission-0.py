class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
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
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next 
        

    def remove(self, index: int) -> bool:
        if index < 0:
            return False

        temp = self.head
        i = 0
        while i < index and temp:
            temp = temp.next
            i += 1

        if not temp or not temp.next:
            return False
        
        curr = temp.next
        temp.next = curr.next 
        curr.next = None

        if not temp.next:
            self.tail = temp
        return True
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next 
        return res 

        
