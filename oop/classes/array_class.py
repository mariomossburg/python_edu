from typing import Any, Optional

# Array Pros:
# Accessing any index == 0(1) -- constant time 
# Cache friendly(contigous memory)... faster iteration


# Cons:
# Fixed size(), python lists are dynamic arrays, so appending is 0(1) -- constant time
# slow insert and delete in the middle, requires shifting   -- 0(n) -- linear time 



class Array: 
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.length: int = 0
        self.data: list[Optional[Any]] = [None] * capacity

    def get(self, index: int) ->Any:
        if 0 <= index < self.length:
            return self.data[index]
        raise IndexError("Index is out of bounds")
    
    def set(self, index: int, value: Any)-> None:
        if 0 <= index < self.length:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def append(self, value: Any) -> None:
        if self.length < self.capacity:
            self.data[self.length] = value
            self.length += 1
        else:
            raise OverflowError("Array is full")
        

    def insert(self, index: int, value: Any)-> None:
        if self.length >= self.capacity:
            raise OverflowError('Array is Full')
        if not (0 <= index <= self.length):
            raise IndexError('Index is out of bounds')
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.length +=1

    def delete(self, index: int)-> None:
        if 0 <= index < self.length:
            for i in range(index, self.length - 1):
                self.data[i] = self.data[i + 1]
            self.data[self.length - 1] = None
            self.length -= 1
        else:
            raise IndexError('Index out of bounds')
        
    def __str__(self) -> str:
        return str([self.data[i] for i in range(self.length)])
    


# Cache & cookies

        