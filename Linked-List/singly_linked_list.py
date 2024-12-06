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

    def insert_after(self, temp, data):
        if temp is not None:
            n=Node()



#Driver code

mylist = SinglyLinkedList()

#check if linked list is empty
print(mylist.is_empty())












