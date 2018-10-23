class base(object):
    def get(self):
        print("In Base")

    def get_2(self):
        print("In Get 2")
        self.from_child()

    def from_child(self):
        raise RuntimeError("Not Yet Implemented")


class child(base):
    def __init__(self):
        super(child, self).__init__()

    def get(self):
        print("In Child")
        self.get_2()

    def from_child(self):
        print("In From Child")


def main():
    c = child()
    c.get()
    c.get_2()


main()
