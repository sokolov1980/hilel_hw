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

# #вивести суму чисел головної діагоналі матриці
# sum = 0
# for i in range(NUM):
#     for j in range(NUM):
#         if i == j:
#             sum += matrix[i][j]
# print(f"Sum diagonal of the matrix: {sum}")
#
# # вивести мінімальне та максимальне значення побічної діагоналі матриц
# diagonal = []
# for i in range(NUM):
#     for j in range(NUM):
#         if i == NUM - 1 - j:
#             diagonal.append(matrix[i][j])
#             mini = min(diagonal)
#             maxi = max(diagonal)
# print(diagonal)
# print(f"Min and Max: {mini} {maxi}")
#
# #ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
# n1 = int(input("Enter line number: "))
# column = []
# line = []
# if n1 > NUM or n1 <= 0:
#     print("Invalid number")
# else:
#     for i in range(NUM):
#         print(matrix[n1-1][i], end=" ")
# n2 = int(input("\nEnter column number: "))
# if n2 > NUM or n2 <= 0:
#     print("Invalid number")
# else:
#     for i in range(NUM):
#         print(matrix[i][n2-1], end=" ")
#
# #ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# #строки
nl1 = int(input("\nEnter first line number: "))
nl2 = int(input("Enter second line number: "))
if nl1 > NUM or nl1 <= 0 or nl2 > NUM or nl2 <= 0 or nl1 >= nl2:
    print("Invalid number or identical rows selected")
# #v1
# else:
#     line1 = matrix[nl1 - 1]
#     line2 = matrix[nl2 - 1]
#     matrix.pop(nl2 - 1)
#     matrix.pop(nl1 - 1)
#     matrix.insert(nl1 - 1, line2)
#     matrix.insert(nl2 - 1, line1)
#     for i in range(NUM):
#         for j in range(NUM):
#             print(matrix[i][j], end=" ")
#         print()
#v2
else:
    for j in range(NUM):
        matrix[nl1 - 1][j], matrix[nl2 - 1][j] = matrix[nl2 - 1][j], matrix[nl1 - 1][j]
    for q in range(NUM):
        for p in range(NUM):
            print(matrix[q][p], end=" ")
        print()

#стовбці
nc1 = int(input("\nEnter first column number: "))
nc2 = int(input("Enter second column number: "))
if nc1 > NUM or nc1 <= 0 or nc2 > NUM or nc2 <= 0 or nc1 == nc2:
    print("Invalid number or identical column selected")
else:
    for i in range(NUM):
        matrix[i][nc1 - 1], matrix[i][nc2 - 1] = matrix[i][nc2 - 1], matrix[i][nc1 - 1]
    for q in range(NUM):
        for p in range(NUM):
            print(matrix[q][p], end=" ")
        print()




