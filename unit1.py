import unittest
# Method assertEqual
#
class TestNumber(unittest.TestCase):
    def test_add(self):
        self.assertNotEqual(1 + 2, 4)
        self.assertNotEqual(3 + 4, 6)

    def testMultiply(self):
        self.assertNotEqual(2 * 2,6)
        self.assertNotEqual(7 * 7,45)

if __name__ == '__main__':
    unittest.main()