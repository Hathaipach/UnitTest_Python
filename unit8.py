# unit test case
import unittest

# Method assertIsNotNone()
# UnitTestBy Hathaipach I.

class NumberClass:
  x = 5

class TestNumber(unittest.TestCase):

    def test_positive(self):
        firstValue = NumberClass()
        # error message in case if test case got failed
        # assertIs() to check that if first & second evaluated to same object
        message = "First value is None!"
        self.assertIsNotNone(firstValue,message)


if __name__ == '__main__':
    unittest.main()
