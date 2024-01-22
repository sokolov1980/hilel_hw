class Person(object):
    __name = "John Dou"
    __age = "no 18 years old"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 10 < len(name) < 60:
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 <= age:
            self.__age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    __year = 1
    __education = "secondary"

    def __init__(self, name, age, year=None, education=None):
        super().__init__(name, age)
        self.__year = year
        self.__education = education

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if 1 <= year <= 5:
            self.__year = year

    @property
    def education(self):
        return self.__education

    def show_info(self):
        super().show_info()
        print(f"Year: {self.year}, Education: {self.education}")


class Teacher(Person):
    __experience = 0
    __academic_degree = "absent"

    def __init__(self, name, age, experience=None, education=None):
        super().__init__(name, age)
        self.__experience = experience
        self.__education = education

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        if 0 < experience:
            self.__experience = experience

    @property
    def academic_degree(self):
        return self.__academic_degree

    def show_info(self):
        super().show_info()
        print(f"Experience: {self.experience}, Academic degree: {self.academic_degree}")
