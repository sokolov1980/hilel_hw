#1.У списку цілих, заповненому випадковими числами обчислити:
try:
    import random
    NUMS_SIZE = 10
    MIN_NUMBER = -20
    MAX_NUMBER = 20
    numbers = []
    number = []
    number2 = []
    number3 = []
    for i in range(NUMS_SIZE):
        numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
    print(numbers)

#Суму негативних чисел
    for i in range(NUMS_SIZE):
        if numbers[i] < 0:
            number.append(numbers[i])
            result = sum(number)
    print(f"List a negative number: {number}")
    print(f"Sum a negative number: {result}")

#Суму парних чисел
    for i in range(NUMS_SIZE):
        if numbers[i] % 2 == 0:
            number2.append(numbers[i])
            result = sum(number2)
        else: #Суму непарних чисел
            number3.append(numbers[i])
            result2 = sum(number3)
    print(f"List a even number: {number2}")
    print(f"Sum a even number: {result}")
    print(f"List a odd number: {number3}")
    print(f"Sum a odd number: {result2}")

#Добуток елементів з кратними індексами 3
#v1
    result = 1
    for i in numbers[3::3]:
        result *= i
    print(f"Index multiple 3 number: {numbers[3::3]}")
    print(f"Multiplication a index multiple 3 number: {result}")
#v2
    result = 1
    for i in range(1, len(numbers)):
        if i % 3 == 0:
            result *= numbers[i]
    print(f"Multiplication a index multiple 3 number v2: {result}")
#Добуток елементів між мінімальним та максимальним елементом;
    result = 1
    number4 = []
    j = numbers.index(min(numbers))
    k = numbers.index(max(numbers))
    for i in range(NUMS_SIZE):
        if j < k:
            number4 = numbers[j:k+1]
        else:
            number4 = numbers[k:j+1]
    for i in range(len(number4)):
        result *= number4[i]
    print(f"List interval min max: {number4}")
    print(f"Multiplying numbers on the interval min max : {result}")

#Суму елементів, що знаходяться між першим та останнім позитивними елементами.
    result = 0
    for i in range(NUMS_SIZE):
        try:
            if numbers[i] > 0:
                num1 = i
                break
        except Exception as error:
            print(f"no positive numbers: {error}")
    for i in range(NUMS_SIZE - 1, -1, -1):
        if numbers[i] > 0:
            num2 = i
            break
    for i in range(num1+1,num2):
        result += numbers[i]
    print(f"Index the first and last number : {num1}, {num2}")
    print(f"sum of numbers in the interval : {result}")

except Exception as error:
    print(f"Error: {error}")

#2Є список цілих, заповнений випадковими числами. На підставі даних цього масиву потрібно
