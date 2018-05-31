class Stack:

    def __init__(self):
        self.data = []
        self.len = 0

    def push(self, x):
        self.data.append(x)
        self.len += 1

    def pop(self):
        if self.len > 0:
            temp = self.data[self.len - 1]
            self.len -= 1
            self.data.remove(temp)
            return temp
        else:
            return None

class Queue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        if self.s2.len > 0:
            return self.s2.pop()
        elif self.s1.len > 0:
            for _ in range(self.s1.len):
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return None

q = Queue()
q.push(1)
q.push(2)
q.push(3)

for _ in range(4):
    print(q.pop())
