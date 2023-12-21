#Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран
try:
    line = input("Enter the line: ")
    dig = 0
    alp = 0
    for i in line:
        if i.isdigit():
            dig +=1
        elif i.isalpha():
            alp += 1
        else:
            alp += 1
    print(f"Result number: {dig}")
    print(f"Result letter: {alp}")
except Exception as error:
    print(f"Error: {error}")