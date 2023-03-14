import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

operator_input = input('Please enter operator: ')
number1 = 4
number2 = 2

print(ops[operator_input](number1,number2))
