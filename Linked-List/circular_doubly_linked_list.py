class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class CircularDoublyLinkedList:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            return True
        return False
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
       
    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        if temp.val == data:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.val == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n


    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.val, end= ' ')
            temp = temp.next
            while temp is not self.start:
                print(temp.val, end = ' ')
                temp = temp.next
            print()


    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, val):
        if not self.is_empty():
            temp = self.start
            if temp.val == data:
                self.delete_first()
            else:
                temp = temp.next
            while temp is not self.start:
                if temp.val == data:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next

list1 = CircularDoublyLinkedList()
list1.insert_at_start(10)
list1.insert_at_start(20)
list1.insert_at_start(30)
list1.insert_at_start(40)
list1.insert_at_start(50)
list1.print_list()
list1.insert_at_last(14)
list1.print_list()
print(list1.search(14))





       
