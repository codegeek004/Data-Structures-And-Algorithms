class Deque:
    def __init__(self):
        self.list1 = []
        self.front = None
        self.rear = None

    def is_empty(self):
        return len(self.list1) == 0

    def insert_at_front(self, data):
        self.list1.insert(0,data)

    def insert_at_rear(self, data):
        self.list1.append(data)

    def delete_at_front(self):
        self.list1.pop(0)

    def delete_at_rear(self):
        self.list1.pop(-1)

    def get_front(self):
        return self.list1[0]
    
    def get_rear(self):
        return self.list1[-1]

    def size(self):
        return len(self.list1)

d1 = Deque()
d1.insert_at_front(10)
d1.insert_at_front(20)
d1.insert_at_rear(30)
d1.insert_at_rear(40)
print(d1.size())
d1.delete_at_front()
d1.delete_at_rear()
print(d1.get_front())
print(d1.get_rear())



