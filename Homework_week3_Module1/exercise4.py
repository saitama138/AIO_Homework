class MyQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def enqueue(self, x):
        if not self.is_full():
            self.stack.append(x)
        else:
            raise Exception("Stack is full")
    
    def dequeue(self):
        if not self.is_empty():
            return self.stack[0].pop()
        else:
            raise Exception("Stack is empty")
    
    def front(self):
        if not self.is_empty():
            return self.stack[0]
        else:
            raise Exception("Stack is empty")
