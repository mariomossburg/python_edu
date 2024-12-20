class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    
    def your_age(self):
        return (f"you are {self.age} years old")
    
    
    def your_name(self):
        return(f"your name is {self.name}")
    
    # does not rely on self, don't have access to class or instance
    # atttibutes 
    @staticmethod
    def static_method():
        return ('i am a MR. static')
    

a = Animal("tee", 15)
print(a.your_age())
print(a.your_name())
print(a.static_method())