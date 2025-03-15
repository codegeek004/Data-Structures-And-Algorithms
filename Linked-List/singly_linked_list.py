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
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class SinglyLinkedList:
    def __init__(self, start=None):
        self.start=start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        #pass the value of n in start if you are inserting from start
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)# here i have not passed any argument that means none will be passed
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start=n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data): #using temp I am passing the reference of the node after which I have to insert the data
        #first search the node after which you have to insert the new value using the search method
        if temp is not None:
            n=Node(data, temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = ' ')
            temp = temp.next

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next=None

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next=temp.next.next
                        break
                    temp = temp.next


    def __iter__(self):
        return sll_iterator(self.start)


#Driver code
mylist = SinglyLinkedList()

mylist.insert_at_start(14)
mylist.insert_at_last(20)
mylist.insert_at_start(4)
mylist.insert_after(mylist.search(14), 144)
mylist.print_list()

print()
mylist.delete_item(144)
mylist.print_list()
print()


###iterating through the ll
class sll_iterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data



for x in mylist:
    print(x, end=' ')


