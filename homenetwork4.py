#Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран
# try:
#     line = input("Enter the line: ")
#     dig = 0
#     alp = 0
#     for i in line:
#         if i.isdigit():
#             dig += 1
#         elif i.isalpha():
#             alp += 1
#     print(f"Result number: {dig}")
#     print(f"Result letter: {alp}")
# except Exception as error:
#     print(f"Error: {error}")

#Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається символ
try:
    line = input("Enter the line: ")
    sim = input("Enter search symbol: ")
    qua = 0
    for i in range(len(line)):
        if line[i] == sim:
            qua += 1
    print(f"Result symbol: {qua}")
except Exception as error:
    print(f"Error: {error}")

