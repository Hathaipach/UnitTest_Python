# unit test case
import unittest

# Method assertIn(a, b)
# UnitTestBy Hathaipach I.


class TestNumber(unittest.TestCase):

  def testDict(self):
        self.assertIn(4, {1: 'a', 2: 'b', 3: 'c', 4: 'd'},'Please check your value.')

if __name__ == '__main__':
    unittest.main()
