'''
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один из этих списков
'''


def main():
    firstList = input('Введите цифры').split()
    secondList = input('Введите цифры').split()
    print(len(set(firstList) ^ set(secondList)))


if __name__ == "__main__":
    main()
