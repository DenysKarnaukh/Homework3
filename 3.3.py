

lst = [1, 2, 3, 4, 5, 6]

if lst == []:
    result = [[], []]

elif len(lst) == 1:
    result = [lst, []]

elif len(lst) % 2 == 0:
    middle = len(lst) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    result = [first_half, second_half]

else:
    middle = (len(lst) + 1) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    result = [first_half, second_half]

print(result)
