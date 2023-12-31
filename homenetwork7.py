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
    print(f"Result: {mult}")

except Exception as error:
    print(f"Error: {error}")

#Напишіть функцію для знаходження мінімуму у списку цілих