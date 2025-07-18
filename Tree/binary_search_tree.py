class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.val:
            root.left = self.rinsert(root.left, data)
        elif data >= root.val:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.val == data:
            return root
        else:
            if data < root.val:
                return self.rsearch(root.left, data)
            elif data > root.val:
                return self.rsearch(root.right, data)

    def inorder_search(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.val)
            self.rinorder(root.right, result)

    def preorder_search(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.val)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder_search(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.val)
    
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.val

    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.val:
            root.left = self.rdelete(root.left, data)
        elif data > root.val:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            #replacing with successor
            root.val = self.min_value(root.right)
            root.right = self.rdelete(root.right, root.val)
        return root
    
    def size(self):
        return len(self.inorder_search())


t1 = BST()
t1.insert(40)
t1.insert(20)
t1.insert(30)
t1.insert(40)
t1.insert(50)
t1.insert(60)
t1.insert(45)
t1.insert(70)
t1.delete(50)
t1.delete(40)
print(t1.inorder_search())
