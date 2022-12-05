# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

# class Сreature:
#     def __init__(self):
#         pass
#     def info(self):
#         print('Это существо')
#
# class Animal(Сreature):
#     def info(self):
#         print('Это животное')
#
# bear = Сreature()
# bear.info()
# bear = Animal()
# bear.info()

class Any:
    def start(self, a=None, b=None):
        if len(a) > 10:
            print(a)
        else:
            print(b)


obj = Any()
obj.start("aslkh", 15)
