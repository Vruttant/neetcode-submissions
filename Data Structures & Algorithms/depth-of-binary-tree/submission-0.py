# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root, depth=0):
            if root is None: 
                return depth 
            
            left = rec(root.left, depth=depth + 1)
            right = rec(root.right, depth=depth + 1)
        
            return max(left, right)
        
        return rec(root)