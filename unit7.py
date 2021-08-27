# unit test case
import unittest

# Method assertIsNone()
# UnitTestBy Hathaipach I.

class TestNumber(unittest.TestCase):

    def test_positive(self):
        firstValue = None
        # error message in case if test case got failed
        # assertIs() to check that if first & second evaluated to same object
        message = "First value is not None!"
        self.assertIsNone(firstValue,message)


if __name__ == '__main__':
    unittest.main()
