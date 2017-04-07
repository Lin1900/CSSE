import unittest
import softwareprocess.dispatch as SD
import math

class redictTest(unittest.TestCase):
    def test_100_001(self):
        output = SD.dispatch(42)
        self.assertTrue(output == {'error': 'parameter is not a dictionary'})

    def test_100_002(self):
        output = SD.dispatch({})
        self.assertTrue(output == {'error': 'no op is specified'})

    def test_100_003(self):
        output = SD.dispatch({'op': 'unknown'})
        self.assertTrue(output == {'op': 'unknown', 'error': 'op is not a legal operation'})

    def test_100_004(self):
        output = SD.dispatch({'op': 'predict'})
        self.assertTrue(output == {'op': 'adjust', 'error': 'mandatory is missing'})

    def test_100_005(self):
        output = SD.dispatch()
        self.assertTrue(output == {'error': 'parameter is missing'})

    def test_100_006(self):
        output = SD.dispatch({'op': 'predict','observation': '30d90.5'})
        self.assertTrue(output == {'op': 'adjust', 'observation': '30d90.5', 'error': 'observation is invalid'})
