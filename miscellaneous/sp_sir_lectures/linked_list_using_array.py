class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        self.arr = []
        self.head = None

    def insert(self, val, pos=-1):
        last_idx = len(self.arr)
        new_node = [val, self.next]
        # self.arr.insert(pos, new_node)
        # self.head = x
        if pos == -1:
            pos = last_idx
            self.arr.append(new_node)
            # self.arr[pos][1] = None

            if len(self.arr) <= 1:
                self.head = new_node
                self.arr[0][1] = None
            else:
                self.arr[pos-1][1] = id(new_node)

        elif pos == 0:
            # self.next = id(self.arr[0])
            self.arr.insert(0, new_node)
            self.head = self.arr[0]
            if len(self.arr) > 1:
                self.arr[0][1] = id(self.arr[1])
        else:
            # self.next = id(self.arr[pos])
            self.arr.insert(pos, new_node)
            if pos > 0:
                self.arr[pos-1][1] = id(self.arr[pos])
            if pos < len(self.arr)-1:
                self.arr[pos][1] = id(self.arr[pos+1])

        return f"Successfully added item at {pos} position"

    def delete(self, pos=-1):
        last_idx = len(self.arr)-1
        if pos == -1 or len(self.arr) == 1 or pos == last_idx:
            self.arr[last_idx-1][1] = None
            self.arr.pop(last_idx)
        elif pos == 0:
            self.head = self.arr[1]
            self.arr.pop(0)
        else:
            if pos > last_idx:
                return f"WARNING : {pos} is greater than length of the array: {last_idx+1}. Delete Operation Failed"

            if pos >= 1:
                self.arr[pos-1][1] = id(self.arr[pos+1][1])
                self.arr.pop(pos)
        return f"Deleted item at {pos} position"

    def update(self, pos, val):
        last_idx = len(self.arr)-1
        if pos > last_idx:
            return f"WARNING : {pos} is greater than length of the array: {last_idx+1}. Update Operation Failed"

        if pos == -1:
            self.arr[-1][0] = val
        elif pos == 0:
            self.arr[0][0] = val
        else:
            self.arr[pos][0] = val

        return f"Updated item at {pos} position"


list1 = LinkedList()

print(list1.insert(1))
print(list1.insert(2))
print(list1.insert(3, 0))
print(list1.insert(4, 1))
print(list1.insert('yash', 2))
print(list1.update(3, 'pulkit'))
print(list1.head)
print(list1.arr)
print(list1.delete())
print(list1.delete(0))
print(list1.delete(1))
print(list1.delete(2))
print(list1.delete(100))
print(list1.arr)
print(list1.update(-1, 'yash'))
print(list1.arr)
