#Написати гру "Вгадай число" використовуючи бінарний пошук: гравець загадує число, пк відгадує і показує кількість спроб.


def binary_search(numb, search_item) -> int:
    first_index = 0
    last_index = 49
    attempt = 0
    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        print("Мое число:", middle_index, "правильно?")
        answer = input("Enter yuor answer: ")
        if answer == "=":
            attempt += 1
            print(f"I win! attempt: {attempt}")
            break

        elif answer == "<":
            last_index = middle_index - 1
            attempt += 1

        elif answer == ">":
            first_index = middle_index + 1
            attempt += 1
        else:
            print("Invalid input! Valid characters: '<', '>' and '='")


nums = 50
numbers = list(range(1, nums+1))
search_item = int()
print(numbers)
print(f"Загадайте число, я его отгадаю. Если преложенное мной число меньше вашего - введите <, "
      f"если больше - > , если я угадал введите = ")
try:
    start = binary_search(numbers, search_item)
except Exception as error:
    print(f"Error: {error}")
