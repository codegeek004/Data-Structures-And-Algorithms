import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

def preorder_iterative(root, result):
    if not root:
        return  
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorder_iterative(root, result):
    if not root:
        return

    stack = []
    node = root
    
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
    return result

def postorder_iterative(root, result):
    if not root:
        return

    stack = []
    visited = set()
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
    return result

def level_order_iterative(root, result):
    if root is None:
        return 

    q = queue.Queue()
    q.put(root)
    node = None

    while not q.empty():
        node = q.get()
        result.append(node.getData())
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight() is not None:
            q.put(node.getRight())
    return result

root = BinaryTreeNode(1)
root.left  = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.left.right = BinaryTreeNode(5)
root.left.left.left = BinaryTreeNode(6)

result = []
#print(preorder_iterative(root, result))
#print(inorder_iterative(root, result))
#print(postorder_iterative(root, result))
print(level_order_iterative(root, result))
