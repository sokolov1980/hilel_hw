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
        print(f"Name: {self.name}, Age: {self.age}", end=' ')


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


class Teacher(Person):
    __experience = 0
    __academic_degree = "absent"

    def __init__(self, name, age, experience=None, academic_degree=None):
        super().__init__(name, age)
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
        super().show_info()
        print(f"Experience: {self.experience}, Academic degree: {self.academic_degree}")


class Teacher(Person):
    __experience = 0
    __academic_degree = "absent"

    def __init__(self, name, age, experience=None, academic_degree=None):
        super().__init__(name, age)
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
        super().show_info()
        print(f"Experience: {self.experience}, Academic degree: {self.academic_degree}")


class Academy:
    __name_academy = "Academy"

    def __init__(self, name_academy=None):
        self.teachers = []
        self.students = []
        self.name_academy = name_academy

    @property
    def name_academy(self):
        return self.__name_academy

    @name_academy.setter
    def name_academy(self, name_academy):
        if 5 < len(name_academy) < 40:
            self.__name_academy = name_academy

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def show_info(self):
        print(f"Academy: {self.name_academy}")
        print("Teachers:")
        for teacher in self.teachers:
            teacher.show_info()
        print("Students:")
        for student in self.students:
            student.show_info()


try:
    academy = Academy("Great Academy")
    teachers: list[Teacher] = [Teacher("Fedor Fedorovich Fedorov", 40, 10, "doctor"),
                               Teacher("Elena Ivanovna Fedorova", 38, 7, "candidate")]
    students: list[Student] = [Student("Ivan Petrov", 19, 2, "secondary"),
                               Student("Vasya Ivanov", 19, 2, "secondary"),
                               Student("Petya Vasilyev", 19, 2, "secondary"),
                               Student("Anna Petrova", 18,  1, "secondary")]
    for teacher in teachers:
        academy.add_teacher(teacher)

    for student in students:
        academy.add_student(student)

    academy.show_info()
except Exception as error:
    print(error)
print(Academy.mro())