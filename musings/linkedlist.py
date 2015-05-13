import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.N = 0

    def addFront(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.N += 1

    def removeFront(self):
        if self.isEmpty():
            print "List is Empty!"
            return
        node = self.head
        self.head = self.head.next
        self.N -= 1
        return node

    def isEmpty(self):
        return self.N == 0

    def __str__(self):
        sll = []
        node = self.head
        while node is not None:
            sll.append(node.data)
            node = node.next
        print sll


def main():
    operations = "+_+++_+++_"

    rand = random.Random()
    ll = LinkedList()
    for i in operations:
        if i == '+':
            rval = rand.randint(1, 99)
            ll.addFront(rval)
            print "Added: ", rval
        if i == '_':
            tmp = ll.removeFront()
            print "Removed: ", tmp.data
        ll.__str__()


if __name__ == '__main__':
    main()
