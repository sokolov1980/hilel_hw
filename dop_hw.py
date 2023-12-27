#Додаткові завдання по матрицях
#створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99

import random
matrix = []
NUM = 10
for i in range(NUM):
    matrix.append([])
    for j in range(NUM):
        matrix[i].append(random.randint(10, 99))
#вивести на екран
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

#вивести суму чисел головної діагоналі матриці
sum=0
for i in range(NUM):
    for j in range(NUM):
        if i == j:
            sum += matrix[i][j]
print(f"Sum diagonal of the matrix: {sum}")

# вивести мінімальне та максимальне значення побічної діагоналі матриц
diagonal=[]
for i in range(NUM):
    for j in range(NUM):
        if i == NUM - 1 - j:
            diagonal.append(matrix[i][j])
            mini = min(diagonal)
            maxi = max(diagonal)
print(diagonal)
print(f"Min and Max: {mini} {maxi}")

#ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
n1 = int(input("Enter column number: "))
column=[]
for i in range(NUM):
    for j in range(NUM):
        if i == n1:
            column.append(matrix[i][NUM])
            print(column)
n2 = int(input("Enter line number: "))


