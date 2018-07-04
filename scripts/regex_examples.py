import re

def is_path(variable):
    pattern = '^/(\w+/)+$'
    groups = re.match(pattern, variable)
    if groups:
        print ('Matched')
        #groups = [group for group in groups]
        print(groups[0])

variable = '/home/abhi/hello13/2323/2e2e/a_b/_/'

is_path(variable)