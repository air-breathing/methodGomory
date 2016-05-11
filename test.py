#!usr/bin/python3

import unittest
import task


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def testParseExpr(self):
        value = ['3*x1', '+', '1*x2']
        actual = task.parseExpr(value)
        expected = {1: 3, 2: 1}
        self.assertDictEqual(actual, expected)

    def testParseExpr2(self):
        value = ['4*x1', '+', '3*x2']
        actual = task.parseExpr(value)
        expected = {1: 4, 2: 3}
        self.assertDictEqual(actual, expected)

    def testParseExpr3(self):
        value = ['-', '1*x1', '+', '2*x2']
        actual = task.parseExpr(value)
        expected = {1: -1, 2: 2}
        self.assertDictEqual(actual, expected)

    def testParseExpr4(self):
        value = ['-', '1*x1', '-', '2*x2']
        actual = task.parseExpr(value)
        expected = {1: -1, 2: -2}
        self.assertDictEqual(actual, expected)

    def testParse4(self):
        value = '0 <= x1'
        task.parse(value)
        self.assertFalse(False)

    def testParse9(self):
        value = 'x2 <= 4'
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
        value = 'x1 + 2*x2 <= 6'
        task.parse(value)
        self.assertFalse(False)

    def testParse8(self):
        value = '- 4*x1 - 2*x2 <= 18'
        task.parse(value)
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
