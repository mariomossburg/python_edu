
# Lifo
class Stack:
    def __init__(self, ) -> None:
        self.items = []
        
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    
    # using me allows you to use the print function
    def __str__(self) -> str:
        return f"Stack: {list((self.items))}"
    
    
    
s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.pop() # I pop the first item  first item 
print(s)