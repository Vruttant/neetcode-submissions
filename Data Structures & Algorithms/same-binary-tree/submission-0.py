# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(p, q):
            if p is not None and q is not None:
                if p.val == q.val:
                    left = rec(p.left, q.left)
                    right = rec(p.right, q.right)
                else:
                    return False
                
                return left and right
            elif p is None and q is None:
                return True 
            else:
                return False

        return rec(p, q)
        
            
