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


