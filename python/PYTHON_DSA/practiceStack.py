class stck:
    def __init__(self):
        self.element =[]

    def isEmpty(self):
        if ( len(self.element)==0):
            return True
        
    def PUSH(self , element):
        self.element.append(element)

    def POP(self):
        if(self.isEmpty()==True):
            return print("Stack is Empty")
        else:
            return self.element.pop()
      

        
    def SIZE(self):
        return len(self.element)    
    
    def PEAK(self):
      
        return self.element[-1]
    



stack = stck()
stack.PUSH(1)
stack.PUSH(2)
stack.PUSH(3)
stack.PUSH(4)
print(stack.SIZE())
print (stack.POP())

print(stack.POP())
print(stack.PEAK())


 

 

