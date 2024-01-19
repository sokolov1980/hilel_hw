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
        if 0 < len(c_name) < 100:
            self.__city_name = c_name

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if 3 < len(region) < 100:
            self.__region = region

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        if 3 < len(country) < 60:
            self.__country = country

    @property
    def city_res(self):
        return self.__city_residents

    @city_res.setter
    def city_res(self, city_res):
        if 500 < city_res < 38000000:
            self.__city_residents = city_res

    @property
    def postcode(self):
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode):
        if 4 < len(postcode) < 10:
            self.__postcode = postcode

    @property
    def tel_code(self):
        return self.__telephone_code

    @tel_code.setter
    def tel_code(self, tel_code):
        if 2 < len(tel_code) < 8:
            self.__telephone_code = tel_code

    def show_info(self):
        print(f"City: {self.c_name} | Region: {self.region} | Country: {self.country} | City residents: {self.city_res} "
              f"| Postcode: {self.postcode} | Telephone code: {self.tel_code}")


class Cities:
    def __init__(self, cities: list[City] = None):
        self.cities = cities

    def show_cities(self):
        for city in self.cities:
            city.show_info()
            print()

try:
    city1 = City("Kharkov", "Kharkovska oblast", "Ukraine", 2000000, "61000", "+38057")
    city1.show_info()
    city2 = City("London", "Big London", "England", 9500000, "", "+4420")
    city2.show_info()

    cities: list[City] = [City("Kharkov", "Kharkovska oblast", "Ukraine", 2000000, "61000", "+38057"),
                          City("London", "Big London", "England", 9500000, "", "+4420")]
    list_city = Cities(cities)
    list_city.show_cities()
except Exception as error:
    print(f"Error: {error}")

#Завдання 2:
#Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів
# країни, телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).