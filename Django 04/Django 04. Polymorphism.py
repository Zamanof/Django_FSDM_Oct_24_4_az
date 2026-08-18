# Human is superclass for Student
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    def get_info(self):
        return self.name, self._surname, self.__age

# Student is subclassed
class Student(Human):
    def __init__(self, name, surname, age, group, mark):
        super().__init__(name, surname, age)
        self.group = group
        self.mark = mark


    def get_info(self):
        return super().get_info(), self.mark, self.group



def foo(obj: Human):
    print(obj.get_info())

student = Student("Nadir", "Zamanov", 45, "FSDM_Oct_24_4_az", 10.5)
human = Human("John", "Doe", 17)

foo(human)
foo(student)