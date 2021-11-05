'''
Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно как в первом
списке, так и во втором.
'''


def main():
    firstList = input('Введите цифры').split()
    secondList = input('Введите цифры').split()
    print(len(set(firstList) | set(secondList)))


if __name__ == "__main__":
    main()
