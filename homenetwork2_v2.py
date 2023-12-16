#ввод трех чисел максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
#выводим минимум
if n1 <= n2 and n1 < n3:
    print(f"minimum: {n1}")
elif n2 <= n1 and n2 < n3 or n2 < n1 and n2 <= n3:
    print(f"minimum: {n2}")
elif n3 <= n1 and n3 < n2:
    print(f"minimum: {n3}")
else:
   print("All numbers equals")
# #выводим максимум
if n1 >= n2 and n1 > n3:
    print(f"maximum: {n1}")
elif n2 >= n1 and n2 > n3 or n2 > n1 and n2 >= n3:
    print(f"maximum: {n2}")
elif n3 >= n1 and n3 > n2:
    print(f"maximum: {n3}")
else:
   print("All numbers equals")
# #выводим среднеарифметическое
result = (n1 + n2 + n3) / 3
print(f"average: {result}")
#
# #Користувач вводить з клавіатури кількість метрів.
# number = int(input("Enter number of meters: "))
# #выводим мили
# result1 = number * 0.000621371
# print("mile: ", end=" ")
# print(result1)
# #выводим дюймы
# result2 = number * 39.3701
# print("inch: ", end=" ")
# print(result2)
# #выводим ярды
# result3 = number * 1.09361
# print("yard: ", end=" ")
# print(result3)