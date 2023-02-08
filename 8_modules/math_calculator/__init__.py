# makes basic math operations "* / + - ^"

def m_operation(n1=float, op=str, n2=int ):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y,
    }

    result = operations[op](n1, n2)
    return result
