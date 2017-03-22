from unittest import TestCase
import urllib

import softwareprocess.convertString2Dictionary as cs2d

class convertString2DictionaryTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.errorDict = {'error':'true'}

# ---
# Acceptance test analysis
#   input:  inputString -> percent-encoded UTF-8, optional,
#           contains key-value pairs,    (key = value)*
#                   key is ([a..z]|[A..A])([a..z]|[A..Z]|[0..9]|[.])*
#                   value is ([a..z]|[A..Z]|[0..9]|[.])+
#   output: dictionary -> {'key':'value', (,'key': 'value')*}
#                   invalid input:  {'error':'true'}
#
#   happy path analysis
#       inputString =   010 nominal percent-encoded UTF-8 string with one key-value pair
#                           given:  quote("key=value")
#                           expected:  {'key':'value'}
#                       020 nominal percent-encoded UTF-8 string with one key-value pair
#                           given:  quote("key1=value,key2=value")
#                           expected:  {'key1':'value','key2':'value'}
#                       030 nominal percent-encoded UTF-8 string with .GT. two key-value pairs
#                           given:  quote("key1=value,key2=value,key3=value")
#                           expected:  {'key1':'value','key2':'value'}
#                       040 nominal percent-encoded UTF-8 string with blanks
#                           given:  quote(" key1 = value , key2 = value ")
#                           expected:  {'key1':'value','key2':'value'}
#
#   sad path analysis
#       inputString:    900 missing string
#                       905 blanks
#                       910 percent-encoded UTF-8 string with multiple key-value pairs, not comma
#                       915 percent-encoded UTF-8 string with duplicate key
#                       920 percent-encoded UTF-8 string with an invalid key (invalid = key no alpha)
#                       925 percent-encoded UTF-8 string with an invalid key (invalid = key missing)
#                       930 percent-encoded UTF-8 string with an invalid key (invalid = key with blank)
#                       935 percent-encoded UTF-8 string with an invalid key (invalid = key with invalid char)
#                       940 percent-encoded UTF-8 string with invalid value (invalid = value missing)
#                       945 percent-encoded UTF-8 string with invalid value (invalid = value with blank)
#                       950 percent-encoded UTF-8 string with invalid value (invalid = value with invalid char)
#                       955 percent-encoded UTF-8 string with missing key and missing value
#                       960 percent-encoded UTF-8 string with comma separator alone
#                       965 percent-encoded UTF-8 string with valid and invalid

# Happy path tests
    def test_100_010_ShouldConvertNominalStringWithOneKeyValuePair(self):
        encodedString = urllib.quote("key=value")
        expectedResult = {'key':'value'}
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
                             "Major defect:  not able to parse one key-value pair")

    def test_100_020_ShouldConvertNominalStringWithOneKeyValuePairs(self):
        encodedString = urllib.quote("key1=value,key2=value")
        expectedResult = {'key1':'value','key2':'value'}
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
                             "Major defect:  not able to parse comma separated pairs")

    def test_100_030_ShouldConvertNominalStringWithMultipleKeyValuePairs(self):
        encodedString = urllib.quote("key1=value,key2=value,key3=value")
        expectedResult = {'key1':'value','key2':'value','key3':'value'}
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
                             "Major defect:  not able to parse multiple comma spearated pairs")

    def test_100_030_ShouldConvertNominalStringWithBlanks(self):
        encodedString = urllib.quote(" key1 = value , key2 = value ")
        expectedResult = {'key1':'value','key2':'value'}
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
                             "Major defect:  not able to parse appropriate white space")

# Sad path tests
    def test_100_900_ShouldReturnErrorNoInput(self):
        self.assertDictEqual(cs2d.convertString2Dictionary(), self.errorDict,
                             "Major defect:  does not return proper result on missing parm")

    def test_100_905_ShouldReturnErrorNullString(self):
        self.assertDictEqual(cs2d.convertString2Dictionary(" "), self.errorDict,
                             "Minor defect:  does not return proper result on blank parm")

    def test_100_910_ShouldReturnErrorOnMissingComma(self):
        encodedString = urllib.quote("key1=value1 key2=value2")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on missing comma")

    def test_100_915_ShouldReturnErrorOnDuplicateKey(self):
        encodedString = urllib.quote("key=value,key=value")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on duplicate key")

    def test_100_920_ShouldReturnErrorOnBadKeyName(self):
        encodedString = urllib.quote("1key=value")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on invalid key")

    def test_100_925_ShouldReturnErrorOnMissingKey(self):
        encodedString = urllib.quote("=value")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on missing key")

    def test_100_930_ShouldReturnErrorOnMissingKeyWithBlank(self):
        encodedString = urllib.quote("ke y=value")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on key with embedded blanks")

    def test_100_935_ShouldReturnErrorOnKeyWithInvalidChar(self):
        encodedString = urllib.quote("my_key=value")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on key with invalid characters")

    def test_100_940_ShouldReturnErrorOnMissingValue(self):
        encodedString = urllib.quote("key=")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on missing value")

    def test_100_945_ShouldReturnErrorOnValueWithBlank(self):
        encodedString = urllib.quote("key=va lue")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on value with embedded blanks")

    def test_100_950_ShouldReturnErrorOnValueWithInvalidChar(self):
        encodedString = urllib.quote("key=va_lue")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on value with invalid characters")

    def test_100_955_ShouldReturnErrorOnMissingKeyMissingValue(self):
        encodedString = urllib.quote("=")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on missing key and missing value")

    def test_100_960_ShouldReturnErrorOnLoneComma(self):
        encodedString = urllib.quote(",")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on empty separator")

    def test_100_960_ShouldReturnErrorOnValidInvalidKeyValuePair(self):
        encodedString = urllib.quote("key1=value,key2=")
        self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
                             "Major defect:  does not return proper result on mix of valid and invalid items")
