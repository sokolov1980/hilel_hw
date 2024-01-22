class Person:
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


class Subject:
    __subject = "Subject X"

    def __init__(self, subject=None):
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if 5 < len(subject) < 20:
            self.__subject = subject

    def show_info(self):
        print(f"Subject: {self.subject}")


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


class Teacher(Person, Subject):
    __experience = 0
    __academic_degree = "absent"

    def __init__(self, name, age, subject, experience=None, academic_degree=None):
        Person.__init__(self, name, age)
        Subject.__init__(self, subject)
        self.__experience = experience
        self.__academic_degree = academic_degree

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
        Person.show_info(self)
        Subject.show_info(self)
        print(f"Experience: {self.experience}, Academic degree: {self.academic_degree}")


class Academy(Teacher, Student):
    __name_academy = "Academy"

    def __init__(self, name, age, subject, experience, academic_degree, name_s, age_s, year, education, name_academy=None):
        Teacher.__init__(self, name, age, subject, experience, academic_degree)
        Student.__init__(self, name_s, age_s, year, education)
        self.name_academy = name_academy

    @property
    def name_academy(self):
        return self.__name_academy

    @name_academy.setter
    def name_academy(self, name_academy):
        if 5 < len(name_academy) < 40:
            self.__name_academy = name_academy

    def show_info(self):
        Teacher.show_info(self)
        Student.show_info(self)
        print(f"Academy: {self.name_academy}")


test = Academy("Ivan", 32, "Mathematics", 4, "doctor", "Fedor",
               20, 2, "secondary", "Great Academy")
test.show_info()
print(Academy.mro())

tests: list = [Student("Ivan", 20, 2, "secondary"),
               Student("Vasya", 20, 2, "secondary"),
               Student("Petya", 20, 2, "secondary"),
               Teacher("Fedor", 32, "Mathematics", 4, "doctor")]

for test in tests:
    test.show_info()
