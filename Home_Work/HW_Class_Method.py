# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

# статический метод
class Person():
    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else:
            return False
print(Person.is_adult(18))

# метод экземляра (обычные функции в классе)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

v = Vector(1, 2)
print(v.get_coord())

# метод класса
class MaxMin:
    MIN = 0
    MAX = 100

    @classmethod
    def validate(cls, x):
        return cls.MIN <= x <= cls.MAX

print(MaxMin.validate(127))