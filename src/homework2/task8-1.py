# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def raw_input():
    return input()


def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    print(a)


if __name__ == "__main__":
    line = raw_input()
    result = split_and_join(line)
