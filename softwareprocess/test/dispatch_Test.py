import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
"""
    def test100_010_missinput(self):
        input = {}
        output = {'error': 'no op is specified'}
        self.assertEqual(SD(input), output)

    def test_dispatch100_110_givenCase1(self):
        input = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        output = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertEqual(SD(input) == output)
"""
    def test_dispatch_invalid_observation(self):
        output = DT.dispatch({'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural',
                              'op': 'adjust', 'temperature': '71'})
        self.assertTrue(output == {'temperature': '71', 'height': '6', 'pressure': '1010', 'horizon': 'natural','error': 'degrees are out of range, should be between 0 and 90', 'observation': '101d15.2', 'op': 'adjust'})
