'''
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import tasks


def runner(*args):
    func_names = dir(tasks)
    functions = [func_name for func_name in func_names if not func_name.startswith('__')]
    if not len(args):
        for function in functions:
            func = getattr(tasks, function)
            if func.__name__ != 're':
                func()
                print('-----------------------')
    else:
        for function in args:
            func = getattr(tasks, function.__name__)
            func()
            print('-----------------------')


def main():
    runner(tasks.count_total_price, tasks.fizz_buzz, tasks.find_greatest_common_factor)


if __name__ == "__main__":
    main()
