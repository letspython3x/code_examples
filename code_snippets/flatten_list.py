from functools import reduce


def flatten(lst):
    f_list= list()
    if len(lst) == 0:
        return None
    else:
        for item in lst:
            if isinstance(item, list):
                f_list.extend(item)
            elif isinstance(item, int):
                lst.append(item)
    print(f_list)

print('Hello')

def flatten_2(lst):
    for i, element in enumerate(lst):
        if not isinstance(element, list):
            lst[i] = list(element)

    return reduce(lambda x,y: x+y, lst)

#print (flatten_2([[1, 2, 3], 10, [4, 5, 6], [7], [8, 9]]))
flatten([1, [2, 3, [4]], 5, [[6]]]) # => [1, 2, 3, 4, 5, 6])