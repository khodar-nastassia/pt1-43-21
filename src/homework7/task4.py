'''
Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.

Пример:
func(1, 4)   -->  1111010
    1  // 1 в двоичном виде 1
+  10  // 2 в двоичном виде 10
+  11  // 3 в двоичном виде 11
+ 100  // 4 в двоичном виде 100
-----
  122  // 122 в двоичном виде 1111010
'''


def dec_to_bin(num):
    base = 2
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return int(newNum)


def do_binary_pyramid(numbers):
    if 0 <= int(numbers[0]) <= int(numbers[1]):
        total = 0
        for item in range(int(numbers[0]), int(numbers[1]) + 1):
            total += dec_to_bin(item)
        strBin = str(dec_to_bin(total))
        print(strBin)
    else:
        print("Введите корректные данные")


def main():
    numbers = input('Введите два числа больше нуля ').split()
    do_binary_pyramid(numbers)


if __name__ == "__main__":
    main()
