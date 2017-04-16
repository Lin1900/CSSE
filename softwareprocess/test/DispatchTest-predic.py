import unittest

import softwareprocess.dispatch as DP

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 100 dispatch operation
    #   Happy path analysis:
    #        values:      mandatory
    #                     dictionary
    #                     Operations:   {'op':'adjust'}
    #                                   {'op':'predict'}
    #                                   {'op':'correct'}
    #                                   {'op':'locate'}
    #   Sad path analysis:
    #        values:
    #                     no op specified             values={}
    #                        -- return {'error':'no op  is specified'}
    #                     contain 'error' as a key      values={5d04.9', 'height': '6.0', 'pressure': '1010',
    #                                                           'horizon': 'artificial', 'temperature': '72'
    #                                                           'error':'no op is specified'}'
    #                        -- return values without error as a key and without its values
    #                     not-dictionary                values=42
    #                        -- return {'error':'parameter is not a dictionary'}
    #                     not legal operation           values={'op': 'unknown'}
    #                        -- return {'error':'op is not a legal operation'}
    #                     missing dictionary            dispatch()
    #                        -- return {'error':'dictionary is missing'}
    # Happy path
    # def test100_010ShouldReturnUnchangedValuesWithOperationAdjust(self):
    #    values = {'op':'adjust'}
    #    self.assertDictEqual(DP.dispatch(values), values)

    # def test100_010ShouldReturnUnchangedValuesWithOperationPredict(self):
    #     values = {'op': 'predict'}
    #     self.assertDictEqual(DP.dispatch(values), values)

    # def test100_010ShouldReturnUnchangedValuesWithOperationCorrect(self):
    #     values = {'op': 'correct'}
    #     self.assertDictEqual(DP.dispatch(values), values)
    #
    # def test100_020ShouldReturnUnchangedValuesWithOperationLocate(self):
    #     values = {'op': 'locate'}
    #     self.assertDictEqual(DP.dispatch(values), values)

    # Sad path
    # def test100_910_ShouldReturnValuesWithErrorKeyWhenNoOpSpecified(self):
    #     values = {}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test100_920ShouldReturnValuesWithErrorWhenParameterIsNotADictionary(self):
    #     values = 42
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test100_930ShouldReturnValuesWithErrorWhenOpNotALegalOperation(self):
    #     values = {'op': 'unknown'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test100_940ShouldReturnValuesWithErrorWhenDictionaryMissing(self):
    #     self.assertTrue(DP.dispatch().has_key("error"), True)

    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 200 operation {'op': 'adjust'}
    #    Happy path analysis:
    #        observation: mandatory string in the form of xdy.y
    #                     x : is degree portion of the altitude
    #                         positive integer  where 0<=x<90
    #                         low bound x=0
    #                         high bound x=89
    #                     d : character that is used to separate degrees from minutes
    #                     y : minutes
    #                         positive floating point where 0.0<=y<60.0
    #                         low bound  y=0
    #                         high bound y=59.9
    #        height:      optional string
    #                     numerical value(in feet) where height>0
    #                     low bound      height=0
    #                     missing height height=0
    #        temperature: Temperature (in degrees F)
    #                     optional string
    #                     integer where -20<=temperature<=120
    #                     low bound      temperature = -20
    #                     high bound     temperature = 120
    #                     if missing     temperature = 72
    #        pressure:    Barometric pressure(in mbar) at the time observation
    #                     optional string
    #                     integer where 100<=pressure<=1100
    #                     low bound      pressure = 100
    #                     high bound     pressure = 1100
    #                     if missing     pressure = 1010
    #        horizon:     what the observed altitude is relative to
    #                     optional case-insensitive strings
    #                     horizon ="artificial" or horizon="natural
    #                     if missing     horizon = "natural"
    #
    #
    #   Calculation analysis:
    #       dip:
    #                   if the observation is relative to a natural horizon:
    #                       dip = ( -0.97 * sqrt( height ) ) / 60
    #                   else:
    #                       dip = 0
    #       refraction:
    #                   refraction=(-0.00452*pressure) / (273+convert_to_celsius(temperature))/tangent(altitude)
    #       altitude:
    #                   altitude = observation + dip + refraction
    #                   round altitude to the nearest 0.1 arc-minute
    #                   convert altitude to a string having the format xdyy.y where
    #                           x:   degree portion of the altitude
    #                                integer                 -90<x<90
    #                                low bound               x=-89
    #                                high bound              x=89
    #                           d:   character
    #                           y.y: positive floating point    0.0<=y<60.0
    #                                low bound             y=0.0
    #                                high bound            y=59.9
    #                                formatted with two digits to the left of the decimal point
    #                                               one digit to the right
    #
    #    Sad path analysis:
    #        values     : if values = {'op': 'adjust'}:
    #                             return {'error':'mandatory information is missing'}
    #        observation: not in the form of xdy.y        observation="abc"
    #                     missing observation
    #                     x:      non-int x               x="abc"
    #                             out-of-bounds x         x=-1; x=90
    #                             missing x
    #                             -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                     y:      non-floating point y    y="abc"
    #                             out-of-bounds x         y=-1; y=60
    #                             missing y
    #                             -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #        height:      out-of-bounds height            height=-1
    #                     non-int height                  height="a"
    #                     -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #        temperature: non-int temperature             temperature="ab"
    #                     out-of-bounds temperature       temperature=-21; temperature=121
    #                     -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #        pressure:    non-int pressure                pressure="a"
    #                     out-of-bounds pressure          pressure=99; pressure 1101
    #                     -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #        altitude:    already exists in input dict    return values['error'] = diagnostic string
    #

    # sad path
    # def test200_910ShouldReturnErrorIfMandatoryInformationIsMissing(self):
    #     values = {'op': 'adjust'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_920ShouldReturnErrorWhenObservationIsIncorrectFormat(self):
    #     values = {'observation': 'abc', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '71'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_930ShouldReturnErrorWhenDegreeInObservationGreaterThan90(self):
    #     values = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '71'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_940ShouldReturnErrorWhenDegreeInObservationLessThan0(self):
    #         values = {'observation': '-12d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural',
    #                   'op': 'adjust',
    #                   'temperature': '71'}
    #         self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_950ShouldReturnErrorWhenHeightNotNumericalValue(self):
    #     values = {'observation': '89d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '71'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_960ShouldReturnErrorWhenHeightLessThan0(self):
    #     values = {'observation': '89d15.2', 'height': '-1', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '71'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_970ShouldReturnErrorWhenTempNotANumericalValue(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': 'ab'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_980ShouldReturnErrorWhenTempLTMinus20(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '-21'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_990ShouldReturnErrorWhenTempGEMinus120(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '121'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1000ShouldReturnErrorWhenPressureNotANumericalValue(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': 'aa', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '72'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1010ShouldReturnErrorWhenPressureLT100(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '90', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '72'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1020ShouldReturnErrorWhenPressureGT1100(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1120', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '72'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1030ShouldReturnErrorWhenHorizonNotArtificalNorNatural(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'abc', 'op': 'adjust',
    #               'temperature': '72'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1040ShouldReturnErrorWhenHorizonNotString(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': '45', 'op': 'adjust',
    #               'temperature': '72'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test200_1050ShouldReturnErrorWhenAltitudeInInputDictionary(self):
    #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
    #               'temperature': '72', 'altitude':'29d59.9'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #

    # Happy Path
    # def test200_110ShouldCalculateAltitude(self):
    #     values = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
    #     expectedDictionary = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
    #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)
    #
    # def test200_120ShouldCalculateAltitudeWithDefaultValue(self):
    #     values = {'observation': '42d0.0',  'op': 'adjust'}
    #     expectedDictionary = {'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust'}
    #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)
    #
    # def test200_130ShouldCalculateAltitudeWithExtraKey(self):
    #     values = {'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
    #     expectedDictionary = {'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
    #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)

    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 300 operation {'op': 'predict'}
    #    Happy path analysis:
    #    body: name of the celestial body that has been sighted.
    #          mandatory string
    #    date: date of the observation
    #          optional string in yyyy-mm-dd format
    #                               yyyy is GE 2001
    #          if missing "2001-01-01"
    #    time: time of the sighting
    #          optional string in hh:mm:ss format
    #          if missing "00:00:00"
    #
    #     Sad path analysis:
    #       values     : if values = {'op': 'predict'}:
    #                       return {'error':'mandatory information is missing'}
    #       body       : if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if value['body'] not match with the name of the navigable stars
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #       date       : not string
    #                    not in the form of yyyy-mm-dd
    #                    year in date is LE 2001
    #                       --add values['error'] = diagnostic string to the dictionary
    #                                return values
    #       time       : not string
    #                    not in the form of hh:mm:ss
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values

    # Happy Path

    def test300_100ShouldReturnTheCorrectStarLatitudeValue(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        self.assertEqual(DP.dispatch(values)['lat'], '7d24.3')

    def test300_110ShouldPredictTheLocationWithoutDateAndTime(self):
        values = {'op': 'predict', 'body': 'Betelgeuse'}
        data = DP.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1])/60
        self.assertAlmostEquals(result, 11.695, delta=1.695)

    def test300_120ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        data = DP.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 75.8933333333, delta=0.895)

    def test300_130ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        self.assertAlmostEqual(DP.dispatch(values)['lat'],"8d54.8")

    def test300_140ShouldPredictTheLocation(self):
        values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        data = DP.dispatch(values).get('long').split('d')
        result = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(result, 227.023333333, delta=2.023333333)

    # Sad path
    def test300_900ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        values = {'op': 'predict'}
        expectedDictionary = {'error':'mandatory information is missing', 'op': 'predict'}
        self.assertDictEqual(DP.dispatch(values), expectedDictionary)

    def test300_910ShouldReturnIfBodyIsNumeric(self):
        values = {'op': 'predict', 'body': 42}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_920ShouldReturnIfBodyIsInvalid(self):
        values = {'op': 'predict', 'body': 'unknown'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_930ShouldReturnErrorWhenDateHasIncorrectFormat(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_940ShouldReturnErrorIfDateIsNumeric(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_950ShouldReturnErrorWhenYearInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa-09-17', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_960ShouldReturnErrorWhenYearIsLT2001(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2000-09-17', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_970ShouldReturnErrorWhenFebruaryHasLeapDayWhenItIsNotInLeapYear(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-29', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_980ShouldReturnErrorWhenMonthInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2001-aa-17', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_990ShouldReturnErrorWhenMonthInDateIsGT12(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-35-13', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1000ShouldReturnErrorWhenDayInDateIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-aa', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1010ShouldReturnErrorWhenDayInDateIsGT31(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-99', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1020ShouldReturnErrorForMonthsThatDoesNotHave31Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-04-31', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1030ShouldReturnErrorWhenFebruaryHasMoreThan29Days(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-02-30', 'time': '03:15:42'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1040ShouldReturnErrorIfTimeHasIncorrectFormat(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1050ShouldReturnErrorIfTimeIsNumeric(self):
        values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 19}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1060ShouldReturnErrorIfHourInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa:15:34'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1070ShouldReturnErrorIfHourInTimeGT24(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:15:02'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1080ShouldReturnErrorIfMinuteInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:aa:02'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1090ShouldReturnErrorIfMinuteInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:61:02'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1100ShouldReturnErrorIfSecondInTimeIsInvalid(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:aa'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1110ShouldReturnErrorIfSecondInTimeIsGT59(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:99'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1120ShouldReturnErrorIfLatitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'lat':'7d24.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test300_1130ShouldReturnErrorIfLongitudeIsInInputDictionary(self):
        values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'long':'75d53.6'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
