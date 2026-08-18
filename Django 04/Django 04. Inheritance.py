# Human is superclass for Student
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

# Student is subclassed
class Student(Human):
    def __init__(self, name, surname, age, group, mark):
        super().__init__(name, surname, age)
        self.group = group
        self.mark = mark


    def show_info(self):
        print(self.name, self._surname, self.group, self.mark, sep=" -> ")



student = Student("Nadir", "Zamanov", 45, "31_13", 5.6)
student.show_info()


print(isinstance(student, Student))
print(isinstance(student, Human))
# print(isinstance(Student, Human))
print(isinstance(student, object))