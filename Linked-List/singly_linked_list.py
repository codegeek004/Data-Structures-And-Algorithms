#list of linear collection of data items also called list items.
#example1: list of marks (type -> int) 
# 30, 32, 36, 60

#example2: list of city names (type -> str)
# indore, pune, bangalore, hyderabad, delhi

#example3: list of employees (type -> employee)
# id_100:name_Yash:salary_25000, id_24:name_Ajay:salary_30000, id_13:name_Gurpreet:salary_40000

#statically_typed langauges -> You have to define the datatypes you are using. 
# For example, string name = "yash", int arr[a] = [1,2,3,4,5]

#dynamically typed langauges -> You need not to define the datatypes. You can use multiple.datatypes in the same variable.
# For example, name = "yash", list1 = ['yash', 12, True, 12.55]

# del keyword deletes the reference variable not the object.

###########################################################################################

# node : type of all objects in a linked list where we store the item and reference to the next.
# |Start=0| --> |[item][next=2]| --> |[item][next=3]| --> |[item][next=None]|

#Singly linked list 
#     1. Each node has a single link to the next. It
#     2. It is flexible. It can grow and shrink

# operations: 
#     1. insertion
#     2. deletion
#     3. is_empty
#     4. traverse


###########################################################################################

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        #this stores the reference to the first node
        self.head = head
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_start(self,val):
        #Store the value inside a new node temp
        temp = Node(val, self.head)
        #Reference the new node temp with head 
        self.head = temp
  
    def insert_at_last(self, val):
        n = Node(val, next=None)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.head = n

    def search(self, val):
        if not self.is_empty():
            temp = self.head
            while temp is not None:
                if temp.data == val:
                    return temp
                temp = temp.next
            return "Data not found"
        else:
            return "Linked List is empty"
    
    def insert_after(self, val, x):
        temp = self.head
        if temp is not None:
            while temp is not None:
                if temp.data == x:
                    n = Node(val, next=temp.next)
                    temp.next = n
                    return "Node inserted successfully"
                temp = temp.next
        else:
            return "Node not found"
    
    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
                break
            temp.next = None
    
    def delete_item(self, val):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.data == val:
                self.head = None
        else:
            temp = self.head
            if temp.data == val:
                self.head = temp.next
            else:
                while temp.next is not None:
                    if temp.next.data == val:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    # making linked list iterable
    def __iter__(self):
        return Iterator(self.head)


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

#Making linked list object iterable
class Iterator:
    def __init__(self, current):
        self.current = current
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


list1 = SinglyLinkedList()
list1.insert_at_start(10)
list1.insert_at_start(20)
list1.insert_at_last(30)
list1.insert_after(5,20)
list1.print_list()
print()
print('after delete first')
list1.delete_first()
list1.print_list()
print()
print('delete item')
list1.delete_item(5)
list1.print_list()
print()
print('after delete last')
list1.delete_last()
list1.print_list()

print()
print('sabse niche')
for i in list1:
    print(i, end = ' ')



