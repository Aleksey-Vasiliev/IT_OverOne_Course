# a = [1,5,7]
class Example:
    # Статические поля (переменные класса)
    default_floor = 5
    default_flat = 50
    # def print(self):
    #     print("Hello world")
    # def summa(self):
    #     b = sum(a)
    #     print(b)
    def __init__(self, floor, flat):
        # Динамические поля (переменные объекта)
        self.floor = floor
        self.flat = flat
ex_object = Example(11, 120)
print(ex_object.default_floor)
print(ex_object.floor)
print(ex_object.default_flat)
print(ex_object.flat)
# ex.print()
# ex.summa()