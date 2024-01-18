#Завдання 1:
#Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни, кількість
# жителів міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (Інкапсуляція).

class City:
    __city_name = "no name"
    __region =
    __country =
    __city_residents =
    __postcode =
    __telephone_code =

    def __init__(self, name, age, hobby="no info"):
        self.name = name  # name setter
        self.age = age  # age setter
        self.hobby = hobby  # public field

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) < 30:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 150:
            self.__age = age

    def show_info(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nHobby: {self.hobby}")


#Завдання 2:
#Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів
# країни, телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).