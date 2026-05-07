# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]):
        first = head 
        prev = None 
        while first:
            tmp = first.next 
            first.next = prev 
            prev = first 
            first = tmp 
        


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the number of nodes 
        # reverse the linked list 
        # remove the ith node 
        # reverse the linked list again 
        
        # count the number of nodes in LL 
        i = 0 

        first = second = head 

        while first:
            i += 1
            first = first.next 
        
        
        # # print(ll_len)
        # prev = None 
        # while second: 
        #     if i == ll_len - n:
        #         prev.next = second.next 
        #         return head 
        #     prev = second 
        #     second = second.next
        #     i -= 1 

        t_node_idx = i - n 

        prev = None 
        while second:
            if i == n:
                if prev is None: 
                    return head.next 
                prev.next = second.next
                return head 
            prev = second
            second = second.next 
            i -= 1

