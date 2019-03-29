class Person:
    age = 0

    def __init__(self, age):
        self.age = age

    def print_age(self):
        print(self.age)


class Student(Person):

    number = 10

    def __init__(self, name, age):
        self.name = name
        super(Student, self).__init__(age)

    def print_name(self):
        print(self.__class__.number)

    @classmethod
    def operate_number(cls):
        print(cls.number)

    @staticmethod
    def add(x, y):
        return x + y
