#Користувач вводить три цифри з клавіатури. Необхідно знайти суму чисел, добуток чисел.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
result1 = n1 + n2 + n3
print("sum: ", end=" ")
print(result1)
result2 = n1 * n2 * n3
print("multiplication: ", end=" ")
print(result2)

#Напишіть програму, яка обчислює площу ромба. Користувач із клавіатури вводить довжину двох його діагоналей
d1 = int(input("Enter first diagonal: "))
d2 = int(input("Enter second diagonal: "))
result3 = (d1 * d2) / 2
print("plane of the rhombus: ", end=" ")
print(result3)

#Користувач вводить з клавіатури число, що складається із чотирьох цифр. Потрібно знайти добуток цифр.
number = int(input("Enter 4-digit number: "))
n1 = number // 1000
n2 = number % 1000 // 100
n3 = number % 100 // 10
n4 = number % 10
result = n1 * n2 * n3 * n4
print(f"n1: {n1} n2: {n2} n3 {n3} n4 {n4}")
print("multiplication: ", end=" ")
print(result)