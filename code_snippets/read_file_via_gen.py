def read_file(filepath):
    filepath = filepath

    for line in open(filepath,'r'):
        yield line


def write_file():
    filepath = './demo.txt'
    for line in read_file(filepath):
        print line


write_file()