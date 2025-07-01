# space complexity --> O(n)
# time complexity --> enqueue - O(1)
#                     dequeue - O(1)
#                     dequeue - O(1)
#                     isEmpty - O(1)
#                     isFull - O(1)
#                     size - O(1)
#                     deleteQueue - O(1)

class Queue:
    def __init__(self):
        self.list1 = []
        self.front = None
        self.rear = None

    def is_empty(self):
       return len(self.list1) == 0 

    def enqueue(self, data):
        self.list1.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.list1.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.list1[0]
        else:
            raise IndexError("Queue Underflow")

    def get_rear(self):
        if not self.is_empty():
            return self.list1[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.list1)


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.get_front())
q1.dequeue()
print(q1.size())
print(q1.get_front())
print(q1.get_rear())



