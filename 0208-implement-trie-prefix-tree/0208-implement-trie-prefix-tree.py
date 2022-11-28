class Node:
    
    def __init__(self,isWord=False):
        self.val=''
        self.child={}
        self.isWord=isWord


class Trie:

    def __init__(self):
        self.root=Node('')
        

    def insert(self, word: str) -> None:
        cur=self.root
        
        for c in word:
            if c not in cur.child:
                cur.child[c]=Node(c)
            cur=cur.child.get(c)
        
        cur.isWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        
        for c in word:
            if c in cur.child:
                cur=cur.child.get(c)
            else:
                return False
            
        return cur.isWord==True
                

    def startsWith(self, prefix: str) -> bool:
        
        cur=self.root
        
        for c in prefix:
            if c in cur.child:
                cur=cur.child.get(c)
            else:
                return False
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)