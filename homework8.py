import re
# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# домашній номер телефону (тільки цифри та довжина номера)
number = [input("Enter telephone number: ")]
for val in number:
    if re.findall(r'\d{7}', val) and len(val) == 7:
        print(f"Your telephone number: {number}")
    else:
        print(f"Incorrect input. Enter seven digits without separators!")

# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера) +380501112233
number_m = [input("Enter mobile telephone number: ")]
for val in number_m:
    if re.match(r'[+]?\d{12}', val) and len(val) == 13:
        print(f"Your mobile telephone number: {number_m}")
    else:
        print(f"Incorrect input. Enter twelve digits without separators!")


# email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
mail = [input("Enter mail address: ")]
for val in mail:
    if re.match(r'')



# ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

