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
# try:
#     line = input("Enter the line: ")
#     sim = input("Enter search symbol: ")
#     qua = 0
#     for i in range(len(line)):
#         if line[i] == sim:
#             qua += 1
#     print(f"Result symbol: {qua}")
# except Exception as error:
#     print(f"Error: {error}")

#Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну
# try:
#     text = input("Enter the text: ")
#     word = input("Enter word to search: ")
#     word_r = input("Enter word to replace: ")
#     text = text.replace(word, word_r )
#     print(f"Modified text: {text}")
# except Exception as error:
#     print(f"Error: {error}")

#Дано рядок. (зробити зрізи)
try:
    text = input("Enter the text: ")
#виведіть третій символ
    print(text[2:3])
#виведіть передостанній символ
    print(text[-2:-1])
#виведіть перші п'ять символів
    print(text[0:5])
#виведіть весь рядок, крім двох останніх символів
    print(text[0:-2])
#У п'ятому рядку виведіть усі символи з парними індексами
    print(text[1::2])
# У шостому рядку виведіть усі символи з непарними індексами
    print(text[0::2])
#У сьомому рядку виведіть усі символи у зворотному порядку.
    print(text[::-1])
#У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього
    print(text[::-2])
#У дев'ятому рядку виведіть довжину цього рядка
    print(len(text))
except Exception as error:
    print(f"Error: {error}")

#Додатково
# try:
#     text = input("Enter the line: ")
#     dig = 0
#     alp = 0
#     for i in text:
#         if i.isdigit():
#             dig += 1
#         elif i.isalpha():
#             alp += 1
#     print(f"Result number: {dig}")
#     print(f"Result letter: {alp}")
# except Exception as error:
#     print(f"Error: {error}")