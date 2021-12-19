'''
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без
исключений (но не более n раз - параметр декоратора). Если превышено количество попыток,
должно быть возбуждено исключение типа TooManyErrors
'''


import random


class TooManyErrors(Exception):
    pass


class RandomizerError(Exception):
    pass


def decorator(n):

    def my_decorator(func):

        def wrapper():
            count = 0
            while True:
                if count == n:
                    break
                elif count > n:
                    raise TooManyErrors('Too many tries')
                result = func()
                print("OUT: ", result)
                if result < 1:
                    raise RandomizerError
                count += 1
        return wrapper

    return my_decorator


@decorator(n=int(input()))
def randomizer():
    '''Generate random number'''
    return random.randrange(0, 10)


randomizer()
