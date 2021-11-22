'''
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
'''


def difference_of_sets():
    print("задача 5_4:")
    first_list = "1 2 3 4 5".split()
    second_list = "4 5 6 7 8".split()
    print("Количество различных чисел: ", len(set(first_list) ^ set(second_list)))
