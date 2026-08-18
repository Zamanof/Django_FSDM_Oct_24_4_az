class Human:
    # name = "Nadir"
    # surname = "Zamanov"
    __count = 0
    def __init__(self, name, surname, age):
        self.name = name            # public
        self._surname = surname     # protected
        self.__age = age            # private
        Human.__count += 1

    def show_info(self):
        print(f"Name: {self.name}, Surname: {self._surname}, Age: {self.__age}")


    @staticmethod
    def show_count():
        return Human.__count

    # def initialize(self, name, surname):
    #     self.name = name
    #     self.surname = surname


# human = Human()
# human.initialize("Salam", "Salamzade")
# print(human.name)
# print(human.surname)
print(Human.show_count())
human = Human("Nadir", "Zamanov", 45)
# print(human.name)
# print(human._surname)
# print(human.__age)
human.show_info()
print(human.show_count())
human1 = Human("Salam", "Salamzade", 25)
print(human1.show_count())


