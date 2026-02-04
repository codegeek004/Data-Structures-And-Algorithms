class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.arr = []
        self.head = None

    def insert(self, val, pos=-1):
        last_idx = len(self.arr)
        new_node = [val, self.next]
        self.arr.insert(pos, new_node)
        # self.head = x
        if pos == -1:
            pos = last_idx
            # self.arr[pos][1] = None

            if len(self.arr) <= 1:
                self.arr[pos-1][1] = None
            else:
                print('else mai gaya')
                self.arr[pos-1][1] = id(new_node)

        elif pos == 0:
            # self.next = id(self.arr[0])
            self.arr[pos][1] = id(self.arr[1])
        else:
            # self.next = id(self.arr[pos])
            self.arr[pos][1] = id(self.arr[pos+1])

    def remove(self, pos):
        self.arr.pop(0)

    # def print_list(self):
    #     while self.arr.nexr


list1 = LinkedList()

list1.insert(1)
list1.insert(2)
list1.insert(3, 0)
list1.insert(4, 1)
list1.insert('yash', 2)
print(list1.arr)
