# stack -> Last in First Out
# queue -> First in First out


class Queue:
    def __init__(self):
        self.items = []

    def is_emplyt(self):
        return self.items == []

    def entry_queue(self, item):
        self.items.insert(0, item)

    def delete_queue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

'''
q = Queue()

q.entry_queue(1)
q.entry_queue(2)
q.entry_queue(3)
q.entry_queue(4)
q.entry_queue(5)

print(q.size())
print(q.items)

print(q.delete_queue())
print(q.delete_queue())

print(q.items)
'''


