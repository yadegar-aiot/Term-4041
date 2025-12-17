def sum(num1, num2):
    return num1 + num2
def taf(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2


try:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("1 : + , 2: - ,3 = * , 4 = /"))
    if num3 ==1:
        print(sum(num1, num2))
    elif num3 == 2:
        print(taf(num1, num2))
    elif num3 == 3:
        print(mul(num1, num2))
    elif num3 == 4:
        print(div(num1, num2))
    else:
        print("Invalid input")

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("تقسیم بر صفر مجاز نیست")
finally:
    print("Goodbye")