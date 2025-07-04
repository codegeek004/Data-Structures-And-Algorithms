# space complexity --> push n elements - O(n)
# time complexity --> push - O(1)
#                     pop - O(1)
#                     size - O(1)
#                     isEmpty - O(1)
#                     isFull - O(1)
#                     deleteStack - O(1)
class Stack:
    def __init__(self):
        self.list = []


    def is_empty(self):
        return len(self.list) == 0

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.list)
    
    def deleteStack(self):
        if not self.isEmpty():
            return self.list.clear()

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(10)
print(s1.peek())
print(s1.size())
s1.pop()
print(s1.peek())


