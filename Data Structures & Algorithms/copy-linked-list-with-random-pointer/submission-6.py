"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None : None}

        first = head 
        while first:
            new_node = Node(first.val)
            old_to_copy[first] = new_node 
            first = first.next 
        
        first = head 
        while first: 
            new_node = old_to_copy[first]
            new_node.next = old_to_copy[first.next]
            new_node.random = old_to_copy[first.random]

            first = first.next 
        
        return old_to_copy[head]