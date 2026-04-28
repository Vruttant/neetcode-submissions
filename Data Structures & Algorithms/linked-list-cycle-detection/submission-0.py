# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head 

        while tail:
            if "visited" in str(tail.val):
                return True 
            
            tail.val = str(tail.val) + "_visited"

            tail = tail.next

        return False