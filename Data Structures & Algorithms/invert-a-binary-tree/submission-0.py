# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root1: Optional[TreeNode]) -> Optional[TreeNode]:
        
        root = root1 
        def rec(root):
            if root is None:
                return 
            
            tmp_left = root.left
            root.left = root.right
            root.right = tmp_left 

            left = rec(root.left)
            right = rec(root.right)
        
        rec(root)

        return root1