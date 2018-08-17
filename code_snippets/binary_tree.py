class Node(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

    # insert() is called recursively as we have to locate the place and then insert
    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
    def search(self):
        pass


def inorder_traversal(node):
    if node:
        inorder_traversal(node.right)
        print(node.val)
        inorder_traversal(node.left)


def create_tree():
    root = Node(8)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(7)
    root.insert(14)
    root.insert(13)

    inorder_traversal(root)


def main():
    create_tree()

if __name__ == "__main__":
    main()
