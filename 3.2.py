

lst = [int(x) for x in input("Введіть числа через пробіл: ").split()]

if lst != [] and len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print("Результат:", lst)