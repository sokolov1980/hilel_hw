#Написати рекурсивну функцію знаходження ступеня числа.
def exponentiation(num, exponent):
    if exponent <= 1:
        return num
    return num * exponentiation(num, exponent - 1)


try:
    num = int(input("Enter number: "))
    exponent = int(input("Enter positive exponent: "))
    result = exponentiation(num, exponent)
    print(f"Result exponentiation: {result}")
except Exception as error:
    print(f"Error: {error}")

# exponentiation(2, 3) -> 2 * exponentiation(2, 2) => 8
# exponentiation(2, 2) -> 2 * exponentiation(2, 1) => 4
# exponentiation(2, 1) => 2

#Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.


def star_in_a_row(number):
    if number <= 1:
        return '* '
    return '* ' + star_in_a_row(number - 1)


try:
    number = int(input("Enter positive number: "))
    result = star_in_a_row(number)
    print(result)
except Exception as error:
    print(f"Error: {error}")

# star_in_a_row(3) -> * + star_in_a_row(2) => ***
# star_in_a_row(2) -> * + star_in_a_row(1) => **
# star_in_a_row(1) => *

#Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#Користувач вводить a та b. Проілюструйте роботу функції прикладом.


def calculation_sum(num1, num2):
    if num1 > num2:
        return 0
    return num1 + calculation_sum(num1 + 1, num2)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter first number: "))
    if num1 >= num2:
        print(f"Error")
    else:
        result = calculation_sum(num1, num2)
        print(result)
except Exception as error:
    print(f"Error: {error}")

#Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим
# чином і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.