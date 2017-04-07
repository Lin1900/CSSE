import unittest
import softwareprocess.dispatch as SD
import math

class predictTest(unittest.TestCase):
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
        self.assertTrue(output == {'op': 'predict', 'error': 'Mandatory information is missing'})

    def test_100_005(self):
        output = SD.dispatch()
        self.assertTrue(output == {'error': 'parameter is missing'})

    def test_100_006(self):
        output = SD.dispatch({'op': 'predict','body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42', 'error': 'star not in catalog'})
