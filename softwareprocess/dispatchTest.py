import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test_dispatch100_000_emptyInput(self):
        inputVal = {}
        returnedValue = SD.dispatch(inputVal)
        input = {'error': 'no op  is specified'}
        self.assertTrue(returnedValue == input)

    def test_dispatch100_005_observationValueIllegal(self):
        inputValy = {'op': 'adjust', 'observation': '45d123.4'}
        returnedValue = SD.dispatch(inputValy)
        input == {'error': 'minute is invalid'}
        self.assertTrue(returnedValue == input)

    def test_dispatch1300_003_validvalues(self):
        input = {'op': 'unknown'}
        output = SD.dispatch(input)
        expect = {'error': 'op is not a legal operation'}
        self.assertTrue(output == expect)

    def test_dispatch1200_000_emptyInput(self):
        inputVal = {42}
        returnedValue = SD.dispatch(inputVal)
        input = {'parameter is not a dictionary'}
        self.assertTrue(returnedValue == input)

    def test_dispatch1100_000_emptyInput(self):
        inputVal = None
        returnedValue = SD.dispatch(inputVal)
        input = {'parameter is missing'}
        self.assertTrue(returnedValue == input)

    def test_1211213(self):
        output = SD.dispatch(42)
        self.assertTrue(output == {'error':'parameter is not a dictionary'})

    def test_2(self):
        output = SD.dispatch({})
        self.assertTrue(output == {'error': 'no op  is specified'})
