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


class Student(Person):



class Teacher(Person, Subject):



class Group(Student, Teacher):
