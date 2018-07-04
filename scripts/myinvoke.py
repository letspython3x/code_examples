import pytest

class MyPlugin(object):
    def pytest_sessionfinish(self):
        print "Test Session has ended"

#pytest.main(["-qq"], plugins=[MyPlugin()])

def fib():
    a = 1
    b = 1
    while True:
        yield a
        a,b = b,a+b

for i in fib():
    print i 
    if i >10:
        break

from contextlib import contextmanager

@contextmanager
def tag(name):
    print "%s"% name 
    yield
    print "/%s"%name

with tag('hi'):
    print('foo')

