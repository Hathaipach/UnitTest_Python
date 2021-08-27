# unit test case
import unittest

# Method assertIsNot()
# UnitTestBy Hathaipach I.

class TestMethods(unittest.TestCase):

    def test_positive(self):
        firstValue = 'apple'
        secondValue = 'grape'
        message = "First value & second value are same object !"
        self.assertIsNot(firstValue, secondValue, message)

if __name__ == '__main__':
    unittest.main()
