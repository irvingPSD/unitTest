

''' On the terminal(Comand line)
   $ python unittestFile.py -v  '''

import unittest

''' for unittest, test must be written with a class follow 
    by the function'''

class TestAll(unittest.TestCase):        #1

    def test_assert_equal(self):
        a = 4
        b = 4
        self.assertEqual(a, b)


    def test_assert_true(self):
        x = True
        self.assertTrue(x)


    def test_assert_in(self):
        a = "hello"
        b = ["hello", "world"]
        self.assertIn(a, b)

    def test_string_isupper(self):
        self.assertTrue("UNIT TESTING IN PYHON".isupper())
        self.assertFalse("unit testing in python".isupper())

#    def test_multiline_strings(self):
#        a = '''first line
#        second line
#        third line'''
#        b = '''first line
#        second line
#        third line'''
#        self.assertMultiLineEqual(a, b)

if __name__ == '__main__':
    unittest.main()
