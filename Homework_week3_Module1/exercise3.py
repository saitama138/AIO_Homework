class MyStack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self, x):
        if not self.is_full():
            self.stack.append(x)
        else:
            raise Exception("Stack is full")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")
