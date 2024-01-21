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

class Faculty(Academy):


class Person(Faculty):

class Subject(Faculty):


class Student(Person):



class Teacher(Person, Subject):



class Group(Student, Teacher):
