# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res=-math.inf
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        
        self.res=max(self.res,root.val+left+right)
        return max(0,root.val+max(left,right))
        
