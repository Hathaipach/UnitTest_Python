import unittest
# Method assertN=Equal
# UnitTestBy Hathaipach I.
class TestNumber(unittest.TestCase):

    def testMultiply(self):
        self.assertNotEqual(2 * 2,6)
        self.assertNotEqual(7 * 7,45)

if __name__ == '__main__':
    unittest.main()