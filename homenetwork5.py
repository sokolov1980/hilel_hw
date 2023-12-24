#У списку цілих, заповненому випадковими числами обчислити:
try:
    import random
    NUMS_SIZE = 10
    MIN_NUMBER = -20
    MAX_NUMBER = 20
    numbers = []
    number = []

    for i in range(NUMS_SIZE):
        numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
    print(numbers)

#Суму негативних чисел
    for i in range(NUMS_SIZE):
        if (numbers[i] < 0):
            number.append(numbers[i])
            result = sum(number)
    print(f"List a negative number: {number}")
    print(f"Sum a negative number: {result}")



#Суму парних чисел


#Суму непарних чисел

#Добуток елементів з кратними індексами 3

#Добуток елементів між мінімальним та максимальним елементом;

#Суму елементів, що знаходяться між першим та останнім позитивними елементами.

except Exception as error:
    print(f"Error: {error}")