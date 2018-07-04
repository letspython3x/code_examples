def generator():
    try:
        print("Generator started")
        item = yield
        print("Got:", item)
        yield item + 1
        print("Returned: ", item + 1)
        val = yield
        print("Got:", val)
    except GeneratorExit:
        # if uncaught then the generator silently exits
        print("Shutting Down")


def main():
    g = generator()
    next(g)
    g.send(1010)
    g.send(10111)


if __name__ == "__main__":
    main()
