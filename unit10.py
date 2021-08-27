# unit test case
import unittest

# Method assertNotIn(a, b)
# UnitTestBy Hathaipach I.


class TestNumber(unittest.TestCase):

  def testDict(self):
        self.assertNotIn(4, {1: 'a', 2: 'b', 3: 'c'},'Please check your value. Your number is not a member!')

if __name__ == '__main__':
    unittest.main()
