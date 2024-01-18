#Завдання 1:
#Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни, кількість
# жителів міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (Інкапсуляція).

class City:
    __city_name = "no name"
    __region = "no region name"
    __country = "no country"
    __city_residents = 1000
    __postcode = "no index"
    __telephone_code = "no code"

    def __init__(self, c_name, region, country, city_res, postcode, tel_code):
        self.c_name = c_name
        self.region = region
        self.country = country
        self.city_res = city_res
        self.postcode = postcode
        self.tel_code = tel_code

    @property
    def c_name(self):
        return self.__city_name

    @c_name.setter
    def c_name(self, c_name):
        if 1 < len(c_name) < 100:
            self.__city_name = c_name

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if 4 < len(region) < 100:
            self.__region = region

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if 4 < len(country) < 60:
            self.__country = country

    @property
    def city_res(self):
        return self.__city_residents

    @city_res.setter
    def city_res(self, city_res):
        if 500 < city_res < 38000000:
            self.__city_residents = city_res

    def show_info(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nHobby: {self.hobby}")


#Завдання 2:
#Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів
# країни, телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).