class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self, start=None):
        self.front = None
        self.rear = None 
        self.count = 0
    
    def is_empty(self):
        #return self.front == None
        #return self.rear == None
        return self.count == 0
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.count += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.count -= 1


    def get_front(self):
        if not self.is_empty():
            return self.front.val
        else:
            raise IndexError("Stack Underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.val
        else:
            raise IndexError("Stack Underflow")
    
    def size(self):
        return self.count


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.get_front())

