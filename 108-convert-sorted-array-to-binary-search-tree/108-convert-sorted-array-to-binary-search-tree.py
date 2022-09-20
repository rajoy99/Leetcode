# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def helper(nums):
            
            if not nums:
                return None
            
            median=len(nums)//2
            
            root=TreeNode(val=nums[median])
            
            root.left=helper(nums[:median])
            root.right=helper(nums[median+1:])
            
            return root

        return helper(nums)
        