def get_second_largest(li):
    first, second = li[0], li[0]
    for i in li:
        if i>first:
            first, second = i, first
        
        elif first>i>second:
            second = i

    print first, second

def main():
    li = [2,4,6,7,8,10,23,1]
    get_second_largest(li)

main()
