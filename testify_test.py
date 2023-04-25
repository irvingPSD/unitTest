from testify import *
 
 #python nose_test.py -v
class TestAssertions(TestCase):

    def test_assert_equal(self):
        """
        >>> a = 4
        >>> b = 4
        >>> assert_equal(a, b)
        """
# borra estas funcitnes para que las puedas output <---------
    def test_assert_true(self):
        """
        >>> x = True
        >>> assert_true(x)
        """

#    def test_assert_in(self):
        """
        >>> a = "hello"
        >>> b = ["hello", "world"]
        >>> assert_in(a, b)
        """

    def test_multiline_strings(self):
        """
        >>> a = '''first line
        ... second line
        ... third line'''
        >>> b = '''first line
        ... second line
        ... third line'''
        >>> assert_equal(a, b)
        """
        

    
if __name__ == '__main__':
    run()