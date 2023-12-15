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
