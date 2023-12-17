# Користувач вводить із клавіатури номер дня тижня (1-7). Необхідно вивести на екран назви дня тижня
try:
    print("Enter the day of the week number (1-7)")
    user_select = int(input("Enter number: "))

    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect day number!")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Error: {error}")