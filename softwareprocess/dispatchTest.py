import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test_dispatch100_000_emptyInput(self):
        inputVal = {}
        returnedValue = SD.dispatch(inputVal)
        input = {'error': 'no op  is specified'}
        self.assertTrue(returnedValue == input)

    def test_dispatch100_005_observationValueIllegal(self):
        inputVal = {'op': 'adjust', 'observation': '45d123.4'}
        returnedValue = SD.dispatch(inputVal)
        input == {'error': 'minute is invalid'}
        self.assertTrue(returnedValue == input)

    def test_dispatch100_003_validvalues(self):
        input = {'op': 'unknown'}
        output = SD.dispatch(input)
        input = {'erroe': 'op is not legal operation'}
        self.assertTrue(output == input)
