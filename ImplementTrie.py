class Node:
    def __init__(self,val):
        self.val=val
        self.child={}
        self.isword=False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node('')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur=self.root
        
        for ch in word:
            if ch not in cur.child:
                cur.child[ch]=Node(ch)
                
            cur=cur.child.get(ch)
            
            
        cur.isword=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur=self.root
        
        for ch in word:
            if ch  in cur.child:
                cur=cur.child.get(ch)
            else:
                return False
        return cur.isword
                
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur=self.root
        
        for ch in prefix:
            if ch  in cur.child:
                cur=cur.child.get(ch)
            else:
                return False
            
        return True
        
