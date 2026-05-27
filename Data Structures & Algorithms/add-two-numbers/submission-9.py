# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        ptr1, ptr2, ptr3 = l1, l2, l3 
        carry = 0

        while ptr1 is not None or ptr2 is not None or carry: 
            val1 = ptr1.val if ptr1 else 0 
            val2 = ptr2.val if ptr2 else 0 

            summation = val1 + val2 + carry 
            carry = summation // 10 

            ptr3.next = ListNode(summation % 10)
            ptr3 = ptr3.next 

            ptr1 = ptr1.next if ptr1 else None 
            ptr2 = ptr2.next if ptr2 else None 
        
        return l3.next