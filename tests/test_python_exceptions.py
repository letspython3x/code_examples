import pytest


def func(x):
    return x + 1


def test_answer():
    """ Test function """
    assert func(4) == 5


def f():
    raise SystemExit(1)


def test_f():
    """ System Exit error is Raised """
    with pytest.raises(SystemExit):
        f()


def test_raises_recursion_error():
    def myFun():
        myFun()

    with pytest.raises(RecursionError):
        myFun()


def test_needsfiles(tmpdir):
    print(tmpdir)
    assert True


class TestClass(object):
    def test_one(self):
        """From test Class """
        x = 'hello'
        r = 'f' in x
        assert r is False

    def test_two(self):
        """ from TestClass 2"""
        x = 'hello'
        assert False == hasattr(x, 'check')
