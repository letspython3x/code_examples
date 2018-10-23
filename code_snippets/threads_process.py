from concurrent.futures import Future, ThreadPoolExecutor
from time import sleep
from datetime import datetime


def func(x, y, delay):
    print (datetime.now())
    sleep(delay)
    return x + y


def func2():
    sleep(1)
    return("Hey func2")


def threads():
    pool = ThreadPoolExecutor(4)
    fut1 = pool.submit(func, 10, 10,1)
    fut2 = pool.submit(func, 11, 11,4)
    fut3 = pool.submit(func, 12, 12,1)
    fut4 = pool.submit(func, 13, 13,8)
    print("Got: ", fut1.result())
    print("Got: ", fut2.result())
    print("Got: ", fut3.result())
    print("Got: ", fut4.result())
    fut5 = pool.submit(func2)
    print("Got: ", fut5 .result())

def main():
    threads()


main()
