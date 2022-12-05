# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

# Декоратор-счетчик
def counter(your_func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return your_func(*args, *kwargs)
    wrapper.count = 0
    return wrapper

# Функция, вызовы которой будем считать, обернутая в декоратор
@counter
def func():
    print('Произошёл вызов функции')

func()
func()
func()

print(f'Количество вызовов функции: {func.count}')
