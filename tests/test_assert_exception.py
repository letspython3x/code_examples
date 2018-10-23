# Assertions about Expected Exceptions

import pytest

#  to know about the Exception
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0
    assert True


# to get the info about the Exception
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)

# Here the excinfo is a ExceptionInfo instance, a wrapper around
# actual Exception raised

class ftp(object):
    def __init__(self, passwd):
        self.passwd = passwd

class sftp(object):
    pass

def protocol(kwargs):
    if kwargs['protocol'] == 'ftp':
        pro = ftp('passswd')
    else:
        pro = sftp()
    return pro


def test_protocol():
    assert isinstance(protocol({'protocol':'ftp'}), ftp)
    

pytest.main()

