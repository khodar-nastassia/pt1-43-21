'''
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import tasks


def all_task():
    tasks.count_total_price()
    tasks.find_longest_word()
    tasks.remove_extra_symbols()
    tasks.count_upper_lowercase()
    tasks.fibo()
    tasks.number_polindrom()
    tasks.area_of_triangle()
    tasks.split_and_join()
    tasks.swap_cases()
    tasks.square_number()
    tasks.pairs_of_letter()
    tasks.regex_password()
    tasks.fizz_buzz()
    tasks.list_practice()
    tasks.tuple_practice()
    tasks.pairs_of_elements()
    tasks.unic_elements()
    tasks.zero_left()
    tasks.dict_comprehensions()
    tasks.city_country()
    tasks.union_of_sets()
    tasks.difference_of_sets()
    tasks.know_languages()
    tasks.count_of_word()
    tasks.find_greatest_common_factor()


def chosen_task(func_name):
    if func_name == "task2_1":
        tasks.count_total_price()
    if func_name == "task2_2":
        tasks.find_longest_word()
    if func_name == "task2_3":
        tasks.remove_extra_symbols()
    if func_name == "task2_4":
        tasks.count_upper_lowercase()
    if func_name == "task2_5":
        tasks.fibo()
    if func_name == "task2_6":
        tasks.number_polindrom()
    if func_name == "task2_7":
        tasks.area_of_triangle()
    if func_name == "task2_81":
        tasks.split_and_join()
    if func_name == "task2_82":
        tasks.swap_cases()
    if func_name == "task2_83":
        tasks.square_number()
    if func_name == "task2_84":
        tasks.pairs_of_letter()
    if func_name == "task2_85":
        tasks.regex_password()
    if func_name == "task4_1":
        tasks.fizz_buzz()
    if func_name == "task4_2":
        tasks.list_practice()
    if func_name == "task4_3":
        tasks.tuple_practice()
    if func_name == "task4_4":
        tasks.pairs_of_elements()
    if func_name == "task4_5":
        tasks.unic_elements()
    if func_name == "task4_6":
        tasks.zero_left()
    if func_name == "task5_1":
        tasks.dict_comprehensions()
    if func_name == "task5_2":
        tasks.city_country()
    if func_name == "task5_3":
        tasks.union_of_sets()
    if func_name == "task5_4":
        tasks.difference_of_sets()
    if func_name == "task5_5":
        tasks.know_languages()
    if func_name == "task5_6":
        tasks.count_of_word()
    if func_name == "task5_7":
        tasks.find_greatest_common_factor()


def list_tasks(functions):
    for func in functions:
        func()


def runner(*args):
    if len(args) == 0:
        all_task()
    elif len(args) == 1:
        chosen_task(args[0])
    elif len(args) > 1:
        list_tasks(args)


def main():
    runner(tasks.count_total_price, tasks.fizz_buzz, tasks.find_greatest_common_factor)


if __name__ == "__main__":
    main()
