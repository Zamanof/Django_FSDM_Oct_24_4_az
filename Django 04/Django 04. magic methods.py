class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age

    # def __repr__(self):
    #     return f"{self.name} {self._surname} {self.__age}"

    def __str__(self):
        return "class <Human>"

    def __int__(self):
        return len(self.name)

    def __add__(self, other):
        return self.__age + other.__age

    def __eq__(self, other):
        return self.__age == other.__age


human = Human("Nadir", "Zamanov", 45)
human1 = Human("Salam", "Salamzade", 45)

print(5 + 25.5)
# print(int(human))
# print(human1 + human)
print(human1 == human)

