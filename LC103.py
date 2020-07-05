class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        
        res=[]
        
        while q:
            ans=[]
            for _ in range(len(q)):
                node=q.pop(0)
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        
        for i in range(len(res)):
            if i%2==1:
                res[i].reverse()
        return res
            
        
