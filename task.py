#!usr/bin/python3

from fractions import Fraction

class Inequality:
    def __init__(self, dict_of_inequality, sign, right_number):
        self.data = dict_of_inequality
        self.sign = sign
        self.right_number = right_number

    def normalize(self):
        pass


def parse(expression):
    components = expression.split(' ')
    # print(components)
    if components[0] == 'F':
        parseMainFunc(components)
    else:
        parseUsual(components)


def parseMainFunc(components):
    maxx = False
    if components[-1] == 'max':
        maxx = True
    elif components[-1] != 'min':
        print('error')
        raise Exception()

    if components[1] == '=' and components[-2] == '->':
        parseExpr(components[2:-2])
    else:
        print('error2')
        raise Exception()


def parseUsual(components):
    if components[0] == '0' and components[1] == '<=' and len(components) == 3:
        return
    if components[-2] == '<=' or components[-2] == '>=' or components[-2] == '=':
        parseExpr(components[:-2])
    else:
        print('error3')
        raise Exception()


def parseExpr(expr):
    vars = {}
    firstMinus = False
    if expr[0] == '-':
        expr = expr[1:]

    koef, variable = getElems(expr[0])
    print(koef, variable)


def getElems(expr):
    koef = 0
    variable = 0
    a = expr.split('*')
    if not(len(a) == 2 or len(a) == 1):
        print('лишнее умножение или не хватает знаков')
        raise Exception()
    elif len(a) == 1:
        variable = 1
        if a[0][0] == 'x':
            koef = int(a[0][1:])
        else:
            print('нет переменной x')
            raise Exception()
    else:
        variable = int(a[0])
        if a[1][0] == 'x':
            koef = int(a[1][1:])
        else:
            print('нет переменной x')
            raise Exception()
    return koef, variable
