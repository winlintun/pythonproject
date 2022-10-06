from Queue import Queue

class PQueue:
    def __init__(self):
        self.items = {} # empyt dictionary

    def is_empty(self):
        return len(self.items) == 0

    def ent_queue(self, item):
        if priority not in self.items:
            self.items[priority] = Queue()
            # item[priority=key] = Queue=value // item{priority:Queue}
        queue = self.items[priority]
        queue.ent_queue(item)

    def del_queue(self):
        keys = list(self.items.keys())

