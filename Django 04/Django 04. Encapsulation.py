class Human:
    __count = 0
    def __init__(self, name, surname, age):
        self.name = name                            # public
        self._surname = surname                     # protected
        self.__age = age if age > 0 else 0          # private
        Human.__count += 1

    def show_info(self):
        print(f"Name: {self.name}, Surname: {self._surname}, Age: {self.__age}")

    # Classic Encapsulation

    # def set_age(self, age: int):
    #     self.__age = age if age > 0 else 0
    #
    # def get_age(self)->int:
    #     return self.__age

    # Property
    @property
    def age(self)-> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        self.__age = value if value > 0 else 0


human = Human("Nadir", "Zamanov", 45)
# human.show_info()
# human.set_age(46)
# print(human.get_age())
print(human.age)
human.age = 49
print(human.age)



