# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП

class Academy(object):
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


class Teacher(Subject):
    __name_teacher = "John Dou"
    __age_t = "no 24 years old"
    __academic_degree = "absent"

    def __init__(self, name_academy, name_faculty, subject, name_teacher=None, age_t=None, academic_degree=None):
        super().__init__(name_academy, name_faculty, subject)
        self.__name_teacher = name_teacher
        self.__age_t = age_t
        self.__academic_degree = academic_degree

    @property
    def name_teacher(self):
        return self.__name_teacher

    @name_teacher.setter
    def name_teacher(self, name_teacher):
        if 10 < len(name_teacher) < 60:
            self.__name_teacher = name_teacher

    @property
    def age_t(self):
        return self.__age_t

    @age_t.setter
    def age_t(self, age_t):
        if 24 <= age_t:
            self.__age_t = age_t

    @property
    def academic_degree(self):
        return self.__academic_degree

    def show_info(self):
        super().show_info()
        print(f"Name teacher: {self.name_teacher}, Age: {self.age_t}, Academic degree: {self.academic_degree}")


class Student(Faculty):
    __name_student = "John Dou"
    __age = "no 18 years old"
    __education = "secondary"

    def __init__(self, name_academy, name_faculty, name_student=None, age=None, education=None):
        Faculty.__init__(self, name_academy, name_faculty)
        # super().__init__(name_academy, name_faculty)
        self.__name_student = name_student
        self.__age = age
        self.__education = education

    @property
    def name_student(self):
        return self.__name_student

    @name_student.setter
    def name_student(self, name_student):
        if 10 < len(name_student) < 60:
            self.__name_student = name_student

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 <= age:
            self.__age = age

    @property
    def education(self):
        return self.__education

    def show_info(self):
        super().show_info()
        print(f"Name student: {self.name_student}, Age: {self.age}, Education: {self.education}")


class Person(Student, Teacher):  # участник учебной группы
    __name_group = "some"
    __quantity = "no data"

    def __init__(self, name_academy, name_faculty, name_student, age, education, subject, name_teacher, age_t,
                 academic_degree, name_group=None, quantity=None):
        Student.__init__(self, name_academy, name_faculty, name_student, age, education)
        Teacher.__init__(self, name_academy, name_faculty, subject, name_teacher, age_t, academic_degree)
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

try:
    first_group: list[Person] = [Person("Hogwarts", "Gryffindor", "Garry Potter", 19, "secondary",
                        "Potions making", "Severus Snape", 35, "doctor", "GD-21",
                        25), Person("Hogwarts", "Gryffindor", "Ron Weasley", 19, "secondary",
                        "Divination", "Sybill Trelawney", 40, "doctor", "GD-21",
                        25), Person("", "", "Dobby", 150, "",
                        "", "", "", "", "", "")]
    for person in first_group:
        person.show_info()
    print(Person.mro())
except Exception as error:
    print(error)
