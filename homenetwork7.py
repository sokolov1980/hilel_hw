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
    result = 1
    mult = list_multiplication(numbers)
    print(f"Result multiplication: {mult}")

except Exception as error:
    print(f"Error: {error}")

#2.Напишіть функцію для знаходження мінімуму у списку цілих


def get_minimum(num: list[int]) -> int:
    return min(num)


try:
    min = get_minimum(numbers)
    print(f"Result minimum: {min}")
except Exception as error:
    print(f"Error: {error}")

#3.Напишіть функцію, яка визначає кількість простих чисел у списку цілих



def quantity_prime_number(numbers: list[int]) -> int: #тут считаем кол-во
    qua = 0
    for num in numbers:
        if get_prime_number(num):
            qua += 1
    return qua


def get_prime_number(num) -> int: #тут определяем простое или нет
    if num <= 1: #ограничение - простые считаем от +2 и выше
        return False
    for i in range(2, int(num ** 0.5) + 1): #сокоащаем список - если простое, то можно излечь целый корень
        if num % i == 0:
            return False
    return True

try:
    pn = quantity_prime_number(numbers)
    print(f"Result quantity prime number: {pn}")
except Exception as error:
    print(f"Error: {error}")

#4.Напишіть функцію, яка видаляє зі списку ціле задане число
#
def delete_number(num: list[int]) -> list:
    for i in numbers:
        if i == n1:
            numbers.remove(i)
    return numbers


try:
    n1 = int(input("Enter number to delete: "))
    dn = delete_number(numbers)
    print(f"Result after delete: {dn}")
except Exception as error:
    print(f"Error: {error}")

#5.Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
numbers1 = []
numbers2 = []
for i in range(5):
    numbers1.append(random.randint(-10, 10))
print(numbers1)
for i in range(5):
    numbers2.append(random.randint(-10, 10))
print(numbers2)


def sum_list(num1: list[int], num2: list[int]) -> list:
    summary = numbers1 + numbers2
    return summary


try:
    summary = []
    sl = sum_list(numbers1, numbers2)
    print(f"Result new list: {sl}")
except Exception as error:
    print(f"Error: {error}")

#6.Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Функція повертає новий список, який містить отримані результати


def exponent_list(num: list[int], exp) -> list:
    for i in numbers:
        result.append(i**exp)
    return result


try:
    exp = int(input("Enter exponent: "))
    result = []
    en = exponent_list(numbers, exp)
    print(f"Result exponentiation: {en}")
except Exception as error:
    print(f"Error: {error}")