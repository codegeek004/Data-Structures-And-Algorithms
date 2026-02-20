class CircularQueue:
    def __init__(self, capacity=5):
        self.front = -1
        self.rear = -1
        self.new_front = -1
        self.new_rear = -1
        self.full = capacity
        self.arr = [None] * capacity

    def isempty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isfull(self):
        if self.rear >= self.full - 1:
            return True
        else:
            return False

    def enqueue(self, val):
        print(self.front, self.rear)
        print(self.new_front, self.new_rear)
        if self.isfull():
            return "Queue Overflow"
        else:
            if self.rear == len(self.arr) - 1:
                self.new_rear = 0
            else:
                self.new_rear = self.rear + 1
            self.arr[self.new_rear] = val
            self.rear = self.new_rear

    def dequeue(self):
        if self.isempty():
            return "Queue Underflow"
        else:
            if self.new_front == len(self.arr) - 1:
                self.new_front = 0
            else:
                self.new_front = self.new_front + 1
            delel = self.arr[self.new_front]
            self.front = self.new_front
            return delel

    def print_queue(self):
        print(f'self.front {self.front}', f'self.rear {self.rear}')
        print(f'self.new_front {self.new_front}',
              f'self.new_rear, {self.new_rear}')
        return self.arr


q1 = CircularQueue()
print(q1.isempty())
print(q1.enqueue(1))
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1.print_queue())
print(q1.isempty())
print(q1.isfull())
print(q1.dequeue())
print(q1.print_queue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.print_queue())
