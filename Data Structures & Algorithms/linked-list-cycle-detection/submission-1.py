# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head 
        tracker = set()

        while tail:
            if tail in tracker:
                return True 

            tracker.add(tail)
            tail = tail.next
        return False