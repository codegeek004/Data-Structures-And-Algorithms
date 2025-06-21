class Node:
    def __init__(self, prev=None, val=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

class DoublyLinkedList:
    def __init__(self, head):
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def insert_at_start(self,data):
        n = Node(data,prev,self.start)
        temp = self.head
        if not self.is_empty():
            temp.prev = n
        temp = n

    def insert_at_last(self,data):
        temp = self.head
        if temp is not None:
            while temp.next is not None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp is None:
            self.head = n
        else:
            temp.next = n

    def search(self,data):
        temp = self.head
        if temp is None:
            return temp
        while temp is not None:
            if temp.val == data:
                return temp
            temp = temp.next

    def insert_after(self, data, x):
        temp = self.head
        while temp.next is not None:
            if temp.val == x:
                n = Node(temp, data, temp.next)
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n 
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end = ' ')
            temp = temp.next
    
    def delete_first(self):
        temp = self.head
        if temp is not None:
            if temp.next is None:
                self.head = None
            else:
                temp.next.prev = None
                self.head = temp.next

    def delete_last(self):
        temp = self.head
        if temp is None:
            pass
        elif temp.next is None:
            self.head = None
        else:
            while temp.next is not None:
                temp = temp.next

            temp.prev.next = None
    def delete_node(self, data):
        temp = self.head
        if temp is None:
            pass
        else:
            while temp is not None:
                if temp.val == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        #if there is no temp.next then self.head=None
                        #this case will work if you want to delete the first node
                        self.head = temp.next
                    break
                temp = temp.next


        


