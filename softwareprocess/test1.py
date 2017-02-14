import unittest
from convertString2Dictionary import convertString2Dictionary

class MyTestCase(unittest.TestCase):

    def test1001ValidOnePair(self):
        self.dictionary = convertString2Dictionary('abc%3D123')
        self.assertEqual(self.dictionary, {'abc':'123'})

    def test1102Validwithsomesigns(self):
        self.dictionary = convertString2Dictionary('function%20%3D%20get_stars')
        self.assertEqual(self.dictionary, {'function':'get_stars'})

    def test1003ValidtwoPairs(self):
        self.dictionary = convertString2Dictionary('function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse')
        self.assertEqual(self.dictionary, {'function':'calculatePosition', 'sighting':'Betelgeuse'})

    def test1004ValidthreePairs(self):
        self.dictionary = convertString2Dictionary('function%3D%20calculatePosition%2C%20abcd%3D123%2C%20abc%3D123')
        self.assertEqual(self.dictionary,{'function':'calculatePosition', 'abcd':'123', 'abc':'123'})

    def test1005ValidKeywithdigit(self):
        self.dictionary = convertString2Dictionary('key12%3Dvalue')
        self.assertEqual(self.dictionary, {'key12': 'value'})

    def test2001InvalidDuplicateKey(self):
        self.dictionary = convertString2Dictionary('key%3Dvalue%2C%20key%3Dvalue')
        self.assertEqual(self.dictionary, {'error':'true'})

    def test2002InvalidParameter_MissingValue(self):
        self.dictionary = convertString2Dictionary('key%3D')
        self.assertEqual(self.dictionary,{'error':'true'})

    def test2003InvalidKey(self):
        self.dictionary = convertString2Dictionary('value')
        self.assertEqual(self.dictionary, {'error': 'true'})

    def test2004InvalidKey(self):
        self.dictionary = convertString2Dictionary('1key%3Dvalue')
        self.assertEqual(self.dictionary, {'error': 'true'})

    def test2005InvalidKeyFomat(self):
        self.dictionary = convertString2Dictionary('k%20e%20y%20%3D%20value')
        self.assertEqual(self.dictionary, {'error': 'true'})

    def test2006InvalidFomat(self):
        self.dictionary = convertString2Dictionary('')
        self.assertEqual(self.dictionary, {'error':'true'})

    def test2007InvalidKey(self):
        self.dictionary = convertString2Dictionary('key1%3Dvalue%3B%20key%3Dvalue')
        self.assertEqual(self.dictionary, {'error':'true'})

    def test2008InvalidKey(self):
        self.dictionary = convertString2Dictionary('123%3D%20value')
        self.assertEqual(self.dictionary, {'error': 'true'})

if __name__ == '__main__':
    unittest.main()



