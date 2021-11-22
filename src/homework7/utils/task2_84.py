'''
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').
'''


def pairs_of_letter():
    print("задача 2_84:")
    line = "sjyii"
    if len(line) % 2:
        line += '_'
    print("Пары букв: ", [line[i:i + 2] for i in range(0, len(line), 2)])
