def Sum(num1, num2):
    '''  sum of two numbers'''
    return num1 + num2
def tafrigh(num1, num2):
    '''این تابع تفریق میکند'''
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2


print(sum.__doc__)



num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(Sum(num1, num2))
print(tafrigh(num1, num2))
print(mul(num1, num2))
print(div(num1, num2))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)





print(fib(5))

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(9))

print(fib(10))