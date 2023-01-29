from functools import reduce


def operate(*stuf):
    operations = {'+': lambda x,y: x+y,
                  '-': lambda x,y: x-y,
                  '*': lambda x,y: x*y,
                  '/': lambda x,y: x/y,
                  }
    operator = stuf[0]
    nums = stuf[1:]
    result = reduce(operations[operator], nums)

    return result

print(operate("*", 3, 4))