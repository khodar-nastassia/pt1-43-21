'''
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых
чисел, отсортированных по возрастанию, которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
'''


def get_ranges(numbers):
    numbers.sort()
    chars = []
    startOrder = None
    length = len(numbers)
    for index in range(len(numbers)):
        if (index != length - 1):
            if numbers[index] + 1 == numbers[index + 1]:
                if startOrder is None:
                    startOrder = numbers[index]
                else:
                    continue
            if numbers[index] + 1 != numbers[index + 1]:
                if startOrder is None:
                    chars.append(str(numbers[index]) + ",")
                else:
                    chars.append(str(startOrder) + "-" + str(numbers[index]) + ",")
                startOrder = None
        else:
            if startOrder is not None and numbers[index] + 1 != numbers[index]:
                chars.append(str(startOrder) + "-" + str(numbers[index]))
            else:
                chars.append(str(numbers[index]))
    listToStr = ' '.join([str(elem) for elem in chars]).replace(" ", "")
    print(listToStr)


def main():
    get_ranges([0, 1, 3, 2, 4, 7, 8, 10])
    get_ranges([4, 7, 10])
    get_ranges([2, 3, 8, 9])


if __name__ == "__main__":
    main()
