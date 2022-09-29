class Node:
    def __init__(self,val,isWord=False):
        self.val=val
        self.child={}
        self.isWord=isWord

class Trie:

    def __init__(self):
        self.root=Node('')
        
        

    def insert(self, word: str) -> None:
        
        cur=self.root
        
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node(ch)
            cur=cur.child.get(ch)
            
        cur.isWord=True

    def search(self, word: str) -> bool:
        
        cur=self.root
        
        for ch in word:
            if ch in cur.child:
                cur=cur.child.get(ch)
            else:
                return False
            
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        
        cur=self.root
        
        for ch in prefix:
            if ch in cur.child:
                cur=cur.child.get(ch)
            else:
                return False
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)