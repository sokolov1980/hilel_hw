#Написати рекурсивну функцію знаходження ступеня числа.
def exponentiation(num, exponent):
    if exponent == 1:
        return num
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / (num * exponentiation(num, - exponent - 1))
    return num * exponentiation(num, exponent - 1)



try:
    num = int(input("Enter number: "))
    exponent = int(input("Enter exponent: "))
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
        print(f"Error: enter the smaller range limit first or the values are equal")
    else:
        result = calculation_sum(num1, num2)
        print(f"Result sum: {result}")
except Exception as error:
    print(f"Error: {error}")

# calculation_sum(3, 3) -> 3 + calculation_sum(2, 3) => 6
# calculation_sum(2, 3) -> 2 + calculation_sum(1, 3) => 3
# calculation_sum(1, 3) => 1

#Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим
# чином і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.
import random
NUMS_SIZE = 100
MIN_NUMBER = 0
MAX_NUMBER = 10
numbers = []
for i in range(NUMS_SIZE):
    numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
print(numbers)


def find_min_sum_index(numbers, start_index, end_index, min_sum=999, min_index=0):
    if end_index < len(numbers):
        current_sum = sum(numbers[start_index:end_index + 1])

        if current_sum < min_sum:
            min_sum = current_sum
            min_index = start_index

        start_index += 1
        end_index += 1

        print(f"Min sum: {min_sum} Current sum: {current_sum} Index: {min_index}")

        return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)

    return min_index


result = find_min_sum_index(numbers, 0, 9)
print(f"Min sum index: {result}")