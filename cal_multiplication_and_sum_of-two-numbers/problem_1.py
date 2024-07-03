def product(a, b):
    if b * a <= 1000:
        return f"The result is {a*b}"
    else:
        return f"The result is {a+b}"

a = eval(input())
b = eval(input())
print(product(a, b))

# shorthand
'''
["number1 = input()\nnumber2 = input()\nrs = number1 * number2\nif rs > 1000:\n    rs = number1 + number2","rs"]
'''

