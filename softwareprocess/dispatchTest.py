import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test_dispatch100_000_emptyInput(self):
        inputVal = {}
        returnedValue = SD.dispatch(inputVal)
        inputVal = {'error': 'no op  is specified'}
        self.assertTrue(returnedValue == inputVal)

    def test_dispatch100_005_observationValueIllegal(self):
        inputVal = {'op': 'adjust', 'observation': '45d123.4'}
        returnedValue = SD.dispatch(inputVal)
        inputVal == {'error': 'minute is invalid'}
        self.assertTrue(returnedValue == inputVal)

    def test_dispatch100_003_validvalues(self):
        input = {'op': 'unknown'}
        output = SD.dispatch(input)
        expect = {'erroe': 'op is not legal operation'}
        self.assertTrue(output == expect)
