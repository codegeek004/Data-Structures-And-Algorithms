class PriorityQueue:
    def __init__(self):
        self.list1 = []

    def push(self, data, priority):
        i = 0
        while i<len(self.list1) and self.list1[i][1]<=priority:
            i+=1
        self.list1.insert(i, (data, priority))
    
    def is_empty(self):
        return len(self.list1) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.list1.pop(0)[0]
    
    def size(self):
        return len(self.list1)
p1 = PriorityQueue()
p1.push("yash", 4)
p1.push("Ajay", 2)
p1.push("Robert", 1)
p1.push("Jaferine", 3)
while not p1.is_empty():
    print(p1.pop())

