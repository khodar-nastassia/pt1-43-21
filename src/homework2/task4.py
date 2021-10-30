# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
#  Учитывать только английские буквы.
import re


def main():
    string = input("Введите символы ")
    result = re.match(r'[aA-zZ]+', string).group()
    countSmallLetter = 0
    for c in result:
        if c.islower():
            countSmallLetter = countSmallLetter + 1
    countBigLetter = len(result) - countSmallLetter
    print(countBigLetter)


if __name__ == "__main__":
    main()
