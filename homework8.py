import re
# Написати валідації за допомогою регулярних виразів та протестувати на рiзних кейсах:
# домашній номер телефону (тільки цифри та довжина номера)
number = input("Enter telephone number: ")
for num in number:
    if re.match(r'^\d{7}$', number):
        print(f"Your telephone number: {number}")
        break
    else:
        print(f"Incorrect input. Enter seven digits without separators!")
        break

# Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера) +380501112233
number_m = input("Enter mobile telephone number: ")
for val in number_m:
    if re.match(r'^[+]?\d{12}$', number_m):
        print(f"Your mobile telephone number: {number_m}")
        break
    else:
        print(f"Incorrect input. Enter twelve digits without separators!")
        break


# email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
mail = input("Enter mail address: ")
for val in mail:
    # до собаки от 3 до 20 букв или цифр. также м.б. точка и тире
    if re.match(r'^[\w.\-]{3,20}@gmail\.com$', mail):
        print(f"Your email address: {mail}")
        break
    else:
        print(f"Incorrect input. Enter a name from 3 to 20 characters. E-mail must contain @ and gmail.com")
        break


# ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
name = input("Enter your Full name (last/first/patronymic): ")
for val in name:
    # # v1 первая фамилия м.б. через дефис. каждое слово с большой буквы. учитываем пробелы
    # if re.findall(r'^[A-Z][a-z]{2,19}([-][A-Z][a-z]{2,19})?\s[A-Z][a-z]{2,19}\s[A-Z][a-z]{2,19}$', name):
    #     print(f"Your Full name: {name}")
    #     break
    # #v2 для укр кирилицы. Ї та Є добавкой
    # if re.match(r'^[А-ЯЇЄҐ][а-яЇєґ]{2,20}([-][А-ЯЇЄҐ][а-яїєґ]{2,20})?\s[А-ЯЇЄҐ][а-яїєґ]{2,20}\s[А-ЯЇЄҐґ][а-яїєґ]{2,20}$', name):
    #     print(f"Your Full name: {name}")
    #     break
    # v3 обший - англ, рус, укр
    if re.match(r'^[A-ZА-ЯЇЁЄҐ][a-zа-яЇёєґ]{2,19}([-][A-ZА-ЯЇЁЄҐ][a-zа-яЇёєґ]{2,19})?\s[A-ZА-ЯЇЁЄҐ][a-zа-яЇёєґ]{2,19}\s[A-ZА-ЯЇЁЄҐ][a-zа-яЇёєґ]{2,19}$', name):
        print(f"Your Full name: {name}")
        break
    else:
        print(f"Incorrect input. Enter a first name, patronymic and last name from 2 to 20 characters.")
        break


