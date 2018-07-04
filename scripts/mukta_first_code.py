def declare_var():
     li = [1,2,3,4,5]
     tu = (1,2,3,4)
     di = {'a':1, 'b':2, 'c':3 }

     print(li,tu,di)

declare_var()


def my_fun():
    var=2
    print(type(var))

    var2 = "2+3.0"
    print(var2, type(var2))


my_fun()

def my_loop():
    for i in range(10):
        print(i)

    for i in range(2,20,3):
        print(i)


my_loop()

print "Hello World"
