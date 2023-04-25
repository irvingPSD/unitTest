import unittest
import doctest

def test_assert_equal():            
    """
    >>> a = 4
    >>> b = 4
    >>> assert a == b
    """

def test_assert_true():             

    """
    >>> x = True
    >>> assert x == True
    """

#def test_assert_in():               
    """
    >>> a = "hello"
    >>> b = ["hello", "world"]
    >>> assert a in b
    """

#def test_multiline_strings():       
    """
    >>> a = '''first line
    ... second line
    ... third line'''
    >>> b = '''first line
    ... second line
    ... third line'''
    >>> assert a == b
    """
def test_square_of():
    '''
    >>>  a = 4
         b = a*a
    >>> assert a == b
    
    '''



if __name__ == '__main__':
    doctest.testmod(verbose=True)
    unittest.main()
