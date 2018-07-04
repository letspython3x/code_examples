import pytest

def func(x):
    return x+1

def test_answer():
    """ Test function """
    assert func(4) == 5

def f():
    raise SystemExit(1)

def test_f():
    """ System Exit error is Raised """
    with pytest.raises(SystemExit):
        f()

def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0

class TestClass(object):
    def test_one(self):
        """From test Class """
        x = 'hello'
        assert 'f' in x

    def test_two(self):
        """ from TestClass 2"""
        x = 'hello'
        assert hasattr(x,'check')


def fun():
    # print 'before pass'
    pass
    print 'After pass'

fun()
