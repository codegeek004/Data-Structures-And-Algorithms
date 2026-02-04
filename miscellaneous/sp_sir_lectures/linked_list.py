class ArrayLinkedList:
    def __init__(self):
        self.arr = []          # [[val, next_index]]
        self.head = -1         # index of head node

    def insert(self, val, pos=-1):
        new_node = [val, -1]
        new_index = len(self.arr)
        self.arr.append(new_node)

        # empty list
        if self.head == -1:
            self.head = new_index
            return

        # insert at head
        if pos == 0:
            new_node[1] = self.head
            self.head = new_index
            return

        # insert at end (default)
        if pos == -1:
            cur = self.head
            while self.arr[cur][1] != -1:
                cur = self.arr[cur][1]
            self.arr[cur][1] = new_index
            return

        # insert at position
        cur = self.head
        for _ in range(pos - 1):
            if self.arr[cur][1] == -1:
                break
            cur = self.arr[cur][1]

        new_node[1] = self.arr[cur][1]
        self.arr[cur][1] = new_index

    def remove(self, pos=0):
        if self.head == -1:
            return

        # remove head
        if pos == 0:
            self.head = self.arr[self.head][1]
            return

        cur = self.head
        for _ in range(pos - 1):
            if self.arr[cur][1] == -1:
                return
            cur = self.arr[cur][1]

        next_node = self.arr[cur][1]
        if next_node != -1:
            self.arr[cur][1] = self.arr[next_node][1]

    def print_list(self):
        cur = self.head
        while cur != -1:
            print(self.arr[cur][0], end=" -> ")
            cur = self.arr[cur][1]
        print("None")


ll = ArrayLinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3, 0)
ll.insert(4, 1)
ll.insert("yash", 2)

ll.print_list()
print(ll.arr)
