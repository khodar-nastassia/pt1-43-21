'''
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
'''


def counter_dec(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("Функция {0} была вызвана: {1} раз(а)".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter_dec
def my_func(message):
    print(message)


def main():
    my_func('hi')
    my_func('hi')
    my_func('hi')
    my_func('hi')


if __name__ == "__main__":
    main()
