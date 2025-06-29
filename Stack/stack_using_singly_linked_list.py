class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.top == None

    def push(self, data):
        n = Node(data, self.top)
        self.top = n
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.top.val
            self.top = self.top.next
            self.count -= 1
            return data
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.val
        else:
            raise self.is_empty()

    def size(self):
        return self.count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print(s1.peek())
print(s1.size())
s1.pop()
print(s1.peek())
print(s1.size())


