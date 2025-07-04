class Node:
    def __init__(self, val=None, priority=None, next=None):
        self.val = val
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.count = 0
        
    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.count += 1
    
    def is_empty(self):
        return self.start == None

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")

        data = self.start.val
        self.start = self.start.next
        self.count -= 1
        return data

    def size(self):
        return self.count

    
p1 = PriorityQueue()
p1 = PriorityQueue()
p1.push("yash", 4)
p1.push("ajay", 2)
p1.push("akshay", 1)
p1.push("shashi", 3)
while not p1.is_empty():
    print(p1.pop())



