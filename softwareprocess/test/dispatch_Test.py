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

    def test_100_006(self):
        output = SD.dispatch({'op': 'adjust','observation': '30d90.5'})
        self.assertTrue(output == {'op': 'adjust', 'observation': '30d90.5', 'error': 'observation is invalid'})

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

    def test_300_006_invalidvalue(self):
        input = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'abc', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'abc', 'op': 'adjust', 'temperature': '71', 'error': 'horizon is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_007_invalidvalue(self):
        input = {'observation': '45d15.2', 'height': 'a6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '45d15.2', 'height': 'a6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'height is invalid'}
        self.assertTrue(inputVal == output)

#    def test_700_001_validvalue(self):
#        input = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
#        inputVal = SD.dispatch(input)
#        output = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85', 'error': 'height is invalid'}
#        self.assertTrue(inputVal == output)

    def test_300_0011_invalidvalue(self):
        input = {'observation': '10d15.2', 'height': '6', 'pressure': '110aa', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        inputVal = SD.dispatch(input)
        output = {'observation': '10d15.2', 'height': '6', 'pressure': '110aa', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error': 'pressure is invalid'}
        self.assertTrue(inputVal == output)

    def test_300_0021_invalidvalue(self):
        input = {'observation': '10d15.2', 'height': '6', 'pressure': '1100', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71a'}
        inputVal = SD.dispatch(input)
        output = {'observation': '10d15.2', 'height': '6', 'pressure': '1100', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71a', 'error': 'temperature is invalid'}
        self.assertDictEqual(inputVal, output)

    def test_400_001(self):
        output = SD.dispatch({'op': 'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42', 'error': 'star not in catalog'})
"""
    def test_400_002(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '75d53.6', 'lat': '7d24.3'})

    def test_400_003(self):
        output = SD.dispatch({'op': 'predict'})
        self.assertTrue(output == {'op': 'predict', 'error': 'Mandatory information is missing'})


    def test_400_004(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-13-17', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-13-17', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_005(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-31', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-31', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_006(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-02-29', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-02-29', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_007(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2012-02-30', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2012-02-30', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_008(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-b4-20', 'time': '01:03:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-b4-20', 'time': '01:03:42', 'error': 'date is invalid'})

    def test_400_009(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '206-11-30', 'time': '03:61:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '206-11-30', 'time': '03:61:42', 'error': 'date is invalid'})

    def test_400_010(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-2-21', 'time': '03:15:50'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-2-21', 'time': '03:15:50', 'error': 'date is invalid'})

    def test_400_011(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-2-21', 'time': '13:07:30'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-2-21', 'time': '13:07:30', 'error': 'date is invalid'})

    def test_400_012(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-04-2', 'time': '03:11:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-04-2', 'time': '03:11:42', 'error': 'date is invalid'})
"""
