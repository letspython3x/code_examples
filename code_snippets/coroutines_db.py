def spam():
    try:
        while True:
            line = yield
            print("Got: %s" % line)
    except Exception as e:
        print (e)



def main():
    s = spam()
    s.next()
    s.send('hey')
    s.send('Python')
    s.close()

main()
