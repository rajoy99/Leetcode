# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.checker(root,-math.inf,math.inf)
        
        
    def checker(self,root,min,max):
        
        if not root:
            return True
        
        if root.val<=min or root.val>=max:
            return False
        
        return self.checker(root.left,min,root.val) and self.checker(root.right,root.val,max)
    
    
        
        