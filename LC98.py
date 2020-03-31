# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.helper(root,-math.inf,math.inf)
    
    def helper(self,root,back,forth):
        if not root:
            return True
        if root.val<=back or root.val>=forth:
            return False
        
        return self.helper(root.left,back,root.val) and self.helper(root.right,root.val,forth)
        
