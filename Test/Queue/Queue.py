class Queue:
    def __int__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequenue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
