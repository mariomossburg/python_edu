
"""
define another stack where the node holds the min
"""
class Minstack:
    def __init__(self) -> None:
        self.items = []
        self.min_items = []
        
    def push(self, val):
        self.items.append(val)
        val = min(val, self.min_items[-1] if self.min_items else val)
        self.min_items.append(val)
    
    def pop(self):
        self.items.pop()
        self.min_items.pop()
        
    def top(self)-> int:
        return self.items[-1]
    
    def getmin(self) -> int:
        return self.min_items[-1]
    


        
