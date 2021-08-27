import unittest

# Method assertIs()
# UnitTestBy Hathaipach I.

class NumberClass:
  x = 5

class TestNumber(unittest.TestCase):

    def test_positive(self):
        firstValue = NumberClass()
        secondValue = firstValue
        # error message in case if test case got failed
        # assertIs() to check that if first & second evaluated to same object
        message = "First value & second value are not same object !"
        self.assertIs(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()