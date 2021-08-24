
import unittest

# Method assertFalse()
# UnitTestBy Hathaipach I.

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('APPLE' .lower(), 'apple')

    def test_islower(self):
        self.assertFalse('APPLE'.islower())


if __name__ == '__main__':
    unittest.main()