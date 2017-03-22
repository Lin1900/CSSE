import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test_dispatch100_000_emptyInput(self):
        inputVal = {}
        returnedValue = SD.dispatch(inputVal)
        self.assertTrue(returnedValue == {'error': 'parameter is missing'})

    def test_dispatch100_005_observationValueIllegal(self):
        inputVal = {'op': 'adjust', 'observation': '45d123.4'}
        returnedValue = SD.dispatch(inputVal)
        outputVal['error'] = 'minute is invalid'
        self.assertTrue(returnedValue == outputVal)

