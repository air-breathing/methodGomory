#!usr/bin/python3

import unittest
import task


class Test(unittest.TestCase):
    def setUp(self):
        """
        """
        pass


    def testParse(self):
        value = 'F = 3*x1 + 1*x2 -> max'
        task.parse(value)
        self.assertFalse(False)

    def testParse2(self):
        value = '4*x1 + 3*x2 <= 18'
        task.parse(value)
        self.assertFalse(False)

    def testParse3(self):
        value = '1*x1 + 2*x2 <= 6'
        task.parse(value)
        self.assertFalse(False)

    def testParse4(self):
        value = '0 <= x1'
        task.parse(value)
        self.assertFalse(False)

    def testParse5(self):
        value = 'x1 >= 5'
        task.parse(value)
        self.assertFalse(False)

    def testParse6(self):
        value = '0 <= x2'
        task.parse(value)
        self.assertFalse(False)

    def testParse7(self):
        value = 'x2 <= 4'
        task.parse(value)
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
