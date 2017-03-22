import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test100_010_missinput(self):
        input = {}
        output = {'error': 'no op is specified'}
        self.assertEqual(SD.(input), output)

    def test_dispatch100_110_givenCase1(self):
        inputVal = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        output = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertTrue(returnedValue == inputVal)
