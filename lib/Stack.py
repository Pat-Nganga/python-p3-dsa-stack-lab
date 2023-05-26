class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, item):
          if len(self.items) < self.limit:
            self.items.append(item)
            
    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for index, value in enumerate(self.items[::-1]):
            if value == target:
                return index
        return -1
