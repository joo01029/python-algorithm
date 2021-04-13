class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0

    def setValue(self, n):
        self.value = n

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right
    def getValue(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right


def preorder(ptr):
    if ptr:
        print(ptr.getValue())
        preorder(ptr.getLeft())
        preorder(ptr.getRight())
def inorder(ptr):
    if ptr:
        inorder(ptr.getLeft())
        print(ptr.getValue())
        inorder(ptr.getRight())


def postorder(ptr):
    if ptr:
        postorder(ptr.getLeft())
        postorder(ptr.getRight())
        print(ptr.getValue())

ptr = []
for i in range(16):
    Node = node()
    Node.setValue(i)
    ptr.append(Node)
for i in range(1,16):
    if i %2 == 0:
        ptr[int(i/2)].setLeft(ptr[i])
    else:
        ptr[int(i/2)].setRight(ptr[i])

inorder(ptr[1])
