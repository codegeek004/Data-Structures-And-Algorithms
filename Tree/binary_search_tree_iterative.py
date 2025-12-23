class BSTNode:
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

    def find(root, data):
        currentNode = root
        while currentNode:
            if data == currentNode.getData():
                return currentNode
            elif data < currentNode.getData():
                currentNode = currentNode.getLeft()
            else:
                currentNode = currentNode.getRight()
        return currentNode.data

    def find_min(root, data):
        currentNode = root
        if currentNode == None:
            return None

        while currentNode.getLeft() != None:
            currentNode = currentNode.getLeft()
        return currentNode


    def find_max(root, data):
        currentNode = root
        if currentNode == None:
            return None

        while currentNode.getRight() != None:
            currentNode = currentNode.getRight()

        return currentNode

    def insert(root, node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left == None:
                    root.left = node
                else:
                    insert(root.left, node)
            else:
                if root.right == None:
                    root.right = node
                else:
                    insert(root.right, node)


root = BSTNode(0) 
root.insert(1)

def preorder_traversal(root):
    stack = []
    result = []
    if not root:
        return 
    stack.append(root)

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result

print(preorder_traversal(root))


