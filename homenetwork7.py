#1.Напишіть функцію, яка обчислює добуток елементів списку цілих.
import random
NUMS_SIZE = 10
MIN_NUMBER = -20
MAX_NUMBER = 20
numbers = []
for i in range(NUMS_SIZE):
    numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
print(numbers)


def list_multiplication(num: list[int]) -> int:
    result = 1
    for i in range(NUMS_SIZE):
        result *= numbers[i]
    return result


try:
    mult = list_multiplication(numbers)
    print(f"Result multiplication: {mult}")

except Exception as error:
    print(f"Error: {error}")

#Напишіть функцію для знаходження мінімуму у списку цілих


def get_minimum(num: list[int]) -> int:
    return min(num)


try:
    min = get_minimum(numbers)
    print(f"Result minimum: {min}")
except Exception as error:
    print(f"Error: {error}")

#Напишіть функцію, яка визначає кількість простих чисел у списку цілих


def get_prime_number(num: list[int]) -> int:
    prime_numbers = []
    for i in range(NUMS_SIZE):
        if i > 1:
            if i % i == 0:
                break
            else:
                prime_numbers.append(i)
            return prime_numbers[i]
        else:
            break
    # for i in range(NUMS_SIZE):
    #     if numbers[i] < 1:
    #         return False
    #     elif number % i == 0:
    #         prime_numbers.append(numbers)
    #     return prime_numbers


try:
    pn = get_prime_number(numbers)
    print(f"Result: {pn}")
except Exception as error:
    print(f"Error: {error}")