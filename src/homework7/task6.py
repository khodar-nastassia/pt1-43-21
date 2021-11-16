'''
Написать программу которая находит ближайшую степень двойки к введенному числу. 10(8),
20(16), 1(1), 13(16)
'''


def power(number):
    power_of_two = int(number ** 0.5)  # определили степень двойки веденного числа
    if abs(2 ** power_of_two - number) < abs(2 ** (power_of_two + 1) - number):  # ближайшая степень
        print("Ближайшая степень двойки", power_of_two)
    else:
        print("Ближайшая степень двойки", power_of_two + 1)


def main():
    number = int(input('Введите число '))
    power(number)


if __name__ == "__main__":
    main()
