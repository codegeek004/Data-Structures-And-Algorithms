class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class CircularLinkedList:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        if self.last is None:
            return True
        return False
        
    
    def insert_at_first(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n

        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    
    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.val == data:
                return temp
            temp = temp.next
        if temp.val == data:
            return temp
        return None

    def insert_after(self, data, x):
        temp = self.last.next
        while temp != self.last:
            if temp.val == x:
                n = Node(data, temp.next)
                temp.next = n

                if temp == self.last:
                    self.last = n

            temp = temp.next
        
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last=None
            else:
                temp = self.last.next
                self.last.next = temp.next
    
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last=None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_data(self, data):
        temp = self.last.next
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                if temp.val == data:
                    self.last.next = self.last.next.next
                else:
                    while temp != self.last:
                        if temp.next == self.last:
                            if temp.next.val == data:
                                self.delete_last()
                                break
                        if temp.next.val == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next
                    

    def print_list(self):
        temp = self.last.next
        if not self.is_empty():
            while temp != self.last:
                print(temp.val, end=' ')
                temp = temp.next
            print(temp.val)


list1 = CircularLinkedList()
list1.insert_at_first(10)
list1.insert_at_first(20)
list1.insert_at_first(30)
list1.insert_at_first(40)
list1.insert_at_first(50)
list1.print_list()
list1.insert_at_last(100)
list1.print_list()
print(list1.search(30))
list1.insert_after(105,40)
list1.print_list()
list1.delete_first()
list1.print_list()
list1.delete_last()
print('delete last')
list1.print_list()
print('delete data')
list1.delete_data(105)
list1.print_list()
