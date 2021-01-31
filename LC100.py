# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        treeA=[]
        treeB=[]
        
        q=[]
        
        def getarray(root):
            
            if not root:
                return []
            res=[]
            q=[root]
            
            while q:
                ans=[]
                for i in range(len(q)):
                    a=q.pop(0)
                    ans.append(a)
                    if a.left:
                        q.append(a.left)
                    if a.right:
                        q.append(a.right)
                res.append(ans)
            
            return res
        
        treeA=getarray(p)
        treeB=getarray(q)
        
        if len(treeA)!=len(treeB):
            return False
        m=len(treeA)
        for i in range(m):
            if len(treeA[i])!=len(treeB[i]):
                return False
            for j in range(len(treeA[i])):
                if treeA[i][j]!=treeB[i][j]:
                    return False
                
        return True
            
        
