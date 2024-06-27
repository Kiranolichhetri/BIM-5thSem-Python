# 3. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Popped element: {stack.pop()}")
print(f"Is stack empty? {stack.is_empty()}")
