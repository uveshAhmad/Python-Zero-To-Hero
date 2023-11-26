class Queue:
    def __init__(self):
       list =[]
    def isFull(self):
       if(len(self.list)==0):
         return False   
       else:
         return True
    
    def PUSH(self , element):
        return self.list.append(element)
     
     
    def POP(self):
       if ( self.isFull()==True):
          print("Stack is empty")
       else:
          return self.list.pop()
       
             
    def SIZE(self):
         return len(self.list)

    def PEAK(self):
       return self.list[0]
       
       