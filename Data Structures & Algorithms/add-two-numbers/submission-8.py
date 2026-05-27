# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        dummy = new_list
        ptr1 = l1 
        ptr2 = l2 
        carry = 0 

        while ptr1 is not None or ptr2 is not None: 
            val1 = ptr1.val if ptr1 else 0 
            val2 = ptr2.val if ptr2 else 0 

            current_sum = val1 + val2 
            current_sum += carry 

            print(current_sum)                                                        

            carry = current_sum // 10 
                
            

            dummy.next = ListNode(current_sum % 10)
            dummy = dummy.next
            
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None 

        if carry:
            dummy.next = ListNode(val=carry, next=None)

        return new_list.next


