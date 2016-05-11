#!usr/bin/python3

from fractions import Fraction

class Inequality:
    def __init__(self, dict_of_inequality, right_number=0, sign=None, max_v=None):
        self.data = dict_of_inequality
        self.sign = sign
        self.right_number = right_number
        self.max_v = max_v
        self.max_name_variable = max(dict_of_inequality.keys())

    def normalize(self):
        pass

    def printInequality(self):
        res = ''
        if self.max_v:
            for variable, koef in self.data.items():
                res += str(koef) + '*x' + str(variable) + ' + '
            res = res[:-3]
            res += ' -> '
            if self.max_v:
                res += 'max'
            else:
                res += 'min'
        else:
            for variable, koef in self.data.items():
                res += str(koef) + '*x' + str(variable) + ' + '
            res = res[:-3]
            res += ' ' + str(self.sign) + ' '
            res += str(self.right_number)

        print(res)

class Task:
    def __init__(self, optFunc, inequalities):
        pass



def jardanGaussMethod(matrix, number_str):
    if len(matrix) >= number_str:
        print('номер строки заграницей')
        raise Exception()
    new_matrix = [[] for i in range(matrix[0])]







def parse(expression):
    components = expression.split(' ')
    a = None
    if components[0] == 'F':
        a = parseMainFunc(components)
    else:
        a = parseUsual(components)
    a.printInequality()


def parseMainFunc(components):
    maxx = False
    if components[-1] == 'max':
        maxx = True
    elif components[-1] != 'min':
        print('error')
        raise Exception()

    if components[1] == '=' and components[-2] == '->':
        res = parseExpr(components[2:-2])
        return Inequality(res, 0, max_v=maxx)
    else:
        print('error2')
        raise Exception()


def parseUsual(components):
    if components[0] == '0' and components[1] == '<=' and len(components) == 3:
        return Inequality({int(components[2][1:]): 1}, 0, sign='>=')
    if components[-2] == '<=' or components[-2] == '>=' or components[-2] == '=':
        res = parseExpr(components[:-2])
        return Inequality(res, int(components[-1]), sign=components[-2])
    else:
        print('error3')
        raise Exception()


def parseExpr(expr):
    variables = {}
    firstMinus = False
    if expr[0] == '-':
        expr = expr[1:]
        firstMinus = True

    koef, variable = getElems(expr[0])
    if firstMinus:
        koef *= -1

    variables[variable] = koef
    expr = expr[1:]

    if len(expr) % 2 == 1:
        print('нечетное число коэфициентов')
        raise Exception()

    half = len(expr)//2
    for i in range(half):
        j = i*2
        koef, variable = getElems(expr[j + 1])
        if expr[j] == '-':
            koef *= -1
        variables[variable] = koef
    return variables


def getElems(expr):
    koef = 0
    variable = 0
    a = expr.split('*')
    if not(len(a) == 2 or len(a) == 1):
        print('лишнее умножение или не хватает знаков')
        raise Exception()
    elif len(a) == 1:
        koef = 1
        if a[0][0] == 'x':
            variable = int(a[0][1:])
        else:
            print('нет переменной x')
            raise Exception()
    else:
        koef = int(a[0])
        if a[1][0] == 'x':
            variable = int(a[1][1:])
        else:
            print('нет переменной x')
            raise Exception()
    return koef, variable
