class Queue:    
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.times)