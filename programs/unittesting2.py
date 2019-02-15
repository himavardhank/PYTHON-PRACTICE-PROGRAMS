import unittest
class TestStringMethods(unittest.TestCase):
        def test_lstrip(self): #testing for left stripping
                 self.assertEqual('   hello '.lstrip(),'hello ')
        def test_isupper(self): #testing for isupper
                 self.assertTrue('HELLO'.isupper())
                 self.assertFalse('HELlO'.isupper())
        def test_split(self): #testing for split
                 self.assertEqual('Hello World'.split(),['Hello','World'])
                 with self.assertRaises(TypeError):
                         s.split(2)
if __name__=='__main__':
        unittest.main()
