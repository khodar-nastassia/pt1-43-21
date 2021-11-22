'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
'''


def split_and_join():
    print("задача 2_81:")
    line = "You are given a string"
    a = line.split(" ")
    a = "-".join(a)
    print(a)
