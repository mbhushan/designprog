import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        def insertIntoBST(node, data):
            if node is None:
                return Node(data)
            if data <= node.data:
                node.left = insertIntoBST(node.left, data)
            else:
                node.right = insertIntoBST(node.right, data)
            return node
        self.root = insertIntoBST(self.root, data)

    def inorder(self):
        def inorderPrint(node):
            if node is None:
                return
            inorderPrint(node.left)
            print str(node.data) + " ",
            inorderPrint(node.right)
        inorderPrint(self.root)

    def levelorderSepline(self):
        def levelorderSepline(node):
            if node is None:
                return
            q = Queue.Queue()
            nline = Node(None)
            q.put(node)
            q.put(nline)
            while not q.empty():
                tmp = q.get()
                if tmp == nline:
                    print "\n"
                    if q.empty():
                        break
                    else:
                        q.put(nline)
                else:
                    print str(tmp.data) + " ",
                    if tmp.left is not None:
                        q.put(tmp.left)
                    if tmp.right is not None:
                        q.put(tmp.right)
        levelorderSepline(self.root)

    def levelorder(self):
        def printLevelOrder(node):
            if node is None:
                return
            q = Queue.Queue()
            q.put(node)
            while not q.empty():
                tmp = q.get()
                if tmp.left is not None:
                    q.put(tmp.left)
                if tmp.right is not None:
                    q.put(tmp.right)
                print str(tmp.data) + " ",
        printLevelOrder(self.root)


def main():
    bt = BinaryTree()
    values = [8, 5, 13, 2, 7, 10, 15]
    for v in values:
        bt.insert(v)
    bt.inorder()
    print "\n"
    print "level order if binary tree: \n"
    bt.levelorder()
    print "\nlevel order separate line: \n"
    bt.levelorderSepline()

if __name__ == '__main__':
    main()
