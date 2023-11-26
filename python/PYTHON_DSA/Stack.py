#Stack Implementation :- 
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.items)

# Example usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Stack size:", my_stack.size())
print("Top element:", my_stack.peek())
while not my_stack.is_empty():
    print("Popped:", my_stack.pop())
print("Stack size after popping all elements:", my_stack.size())
