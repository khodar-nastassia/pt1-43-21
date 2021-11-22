'''
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import sys
sys.path.append('src/homework7/utils/')

import task2_1
import task2_2
import task2_3
import task2_4
import task2_5
import task2_6
import task2_7
import task2_81
import task2_82
import task2_83
import task2_84
import task2_85
import task4_1
import task4_2
import task4_3
import task4_4
import task4_5
import task4_6
import task5_1
import task5_2
import task5_3
import task5_4
import task5_5
import task5_6
import task5_7


def all_task():
    task2_1.count_total_price()
    task2_2.find_longest_word()
    task2_3.remove_extra_symbols()
    task2_4.count_upper_lowercase()
    task2_5.fibo()
    task2_6.number_polindrom()
    task2_7.area_of_triangle()
    task2_81.split_and_join()
    task2_82.swap_cases()
    task2_83.square_number()
    task2_84.pairs_of_letter()
    task2_85.regex_password()
    task4_1.fizz_buzz()
    task4_2.list_practice()
    task4_3.tuple_practice()
    task4_4.pairs_of_elements()
    task4_5.unic_elements()
    task4_6.zero_left()
    task5_1.dict_comprehensions()
    task5_2.city_country()
    task5_3.union_of_sets()
    task5_4.difference_of_sets()
    task5_5.know_languages()
    task5_6.count_of_word()
    task5_7.find_greatest_common_factor()


def chosen_task(func_name):
    match func_name:
        case "task2_1":
            task2_1.count_total_price()
        case "task2_2":
            task2_2.find_longest_word()
        case "task2_3":
            task2_3.remove_extra_symbols()
        case "task2_4":
            task2_4.count_upper_lowercase()
        case "task2_5":
            task2_5.fibo()
        case "task2_6":
            task2_6.number_polindrom()
        case "task2_7":
            task2_7.area_of_triangle()
        case "task2_81":
            task2_81.split_and_join()
        case "task2_82":
            task2_82.swap_cases()
        case "task2_83":
            task2_83.square_number()
        case "task2_84":
            task2_84.pairs_of_letter()
        case "task2_85":
            task2_85.regex_password()
        case "task4_1":
            task4_1.fizz_buzz()
        case "task4_2":
            task4_2.list_practice()
        case "task4_3":
            task4_3.tuple_practice()
        case "task4_4":
            task4_4.pairs_of_elements()
        case "task4_5":
            task4_5.unic_elements()
        case "task4_6":
            task4_6.zero_left()
        case "task5_1":
            task5_1.dict_comprehensions()
        case"task5_2":
            task5_2.city_country()
        case"task5_3":
            task5_3.union_of_sets()
        case"task5_4":
            task5_4.difference_of_sets()
        case"task5_5":
            task5_5.know_languages()
        case"task5_6":
            task5_6.count_of_word()
        case"task5_7":
            task5_7.find_greatest_common_factor()


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
    runner(task2_1.count_total_price, task4_1.fizz_buzz, task5_7.find_greatest_common_factor)


if __name__ == "__main__":
    main()
