class Node :
    def __init__(self , item=None , next=None):
        self.item=item
        self.next=next

class LinkedList:
    def __init__(self , start=None):
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insertAtStart(self , data):
        node=Node(data , self.start)
        self.start=node
        
        
    def inserAtLast(self , data):
        node = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                temp=temp.next 
                
            temp.next=node    
        else:
            self.start=node
 
        
            
    def search(self , data):
        temp = self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None    
    
            
    def insertAfter(self , temp , data):
         if temp is not None:
             node =Node(data , temp.next )
             temp.next=node
            
    def display(self):
        temp = self.start
        while temp is not None :
            print(temp.item  , end=" ")
            temp = temp.next   
             
                
    def deleteFirst(self):
        if self.start is not None:
            self.start=self.start.next
                        
    def deleteAtLast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start.next=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next    
            temp.next=None            
            
            
    def deleteItem(self , data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data :
                self.start=None
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next 
                    break
                temp=temp.next            
            
# Driver Code

list = LinkedList()
list.insertAtStart(2)   
list.insertAtStart(1)   
list.insertAtStart(0)   
list.insertAtStart(5)   
list.insertAtStart(8)   
list.insertAtStart(10) 
list.display()
list.inserAtLast(3)          
list.inserAtLast(4)    
list.inserAtLast(5)    
list.display()
list.deleteFirst()
list.display()
list.deleteAtLast()
list.display()
print(list.search(2))
list.display()

