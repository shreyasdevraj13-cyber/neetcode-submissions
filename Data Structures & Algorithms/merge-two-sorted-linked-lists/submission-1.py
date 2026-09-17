# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        dummy = ListNode()
        curr = dummy 

        while l1 and l2:
            if l1.val == l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                curr.next = ListNode(l2.val)
                curr = curr.next 
                l1 = l1.next
                l2 = l2.next
            
            elif l1.val < l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next 
            
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next 
                l2 = l2.next 
        
        if l1:               # If l1 has leftover nodes...
            curr.next = l1   # ...attach l1
        elif l2:             # If l2 has leftover nodes...
            curr.next = l2   # ...attach l2
        
        return dummy.next 
        


        