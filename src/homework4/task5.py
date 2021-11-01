# Уникальные элементы в списке
# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
def main():
    items = [int(s) for s in input().split()]
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                break
        else:
            print(items[i], end=' ')


if __name__ == "__main__":
    main()
