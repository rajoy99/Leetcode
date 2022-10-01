class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordlist=set(wordList)
        q=[(beginWord,1)]
        
        for word,d in q:
            if word==endWord:
                return d
            
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    temp=word[:i]+char+word[i+1:]
                    if temp in wordlist:
                        q.append([temp,d+1])
                        wordlist.remove(temp)
                        
        return 0
                        
                        