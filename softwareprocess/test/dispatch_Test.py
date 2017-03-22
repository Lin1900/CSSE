import unittest
import softwareprocess.lambda.dispatch as SD

class DispatchTest(unittest.TestCase):

#    def test100_010_missinput(self):
 #       input = {}
  #      output = {'error': 'no op is specified'}
   #     self.assertEqual(SD.dispatch(input), output)

    def test_dispatch100_110_givenCase1(self):
        input = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        output = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertEqual(SD.adjust(input) == output)
