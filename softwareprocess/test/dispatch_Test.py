import unittest
import softwareprocess.dispatch as SD

class DispatchTest(unittest.TestCase):
    def test100_010_error(self):
        input = {}
        output = {'error': 'no op is specified'}
        self.assertDictEqual(SD.dispatch(input), output)
