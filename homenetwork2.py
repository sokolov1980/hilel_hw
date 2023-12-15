#ввод трех чисел максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
#выводим минимум
if n1 <= n2 < n3:
    print("minimum: ", end=" ")
    print(n1)
elif n2 <= n3 < n1:
    print("minimum: ", end=" ")
    print(n2)
elif n3 < n2 <= n1:
    print("minimum: ", end=" ")
    print(n3)
elif n1 <= n3 < n2:
    print("minimum: ", end=" ")
    print(n1)
elif n2 < n1 <= n3:
    print("minimum: ", end=" ")
    print(n2)
elif n3 <= n1 < n2:
    print("minimum: ", end=" ")
    print(n3)
elif n1 < n3 <= n2:
    print("minimum: ", end=" ")
    print(n1)
elif n3 == n2 == n1:
   print("All numbers equals")
#выводим максимум
if n1 >= n2 > n3:
    print("maximum: ", end=" ")
    print(n1)
elif n2 > n3 > n1:
    print("maximum: ", end=" ")
    print(n2)
elif n3 >= n2 > n1:
    print("maximum: ", end=" ")
    print(n3)
elif n1 >= n3 > n2:
    print("maximum: ", end=" ")
    print(n1)
elif n3 > n1 >= n2:
    print("maximum: ", end=" ")
    print(n3)
elif n2 > n1 >= n3:
    print("maximum: ", end=" ")
    print(n2)
elif n1 > n3 >= n2:
    print("maximum: ", end=" ")
    print(n1)
elif n3 == n2 == n1:
   print("All numbers equals")
#выводим среднеарифметическое
result = (n1 + n2 + n3) / 3
print("average: ", end=" ")
print(result)

#Користувач вводить з клавіатури кількість метрів.
number = int(input("Enter number of meters: "))
#выводим мили
result1 = number * 0.000621371
print("mile: ", end=" ")
print(result1)
#выводим дюймы
result2 = number * 39.3701
print("inch: ", end=" ")
print(result2)
#выводим ярды
result3 = number * 1.09361
print("yard: ", end=" ")
print(result3)