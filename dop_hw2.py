#Написати рекурсивну функцію знаходження ступеня числа.
def exponentiation(num, exponent):
    if exponent <= 1:
        return num
    return num * exponentiation(num, exponent - 1)


try:
    num = int(input("Enter number: "))
    exponent = int(input("Enter positive exponent: "))
    result = exponentiation(num, exponent)
    print(result)
except Exception as error:
    print(f"Error: {error}")

# exponentiation(2, 3) -> 2 * exponentiation(2, 2) => 8
# exponentiation(2, 2) -> 2 * exponentiation(2, 1) => 4
# exponentiation(2, 1) => 2

#Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.



#Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#Користувач вводить a та b. Проілюструйте роботу функції прикладом.




#Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим
# чином і знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.