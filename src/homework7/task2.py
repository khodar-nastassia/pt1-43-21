'''
Создайте декоратор, который хранит результаты вызовов функции (за все время вызовов, не только
текущий запуск программы)
'''


def counter_dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('count_counter_dec.txt', 'a') as f:
            f.write(f'Результат вызова функции - {res}.\n')
        return res
    return wrapper


@counter_dec
def my_func(message):
    '''Функция выводит сообщение'''
    print(message)


def main():
    my_func('hi')
    my_func('hi')
    my_func('hi')
    my_func('hi')


if __name__ == "__main__":
    main()
