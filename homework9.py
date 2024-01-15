# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що
# складаються не менше ніж з семи літер.
import re

with open("text10.txt", "r") as source, open("text7dit.txt", "w") as destination:
    text = source.read()
    words = re.sub(r"[,?!.]", " ", text)  #заменяем точки, зпт и тд на пробел
    for word in words.split():
        text7 = word.join(re.findall(r'(^[A-Za-z]{7,}$)', word))
        if text7:
            destination.write(text7 + " ")


# 2.Даний текстовий файл. Підрахувати кількість слів у ньому.
with open("text10.txt", "r") as source:
    # v 1
    # word_count = 0
    # for word in words.split():
    #     word_count += len(re.findall(r'^([A-Za-z]+[.,!?]?){1,}$', word))
    # v 2
    text = source.read()
    word_count = len(text.split(' '))
    print(f"Word count: {word_count}")

# 3.Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.

with open("text11.txt", "r") as source, open("text11_new.txt", "w") as destination:
    text = source.read()
    invalid_word = input("Enter invalid word: ")
    text_new = text.replace(invalid_word, '*' * len(invalid_word))
    count = text.count(invalid_word)
    destination.write(text_new)
    print(f"Invalid count: {count}")
