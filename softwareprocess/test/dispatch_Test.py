import unittest
import softwareprocess.dispatch as SD
import math

class DispatchTest(unittest.TestCase):
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
        output = SD.dispatch({'op': 'adjust'})
        self.assertTrue(output == {'op': 'adjust', 'error': 'mandatory information is missing'})

    def test_100_005(self):
        output = SD.dispatch()
        self.assertTrue(output == {'error': 'parameter is missing'})


    def test_200_001_validvalue(self):
        input = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        inputVal = SD.dispatch(input)
        output = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertTrue(inputVal == output)

    def test_200_002_validvalue(self):
        input = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'altitude':'45d11.9', 'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        self.assertTrue(inputVal == output)

    def test_200_003_validvalue(self):
        input = {'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore'}
        inputVal = SD.dispatch(input)
        output = {'altitude':'41d59.0', 'observation': '42d0.0', 'op': 'adjust', 'extraKey': 'ignore'}
        self.assertTrue(inputVal == output)

    def test_300_001_invalidvalue(self):
        input = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'observation is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_002_invalidvalue(self):
        input = {'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'height is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_003_invalidvalue(self):
        input = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': ' ', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': ' ', 'op': 'adjust', 'temperature': '71', 'error': 'horizon is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_004_invalidvalue(self):
        input = {'observation': '0d0.02', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '0d0.02', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'observation is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_005_invalidvalue(self):
        input = {'observation': '45d15.2', 'height': '6', 'pressure': '74', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '45d15.2', 'height': '6', 'pressure': '74', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'pressure is invalid'}
        self.assertTrue(inputVal == output)
