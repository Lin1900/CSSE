import unittest
import softwareprocess.dispatch as SD
import math

class DispatchTest(unittest.TestCase):

    def test6_100_001_caculate(self):
        output = SD.dispatch({'op': 'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4', 'assumedLong': ' 74d35.3'})
        self.assertDictEqual(output, {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth': '164d42.9'})

    def test6_200_001_caculate(self):
        output = SD.dispatch({'op': 'correct'})
        self.assertDictEqual(output, {'op':'correct', 'error': 'Mandatory information is missing'})

    def test6_200_002_caculate(self):
        output = SD.dispatch({'op': 'correct', 'lat': '16d32.3', 'long':'95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4', 'assumedLong': ' 74d35.3', 'correctedDistance':'3950'})
        self.assertDictEqual(output, {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'error': 'correctedDistance or correctedAzimuth is invalid'})



"""
   def test_1100_002(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertEqual(output, {'op': 'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42', 'long': '95d41.6', 'lat': '16d32.3'})

    def test_1400_001(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertEqual(output, {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '75d53.6', 'lat': '7d24.3'})

  #  def test_1400_003(self):
  #      output = SD.dispatch({'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'})
  #      self.assertEqual(output, {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42', 'long': '75d53.6', 'lat': '8d54.8'})

    def test300_140ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 227.023333333, delta=2.023333333)

#

    def test300_100ShouldReturnTheCorrectStarLatitudeValue(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        self.assertEqual(SD.dispatch(values)['lat'], '7d24.3')

    def test300_110ShouldPredictTheLocationWithoutDateAndTime(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1])/60
        self.assertAlmostEquals(result, 11.695, delta=1.695)

    def test300_120ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 75.8933333333, delta=0.895)

    def test300_130ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        self.assertAlmostEqual(SD.dispatch(values)['lat'],"8d54.8")

    def test300_140ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 227.023333333, delta=2.023333333)

    # sad path
    def test300_900ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        values = {'op': 'predict'}
        expectedDictionary = {'error':'Mandatory information is missing', 'op': 'predict'}
        self.assertDictEqual(SD.dispatch(values), expectedDictionary)

    def test300_910ShouldReturnIfBodyIsNumeric(self):
        values = {'op': 'predict', 'body': 42}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_920ShouldReturnIfBodyIsInvalid(self):
        values = {'op': 'predict', 'body': 'unknown'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_930ShouldReturnErrorWhenDateHasIncorrectFormat(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_940ShouldReturnErrorIfDateIsNumeric(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_950ShouldReturnErrorWhenYearInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa-09-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_960ShouldReturnErrorWhenYearIsLT2001(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2000-09-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_970ShouldReturnErrorWhenFebruaryHasLeapDayWhenItIsNotInLeapYear(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-29', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_980ShouldReturnErrorWhenMonthInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2001-aa-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_990ShouldReturnErrorWhenMonthInDateIsGT12(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-35-13', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1000ShouldReturnErrorWhenDayInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-aa', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1010ShouldReturnErrorWhenDayInDateIsGT31(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-99', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1020ShouldReturnErrorForMonthsThatDoesNotHave31Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-04-31', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1030ShouldReturnErrorWhenFebruaryHasMoreThan29Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-02-30', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1040ShouldReturnErrorIfTimeHasIncorrectFormat(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1050ShouldReturnErrorIfTimeIsNumeric(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 19}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1060ShouldReturnErrorIfHourInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa:15:34'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1070ShouldReturnErrorIfHourInTimeGT24(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:15:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1080ShouldReturnErrorIfMinuteInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:aa:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1090ShouldReturnErrorIfMinuteInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:61:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1100ShouldReturnErrorIfSecondInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:aa'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1110ShouldReturnErrorIfSecondInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:99'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1120ShouldReturnErrorIfLatitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'lat':'7d24.3'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1130ShouldReturnErrorIfLongitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'long':'75d53.6'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

# my test


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

    def test_400_012(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '200-11-20'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '200-11-20', 'error': 'date is invalid'})

    def test_400_003(self):
        output = SD.dispatch({'op': 'predict'})
        self.assertTrue(output == {'op': 'predict', 'error': 'Mandatory information is missing'})


    def test_400_004(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '21:-22:1'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '21:-22:1', 'error': 'date is invalid'})


    def test_500_0010(self):
        input = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        output = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '75d53.6', 'lat': '7d24.3'}
        self.assertDictEqual(SD.dispatch(input), output)

    def test_500_0020(self):
        input = {'op': 'predict', 'body': 42, 'date': '2016-01-17', 'time': '03:15:42'}
        output = {'op': 'predict', 'body': 42, 'date': '2016-01-17', 'time': '03:15:42', 'error': 'star not in catalog'}
        self.assertDictEqual(SD.dispatch(input), output)

    def test_500_0030(self):
        input = {'op': 'predict', 'body': 'Betelgeuse', 'date': '42', 'time': 42}
        output = {'op': 'predict', 'body': 'Betelgeuse', 'date': '42', 'time': 42, 'error': 'time is invalid'}
        self.assertDictEqual(SD.dispatch(input), output)

    def test_500_0040(self):
        input = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '42'}
        output = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '42', 'error': 'time is invalid'}
        self.assertDictEqual(SD.dispatch(input), output)


    def test_400_0011(self):
        input = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2011-01-17', 'time': '24:09:10'}
        output = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2011-01-17', 'time': '24:09:10', 'error': 'time is invalid'}
        self.assertDictEqual(SD.dispatch(input), output)

    def test_400_0012(self):
        input = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2004-06-31', 'time': '03:15:42'}
        output = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2004-06-31', 'time': '03:15:42', 'error': 'date is invalid'}
        self.assertDictEqual(SD.dispatch(input), output)

    # bad test
    def test300_100ShouldReturnTheCorrectStarLatitudeValue(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        self.assertEqual(SD.dispatch(values)['lat'], '7d24.3')

    def test300_110ShouldPredictTheLocationWithoutDateAndTime(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1])/60
        self.assertAlmostEquals(result, 11.695, delta=1.695)

    def test300_120ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 75.8933333333, delta=0.895)

    def test300_130ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        self.assertAlmostEqual(SD.dispatch(values)['lat'],"8d54.8")

    def test300_140ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        data = SD.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 227.023333333, delta=2.023333333)

    # sad path
    def test300_900ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        values = {'op': 'predict'}
        expectedDictionary = {'error':'mandatory information is missing', 'op': 'predict'}
        self.assertDictEqual(SD.dispatch(values), expectedDictionary)

    def test300_910ShouldReturnIfBodyIsNumeric(self):
        values = {'op': 'predict', 'body': 42}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_920ShouldReturnIfBodyIsInvalid(self):
        values = {'op': 'predict', 'body': 'unknown'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_930ShouldReturnErrorWhenDateHasIncorrectFormat(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_940ShouldReturnErrorIfDateIsNumeric(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_950ShouldReturnErrorWhenYearInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa-09-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_960ShouldReturnErrorWhenYearIsLT2001(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2000-09-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_970ShouldReturnErrorWhenFebruaryHasLeapDayWhenItIsNotInLeapYear(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-29', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_980ShouldReturnErrorWhenMonthInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2001-aa-17', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_990ShouldReturnErrorWhenMonthInDateIsGT12(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-35-13', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1000ShouldReturnErrorWhenDayInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-aa', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1010ShouldReturnErrorWhenDayInDateIsGT31(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-99', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1020ShouldReturnErrorForMonthsThatDoesNotHave31Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-04-31', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1030ShouldReturnErrorWhenFebruaryHasMoreThan29Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-02-30', 'time': '03:15:42'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1040ShouldReturnErrorIfTimeHasIncorrectFormat(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1050ShouldReturnErrorIfTimeIsNumeric(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 19}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1060ShouldReturnErrorIfHourInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa:15:34'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1070ShouldReturnErrorIfHourInTimeGT24(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:15:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1080ShouldReturnErrorIfMinuteInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:aa:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1090ShouldReturnErrorIfMinuteInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:61:02'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1100ShouldReturnErrorIfSecondInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:aa'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1110ShouldReturnErrorIfSecondInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:99'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1120ShouldReturnErrorIfLatitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'lat':'7d24.3'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)

    def test300_1130ShouldReturnErrorIfLongitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'long':'75d53.6'}
        self.assertTrue(SD.dispatch(values).has_key("error"), True)



    def test_400_002(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertDictEqual(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '75d53.6', 'lat': '7d24.3'})


    def test_400_003(self):
        output = SD.dispatch({'op': 'predict'})
        self.assertTrue(output == {'op': 'predict', 'error': 'Mandatory information is missing'})


    def test_400_004(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-17', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-17', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_005(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-31', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-11-31', 'time': '03:15:42', 'error': 'date is invalid'})

    def test_400_006(self):
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-02-28', 'time': '03:15:42'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2014-02-28', 'time': '03:15:42', 'error': 'date is invalid'})

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
        output = SD.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-04-2'})
        self.assertTrue(output == {'op': 'predict', 'body': 'Betelgeuse', 'date': '2003-04-2', 'error': 'date is invalid'})
"""
