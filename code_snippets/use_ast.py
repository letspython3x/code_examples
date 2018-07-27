class Test(object):
    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def file(self):
        with open(self.filepath, "a") as f:
            return f


class Test2(object):
    def __init__(self, filepath):
        self.filepath = filepath

    @staticmethod
    def my_staticmethod0(data):
        pass

    @staticmethod
    def my_staticmethod1(data):
        pass

    @staticmethod
    def my_staticmethod2(data):
        pass

def work_with_file(filepath):
    with open(filepath, "a") as f:
        for line in f:
            Test2.my_staticmethod0(line)
            Test2.my_staticmethod1(line)
            Test2.my_staticmethod2(line)



def main():
    work_with_file(r'./myfile.txt')