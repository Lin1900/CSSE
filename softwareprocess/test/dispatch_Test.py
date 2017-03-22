import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test_100_001(self):
        output = SD.dispatch(42)
        self.assertTrue(output == {'error':'parameter is not a dictionary'})

    def test_100_002(self):
        output = SD.dispatch({})
        self.assertTrue(output == {'error':'no op  is specified'})

    def test_100_003(self):
        output = SD.dispatch({'op': 'un'})
        self.assertTrue(output == {'error':'op is not a legal operation'})

    def test_100_004(self):
        output = SD.dispatch({'op':'adjust', 'observation': '45d73.4'})
        self.assertTrue(output == {'error': 'minute is invalid'})

    def test_100_005(self):
        output = SD.dispatch(None)
        self.assertTrue(output == {'parameter is missing'})

    def test_dispatch100_110_givenCase1(self):
        input = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        output = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertEqual(SD.dispatch(input) == output)
