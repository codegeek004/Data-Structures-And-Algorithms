class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.count = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.count == 0

    def insert_front(self, data):
        n = Node(data, None, self.front)
        if self.is_empty(): 
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.count += 1

    def insert_rear(self, data):
        n = Node(data, self.rear, None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count += 1

    def delete_front(self):
        if not self.is_empty():
            if not self.front.next:
                self.front = None
                self.rear = None
            else:
                self.front.next.prev = None
                self.front = self.front.next
            self.count -= 1
        else:
            raise IndexError("Queue is empty")

    def delete_rear(self):
        if not self.is_empty():
            if not self.rear.prev:
                self.front = None
                self.rear = None
            else:
                self.rear.prev.next = None
                self.rear = self.rear.prev
            self.count -= 1
        else:
            raise IndexError("Queue is empty")

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.val
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.rear.val
    
    def size(self):
        return self.count

d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front())
print(d1.get_rear())
print(d1.size())
d1.delete_front()
d1.delete_rear()
print(d1.get_front())
print(d1.get_rear())
print(d1.size())






