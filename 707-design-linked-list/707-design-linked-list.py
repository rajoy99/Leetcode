class Node:
    
    def __init__(self,val):
        self.val=val
        self.next=None


class MyLinkedList:

    def __init__(self):
        
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        
        if index<0 or index>=self.size:
            return -1
        if self.head is None:
            return -1
        
        cur=self.head
        for i in range(index):
            cur=cur.next
        return cur.val
            
        

    def addAtHead(self, val: int) -> None:
        

        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        
        cur=self.head
        
        if cur is None:
            self.head=Node(val)
        else:
            while cur.next is not None:
                cur=cur.next
            cur.next=Node(val)
        self.size+=1
        
            
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index<0 or index>self.size:
            return
        cur=self.head
        
        if index==0:
            self.addAtHead(val)
        else:
            for i in range(index-1):
                cur=cur.next
            newnode=Node(val)
            newnode.next=cur.next
            cur.next=newnode
            
        self.size +=1
        
            
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index<0 or index>=self.size:
            return
        
        if index==0:
            self.head=self.head.next
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            cur.next=cur.next.next
        self.size -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)