def addition(num1: int, num2: int):
    return num1 + num2


def subtraction(num1: int, num2: int):
    return num1 - num2


def multiplication(num1: int, num2: int):
    return num1 * num2


def division(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Error: cannot divide by zero!'


