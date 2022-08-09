class Queue:
    def __init__(self):
        self.line = list()

    def __len__(self):
        return len(self.line)

    def enqueue(self, value):
        return self.line.append(value)

    def dequeue(self):
        return self.line.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.line):
            raise IndexError
        return self.line[index]
