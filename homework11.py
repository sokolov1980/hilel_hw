# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП

class Academy:
    __name_academy = "Academy"

    def __init__(self, name_academy):
        self.name_academy = name_academy

    @property
    def name_academy(self):
        return self.__name_academy

    @name_academy.setter
    def name_academy(self, name_academy):
        if 5 < len(name_academy) < 40:
            self.__name_academy = name_academy

    def show_info(self):
        print(f"Academy: {self.name_academy}")


class Faculty(Academy):
    __name_faculty = "Faculty X"

    def __init__(self, name_academy, name_faculty=None):
        super().__init__(name_academy)
        self.name_faculty = name_faculty

    @property
    def name_faculty(self):
        return self.__name_faculty

    @name_faculty.setter
    def name_faculty(self, name_faculty):
        if 5 < len(name_faculty) < 50:
            self.__name_faculty = name_faculty

    def show_info(self):
        super().show_info()
        print(f"Faculty: {self.name_faculty}")


class Person(Faculty):
    __name_person = "John Dou"
    __sex = "doesn't matter"

    def __init__(self, name_academy, name_faculty, name_person=None, sex=None):
        super().__init__(name_academy, name_faculty)
        self.__name_person = name_person
        self.__sex = sex

    @property
    def name_person(self):
        return self.__name_person

    @name_person.setter
    def name_person(self, name_person):
        if 10 < len(name_person) < 60:
            self.__name_person = name_person

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex == "Male" or sex == "Female":
            self.__sex = sex

    def show_info(self):
        super().show_info()
        print(f"Person: {self.name_person}, Sex: {self.sex}")


class Subject(Faculty):
    __subject = "Subject X"

    def __init__(self, name_academy, name_faculty, subject=None):
        super().__init__(name_academy, name_faculty)
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        if 5 < len(subject) < 20:
            self.__subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")


class Student(Person):
    __age = "no 18 years old"
    __education = "secondary"

    def __init__(self, name_academy, name_faculty, name_person, sex, age=None, education=None):
        super().__init__(name_academy, name_faculty, name_person, sex)
        self.__age = age
        self.__education = education

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 <= age:
            self.__age = age

    def show_info(self):
        super().show_info()
        print(f"Age: {self.age}, Education: {self.education}")


class Teacher(Person, Subject):
    __age_t = "no 24 years old"
    __academic_degree = "absent"

    def __init__(self, name_academy, name_faculty, name_person, sex, subject, age_t=None, academic_degree=None):
        Person.__init__(self, name_academy, name_faculty, name_person, sex)
        Subject.__init__(self, name_academy, name_faculty, subject)
        self.__age_t = age_t
        self.__academic_degree = academic_degree

    @property
    def age_t(self):
        return self.__age_t

    @age_t.setter
    def age_t(self, age_t):
        if 24 <= age_t:
            self.__age_t = age_t

    def show_info(self):
        super().show_info()
        print(f"Age: {self.age_t}, Academic degree: {self.academic_degree}")

class Group(Student, Teacher):
    __name_group = "some"
    __quantity = "no data"

    def __init__(self, name_academy, name_faculty, name_person, sex, age, education, age_t, academic_degree,
                 name_group=None, quantity=None):
        Student.__init__(self, name_academy, name_faculty, name_person, sex, age, education)
        Student.__init__(self, name_academy, name_faculty, name_person, sex, age_t, academic_degree)
        self.__name_group = name_group
        self.__quantity = quantity

    @property
    def name_group(self):
        return self.__name_group

    @name_group.setter
    def name_group(self, name_group):
        if 3 < len(name_group) < 6:
            self.__name_group = name_group

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if 15 <= quantity <= 30:
            self.__quantity = quantity

    def show_info(self):
        super().show_info()
        print(f"Name group: {self.name_group}, Quantity: {self.quantity}")