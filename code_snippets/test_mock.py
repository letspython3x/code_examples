import mock

class ProdClass(object):
    def closer(self, something):
        with open('./demo.txt', 'rb') as f:
            something.close()

    def method(self):
        self.something(1,2)

    def something(self, a,b):
        pass


# to Check if the close is called with the correct object

"""
real=ProdClass()
mock_something = mock.Mock()
real.closer(mock_something)
mock_something.close.assert_called_with()
"""

def test_ProdClass():
    real = ProdClass()
    real.something = mock.MagicMock()
    real.method()
    real.something.assert_called_with(1,2)

