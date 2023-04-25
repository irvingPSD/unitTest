
'''On the terminal(Comand line) 
   $ pytest test_pytes.py -v  '''

import pytest

'''pytest allows you to run and test the file without the need to 
    build a class'''
'''def test_assert_equal():            #1
    a = 4
    b = 4
    assert a == b'''      


def test_assert_true():             #4
    x = True
    assert x is True


def test_assert_in():               #2
    a = "Sunshine"
    b = ["Hello", "Sunshine" ]
    assert a in b


#def test_multiline_strings():       #3
#   a = '''first line
#       second line
#        third line'''
        #fourth line'''
#    b = '''first line
#        second line
#        third line'''
#    assert a == b '''

    

#pyTest is simpler and faster. There is no need for 
    if __name__ == '__main__':
       unittest.main() 

  #  Function'''

