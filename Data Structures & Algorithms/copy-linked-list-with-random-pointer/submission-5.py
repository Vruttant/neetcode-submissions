"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # for debug
    def printLL(self, head):
        first = head 
        while first:
            print(first.val)
            first = first.next
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        first = second = head 
        node_set = []
        mapping_next = dict()
        mapping_random = dict()
        val_to_new_node = dict()
        while first: 
            current_node_copy = Node(x=first.val, next=first.next, random=first.random)
            node_set.append(current_node_copy)
            mapping_next[id(current_node_copy)] = first.next        # store node ref, not .val
            mapping_random[id(current_node_copy)] = first.random    # store node ref, not .val
            val_to_new_node[id(first)] = current_node_copy          # original node id -> its copy
            first = first.next

        for node in node_set:
            node.next = val_to_new_node[id(mapping_next[id(node)])] if mapping_next[id(node)] is not None else None
            node.random = val_to_new_node[id(mapping_random[id(node)])] if mapping_random[id(node)] is not None else None
        
        return node_set[0]